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
        goodSections = [".text"] #[".interp", ".note.ABI-tag", ".note.gnu.build-id", ".gnu.hash", ".hash", ".dynsym", ".dynstr", ".gnu.version", ".gnu.version_r", ".rela.dyn", ".rela.plt", ".init", ".plt", ".text", ".fini", ".rodata", ".eh_frame_hdr", ".eh_frame"]
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

            for filename in sys.argv[4:]:
                lengthHex = (int(sys.argv[3])*16)+2
                nbInstru = int(sys.argv[3])
                nbGadget = 0
                r = getHexStreamsFromElfExecutableSections(filename)
                print "Found ", len(r), " executable sections:"
                i = 0
                for s in r:
                    print "   ", i, ": ", s['name'], "0x", hex(s['addr']), s['hexStream']
                    i += 1
                    hexdata = s['hexStream']

                    #Part to find ret instructions and extract gadget
                    badInstruct = ['jmp', 'jmpq', 'jne', 'js', 'jns','jg', 'jge', 'je', 'callq', 'call', 'jb', 'jbe','leave']
                    ret = 'c3'
                    for i, _ in enumerate(hexdata):
                        if hexdata[i:i + len(ret)] == ret:
                            gadget = hexdata[i-lengthHex: i+2]
                            gadget = convertXCS(gadget)
                            offset = 0
                            disasCode = md.disasm_lite(gadget, offset)
                            strList = ['']

                            for (address, size, mnemonic, op_str) in disasCode:
                                endRet = ''
                                if str(mnemonic) not in badInstruct :
                                    strList.append([address, mnemonic, op_str])
                            #print str(strList[len(strList)-1][1])
                            last = strList[-1]
                            if str(last[1]) == 'ret':
                                print 'gadget : \n'
                                nbGadget += 1
                                for a in strList[len(strList)-nbInstru-1:len(strList)]:
                                    print ("%s      %s %s \n") % (a[0], a[1], a[2])
                                    #print '%s' % ' \n'.join(map(str, strList))



