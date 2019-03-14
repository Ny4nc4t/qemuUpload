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
    
    if len(s) % 2 != 0:
        print "Input must be multiple of 2!"
        return 0

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

        if sys.argv[2] == '-length':#I check if there is -length argument

            # branInst = ["jmp", "je", "jz","jne","jnz","jg","jnle","jge","jnl","jl","jnge","jle","jng", "ja","jnbe","jnae","jxcz","jc","jnc"
            #             , "jo","jno","jp","jpe","jnp","jpo","js","jns", "call", "callq", "ret", "retq"]
            badInstruct = ['jmp', 'jmpq', 'jne', 'js', 'jns','jg', 'jge', 'je', 'callq', 'call', 'jb', 'jbe','leave']
            retHex = ['c3','cb']
            count = 0
            md = Cs(CS_ARCH_X86, CS_MODE_64)
            for filename in sys.argv[4:]: #for filename in sys.argv[2:]:
                r = getHexStreamsFromElfExecutableSections(filename)
                print "Found ", len(r), " executable sections:"
                i = 0

                for s in r:
                    print "   ", i, ": ", s['name'], "0x", hex(s['addr'])#, s['hexStream']
                    i += 1

                    hexdata = s['hexStream']

                    for j, _ in enumerate(hexdata):

                        if str(hexdata[j : j + 2]) in retHex:
                            count+= 1
                            #print str(hexdata[i+2:])
                            flag = 1

                            gadget = hexdata[j - (int(sys.argv[3])* 2 * 15 ) : j + 2]  # gadget = hexdata[0 : 30]. Ici on multiplie par 2 le length

                            #print (gadget)

                            gadget = convertXCS(gadget)

                            offset = 0

                            instList = []
                            disassCode = md.disasm_lite(gadget, offset)


                            for (address, size, mnemonic, op_str) in disassCode:
                                instList.append([mnemonic, op_str])
                                #print ("  %s \n")% (mnemonic)


                            for a in range(len(instList)-int(sys.argv[3])-1,len(instList)-1): 
                                print 2
                                if instList and str(instList[a][0]) in badInstruct:
                                    print ("mauvais  %s \n") % (mnemonic)
                                    flag = 0



                            if instList and str(instList[-1][0]) == ('ret') and flag == 1:

                                print "gadget: \n"
                                for ( mnemonic, op_str) in instList[- int(sys.argv[3])-1:]:#J 'affiche length -1 dernier valeur
                                    print ("  %s %s \n") % (mnemonic, op_str)


                    print ("Count %s" % count)



