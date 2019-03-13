import sys
from capstone import *
import binascii

from elftools.elf.constants import SH_FLAGS
from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection

##############################################################
# takes a string of arbitrary length and formats it 0x for Capstone
def convertXCS(s):
    if len(s) < 2: 
        print "Input too short!"
        return 0
    
    # if len(s) % 2 != 0:
    #     print "Input must be multiple of 2!"
    #     return 0

    conX = ''
    
    for i in range(0, len(s), 2):
        b = s[i:i+2]
        b = chr(int(b, 16))
        conX = conX + b
    return conX


##############################################################

def getHexStreamsFromElfExecutableSections(filename):
    print "Processing file:", filename
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        
        execSections = []
        goodSections = [".text"]#, ".interp", ".note.ABI-tag", ".note.gnu.build-id", ".gnu.hash", ".hash", ".dynsym", ".dynstr", ".gnu.version", ".gnu.version_r", ".rela.dyn", ".rela.plt", ".init", ".plt", ".text", ".fini", ".rodata", ".eh_frame_hdr", ".eh_frame"]
        checkedSections = [".init", ".plt", ".text", ".fini"]
        
        for nsec, section in enumerate(elffile.iter_sections()):

            # check if it is an executable section containing instructions
            
            # good sections we know so far:
            #.interp .note.ABI-tag .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt .init .plt .text .fini .rodata .eh_frame_hdr .eh_frame
        
            if section.name not in goodSections:
            
                continue
            
            # add new executable section with the following information
            # - name
            # - address where the section is loaded in memory
            # - hexa string of the instructions
            name = section.name
            addr = section['sh_addr']
            byteStream = section.data()
            hexStream = binascii.hexlify(byteStream)
            newExecSection = {}
            newExecSection['name'] = name
            newExecSection['addr'] = addr
            newExecSection['hexStream'] = hexStream
            execSections.append(newExecSection)

        return execSections


if __name__ == '__main__':
    if sys.argv[1] == '--test':
        if str(sys.argv[2]) == '-length':
            md = Cs(CS_ARCH_X86, CS_MODE_64)
            nbret = 0
            for filename in sys.argv[4:]:
                lengthHex = (int(sys.argv[3])*30)
                nbInstru = int(sys.argv[3])
                nbGadget = 0

                r = getHexStreamsFromElfExecutableSections(filename)
                print "Found ", len(r), " executable sections:"
                i = 0
                for s in r:
                    print "   ", i, ": ", s['name'], "0x", hex(s['addr']) #, s['hexStream']
                    i += 1
                    hexdata = s['hexStream']

                    #Part to find ret instructions and extract gadget
                    badInstruct = ['jmp', 'jmpq', 'jne', 'js', 'jns','jg', 'jge', 'je', 'callq', 'call', 'jb', 'jbe','leave', 'ret', 'retq', 'retf', 'retn']
                    ret = ['c3', 'cb', 'c2', 'ca']
                    for i, _ in enumerate(hexdata): #loops through hex string
                        #TODO the problem might be here. Splitting arbitrarily hex string might result into wrong
                        #assembly instructions and thus wrong gadgets
                        if str(hexdata[i:i + 2]) in ret: #if it finds a ret instruction in hex it gets in the if
                            # takes the bytes before ret, depending on the length specified
                            gadget = hexdata[i-lengthHex: i+2]

                            gadget = convertXCS(gadget)
                            print gadget
                            offset = 0
                            #counts number of return functions discovered
                            nbret += 1
                            # turns hex string extracted into disasCode to assembly instructions
                            disasCode = md.disasm_lite(gadget, offset)
                            strList = []
                            out = False
                            isUseless = True
                            # appends the assembly instructions into strList,
                            # one entry for one assembly instruction
                            for (address, size, mnemonic, op_str) in disasCode:
                                strList.append([address, mnemonic, op_str])
                            #checks that the list is not empty and that the last instruction is a ret
                            if strList and str(strList[-1][1]) == ('ret' or 'retq' or 'retf' or 'retn'):
                                #checks that the instructions in strList (taking only the required number, cfr length)
                                # are not contained inside the list of bad instructions, such as jumps, calls, etc
                                #furthermore I added a check to get only the instructions I want and find precise gadgets
                                for a in strList[len(strList)-nbInstru-1:len(strList)-1]:
                                    if str(a[1]) in badInstruct:
                                        out = True

                                    #uncomment and modify the following two lines to enable specific gadget search
                                    # if str(a[1]) == 'pop' and str(a[2]) == 'rsi':
                                    #     isUseless = False
                                #prints the selected gadgets along with their address offset
                                if not out and isUseless:
                                    nbGadget += 1
                                    # print 'gadget at %x : \n' % (i- lengthHex + int(strList[0][0])+ int(strList[len(strList) - nbInstru - 1][0]))
                                    for a in strList[len(strList) - nbInstru - 1:len(strList)]:
                                        print ("%x      %s %s \n") % (a[0], a[1], a[2])
                                    #print ("%x      %s %s \n") % (strList[-1][0], strList[-1][1], strList[-1][2])
                                    #print '%s' % ' \n'.join(map(str, strList))
                print nbGadget
                print nbret

 # for filename in sys.argv[4:]:
            #     length = (int(sys.argv[3])*2)+2
            #     r = getHexStreamsFromElfExecutableSections(filename)
            #     print "Found ", len(r), " executable sections:"
            #     i = 0
            #     for s in r:
            #         print "   ", i, ": ", s['name'], "0x", hex(s['addr']), s['hexStream']
            #         i += 1
            #         hexdata = s['hexStream']
            #
            #         #Part to find ret instructions and extract gadget
            #         badInstruct = ['jmp', 'jmpq', 'jne', 'js', 'jns','jg', 'jge', 'je', 'callq', 'call', 'jb', 'jbe','leave']
            #         ret = 'c3'
            #         for i, _ in enumerate(hexdata):
            #             if hexdata[i:i + len(ret)] == ret:
            #                 gadget = hexdata[i-length: i+2]
            #                 gadget = convertXCS(gadget)
            #                 offset = 0
            #                 disasCode = md.disasm_lite(gadget, offset)
            #                 strList = ['gadget : \n']
            #
            #                 for (address, size, mnemonic, op_str) in disasCode:
            #                     endRet = ''
            #                     if str(mnemonic) not in badInstruct :
            #                         endRet = str(mnemonic)
            #                         strList.append(("%s      %s %s \n") %(address,mnemonic, op_str))
            #                     if endRet == 'ret' :
            #                         print '%s' % ' \n'.join(map(str, strList))
