Gadgets information
============================================================
0x0000000000007b81 : adc bh, dh ; ret 0x8080 // 10f7c28080
0x000000000000d22d : adc byte ptr [rax], al ; ret // 1000c3
0x000000000001443b : add al, 0x5b ; ret // 045bc3
0x000000000001df97 : add al, 0x6b ; ret // 046bc3
0x000000000000454f : add al, ch ; retf // 00e8cb
0x000000000000a0c0 : add al, ch ; retf -0x6b // 00e8ca95ff
0x0000000000006380 : add al, ch ; retf 0xad // 00e8caad00
0x000000000001317b : add al, ch ; syscall // 00e80f05
0x000000000001c7e9 : add bh, bh ; call qword ptr [rax] // 02ffff10
0x000000000001c819 : add bh, bh ; jmp qword ptr [rdx] // 02ffff22
0x000000000000559f : add bl, dh ; ret // 00f3c3
0x0000000000006413 : add byte ptr [rax], al ; ret // 0000c3
0x000000000000046e : add byte ptr [rax], al ; ret 1 // 0000c20100
0x00000000000009de : add byte ptr [rax], al ; ret 2 // 0000c20200
0x00000000000026ae : add byte ptr [rax], al ; retf // 0000cb
0x0000000000000ae6 : add byte ptr [rax], al ; syscall // 00000f05
0x000000000001bc37 : add byte ptr [rax], bl ; retf -2 // 0018cafeff
0x0000000000006271 : add byte ptr [rcx], ch ; ret // 0029c3
0x000000000001244a : add byte ptr [rcx], ch ; ret 0x8d41 // 0029c2418d
0x000000000001226d : add byte ptr [rcx], ch ; ret 0xd089 // 0029c289d0
0x00000000000120db : add byte ptr [rcx], ch ; ret 0xd129 // 0029c229d1
0x00000000000122cc : add ch, byte ptr [rcx] ; retf -0x17d // 0229ca83fe
0x000000000000e228 : add cl, bl ; retf -0x1525 // 00d9cadbea
0x0000000000005e75 : add cl, ch ; ret // 00e9c3
0x0000000000004268 : add cl, ch ; ret 0xfffb // 00e9c2fbff
0x0000000000007f1e : add cl, ch ; ret 0xfffe // 00e9c2feff
0x00000000000100fc : add cl, ch ; retf // 00e9cb
0x00000000000051d5 : add cl, ch ; retf -6 // 00e9cafaff
0x000000000000659d : add dh, bl ; ret // 02f3c3
0x0000000000010152 : add dword ptr [rax], esp ; ret 0x3174 // 0120c27431
0x000000000000fded : add dword ptr [rax], esp ; ret 0x840f // 0120c20f84
0x000000000000fd1f : add dword ptr [rcx], ecx ; ret 0xfa80 // 0109c280fa
0x0000000000003e6e : add eax, ebx ; jmp rax // 01d8ffe0
0x000000000000dd90 : add eax, ebx ; retf -0x3427 // 01d8cad9cb
0x000000000000f9e1 : add eax, ecx ; jmp rax // 01c8ffe0
0x0000000000008b19 : add eax, edx ; jmp rax // 01d0ffe0
0x000000000000fb19 : add eax, esi ; jmp rax // 01f0ffe0
0x00000000000154b7 : add ebp, dword ptr [rcx] ; ret 0x48d // 0329c28d04
0x0000000000005e57 : add ebp, eax ; ret // 03e8c3
0x000000000000551f : add ebx, esi ; ret // 01f3c3
0x000000000000e769 : add edi, dword ptr [rcx] ; ret 0x894f // 0339c24f89
0x00000000000117b2 : add edx, eax ; jmp rdx // 01c2ffe2
0x0000000000013c68 : add edx, esi ; jmp rdx // 01f2ffe2
0x000000000000f218 : and al, 0xe8 ; ret 0xff43 // 24e8c243ff
0x00000000000159d0 : and al, 8 ; call rax // 2408ffd0
0x000000000001af91 : and bh, bh ; call rsp // 22ffffd4
0x000000000000bee5 : and dword ptr [rax], eax ; ret // 2100c3
0x00000000000041b6 : call 0x10cb2 // e8f5ca0000
0x0000000000006af2 : call 0x35c2 // e8c9caffff
0x000000000000744f : call 0x36d2 // e87cc2ffff
0x0000000000007445 : call 0x3732 // e8e6c2ffff
0x0000000000006e3c : call 0x3942 // e8ffcaffff
0x000000000000a0d3 : call 0x6372 // e898c2ffff
0x0000000000010cf5 : call 0xffffffffe084cf2d // e831c283e0
0x0000000000014e41 : call qword ptr [rax] // ff10
0x00000000000161bb : call qword ptr [rbx] // ff13
0x000000000001a2ab : call qword ptr [rcx] // ff11
0x0000000000016147 : call qword ptr [rdi] // ff17
0x000000000001b463 : call qword ptr [rdx] // ff12
0x0000000000014e21 : call qword ptr [rsi] // ff16
0x000000000000d196 : call r12 // 41ffd4
0x00000000000034d8 : call rax // ffd0
0x000000000001a24b : call rbx // ffd3
0x000000000000f74d : call rcx // ffd1
0x0000000000019da7 : call rdi // ffd7
0x000000000000d197 : call rsp // ffd4
0x00000000000069c0 : cld ; retf // fccb
0x00000000000041b7 : cmc ; retf 0 // f5ca0000
0x000000000000d43c : cmp al, 0x24 ; call rax // 3c24ffd0
0x000000000001d309 : cmp al, 0xff ; call qword ptr [rbx] // 3cffff13
0x000000000001d181 : cmp edi, edi ; call qword ptr [rcx] // 3bffff11
0x000000000001d251 : cmp edi, edi ; jmp rbx // 3bffffe3
0x00000000000041c2 : cmpsb byte ptr [rsi], byte ptr [rdi] ; ret // a6c3
0x0000000000004201 : cmpsd dword ptr [rsi], dword ptr [rdi] ; ret // a7c3
0x000000000000a0d4 : cwde ; ret 0xffff // 98c2ffff
0x000000000000c60f : fdivr st(3), st(0) ; ret // dcf3c3
0x000000000000dd89 : fstpnce st(1), st(0) ; retf -0x3f27 // d9d9cad9c0
0x0000000000008d10 : fsubr st(0) ; retf -0x15 // d8e8caebff
0x0000000000008de8 : fucompi st(0) ; ret 0xfff6 // dfe8c2f6ff
0x000000000001c3a1 : idiv esi ; call qword ptr [rsi] // f7feff16
0x00000000000147e2 : in eax, dx ; ret // edf3c3
0x000000000000406f : in eax, dx ; ret 0x21 // edc22100
0x000000000000ea60 : int 0x80 // cd80
0x0000000000010d22 : ja 0x10d2a ; ret // 7704c3
0x000000000001dfb1 : je 0x1dfb4 ; call qword ptr [rdi] // 74ffff17
0x00000000000034d6 : je 0x34dc ; call rax // 7402ffd0
0x000000000000685d : je 0x6862 ; ret // 7401c3
0x000000000000b1dd : je 0xb1e2 ; ret // 7401c3
0x000000000000b29d : je 0xb2a2 ; ret // 7401c3
0x000000000000b35d : je 0xb362 ; ret // 7401c3
0x0000000000011683 : jmp 0x11651 // ebcb
0x0000000000006309 : jmp 0x62cf // ebc3
0x000000000000c1dc : jmp 0xc1aa // ebcb
0x0000000000007cca : jmp qword ptr [r8] // 43ff20
0x0000000000007ca6 : jmp qword ptr [rax] // ff20
0x000000000001509f : jmp qword ptr [rbx] // ff23
0x00000000000161b3 : jmp qword ptr [rcx] // ff21
0x000000000001c81b : jmp qword ptr [rdx] // ff22
0x0000000000014e28 : jmp qword ptr [rsi] // ff26
0x0000000000005695 : jmp r11 // 41ffe3
0x0000000000003e70 : jmp rax // ffe0
0x0000000000005696 : jmp rbx // ffe3
0x00000000000161cf : jmp rcx // ffe1
0x0000000000016288 : jmp rdi // ffe7
0x00000000000117b4 : jmp rdx // ffe2
0x000000000001a283 : jmp rsi // ffe6
0x0000000000015e73 : jmp rsp // ffe4
0x000000000001dfe1 : jne 0x1dfe4 ; jmp rax // 75ffffe0
0x000000000001e0f1 : jp 0x1e0f4 ; jmp qword ptr [rax] // 7affff20
0x000000000000663d : jp 0x6634 ; ret // 7af3c3
0x00000000000161cd : jrcxz 0x161cf ; jmp rcx // e3feffe1
0x000000000000e70f : lahf ; ret 0x2ce9 // 9fc2e92c
0x00000000000127fa : lahf ; ret 0xd021 // 9fc221d0
0x0000000000006af3 : leave ; retf -1 // c9caffff
0x0000000000007f9b : lodsb al, byte ptr [rsi] ; ret 0xf0 // acc2f000
0x000000000000e672 : loop 0xe64f ; retf -0x3380 // e2d9ca80cc
0x00000000000066c3 : loopne 0x66f1 ; ret // e02ac3
0x00000000000066f5 : loopne 0x6736 ; ret // e03dc3
0x000000000000c891 : mov bh, 0x29 ; ret 0xc985 // b729c285c9
0x000000000000d143 : mov bh, 0xf3 ; ret // b7f3c3
0x000000000001a1f5 : mov bh, bh ; call qword ptr [rax] // 88ffff10
0x000000000001a2a9 : mov bh, bh ; call qword ptr [rcx] // 88ffff11
0x000000000001a249 : mov bh, bh ; call rbx // 88ffffd3
0x000000000001a2a1 : mov bh, bh ; jmp qword ptr [rax] // 88ffff20
0x000000000001ac49 : mov dh, 0xfe ; call rsp // b6feffd4
0x0000000000010d02 : mov dword ptr [rdi], edx ; ret // 8917c3
0x0000000000010cbe : mov dword ptr [rdi], esi ; ret // 8937c3
0x0000000000010c9e : mov eax, dword ptr [rdi] ; ret // 8b07c3
0x000000000000ee21 : mov eax, ecx ; ret // 89c8c3
0x0000000000005569 : mov eax, edx ; ret // 89d0c3
0x000000000000ca7d : mov eax, esi ; ret // 89f0c3
0x0000000000005556 : mov ebp, esp ; call rax // 89e5ffd0
0x000000000001b219 : mov edi, dr1 ; call rsp // 8cffffd4
0x000000000000d40e : mov edi, dword ptr [rbx] ; call rax // 8b3bffd0
0x000000000001b1d9 : mov edi, edi ; call rsp // 89ffffd4
0x00000000000145ce : mov edi, esi ; jmp rax // 89f7ffe0
0x000000000000f74b : mov edi, esp ; call rcx // 89e7ffd1
0x0000000000014eba : neg eax ; ret // f7d8c3
0x0000000000005c5f : nop ; pop rbx ; ret // 905bc3
0x00000000000042d4 : nop ; ret 0x21 // 90c22100
0x00000000000054d3 : or al, 0x5d ; jmp rax // 0c5dffe0
0x0000000000013750 : or al, ch ; retf 1 // 08e8ca0100
0x0000000000006cce : or bl, dh ; ret // 08f3c3
0x000000000000588e : or ebx, esi ; ret // 09f3c3
0x000000000001cbb9 : or edi, edi ; call qword ptr [rdx] // 09ffff12
0x00000000000162b5 : out 0xfe, al ; jmp rdi // e6feffe7
0x000000000000d195 : out dx, al ; call r12 // ee41ffd4
0x0000000000014881 : out dx, al ; ret // eef3c3
0x000000000000424e : out dx, al ; ret 0x21 // eec22100
0x000000000000d068 : out dx, eax ; ret // eff3c3
0x0000000000006c7d : out dx, eax ; retf // efcb
0x0000000000006229 : pop r12 ; ret // 415cc3
0x0000000000005c23 : pop r13 ; ret // 415dc3
0x000000000000beda : pop r14 ; ret // 415ec3
0x0000000000004b19 : pop r15 ; ret // 415fc3
0x0000000000005487 : pop rbp ; jmp rax // 5dffe0
0x0000000000005490 : pop rbp ; ret // 5dc3
0x00000000000062e5 : pop rbx ; pop rbp ; ret // 5b5dc3
0x0000000000005c60 : pop rbx ; ret // 5bc3
0x000000000000d8ab : pop rcx ; ret 0x2e0f // 59c20f2e
0x000000000000968f : pop rdi ; pop rbp ; ret // 5f5dc3
0x0000000000004b1a : pop rdi ; ret // 5fc3
0x000000000000bedb : pop rsi ; ret // 5ec3
0x000000000000622a : pop rsp ; ret // 5cc3
0x000000000001ddc6 : push rbp ; ret // 55c3
0x000000000000c55a : push rbx ; ret // fff3c3
0x00000000000034de : ret // c3
0x000000000000d95d : ret 0 // c20000
0x000000000000d096 : ret 0x10eb // c2eb10
0x000000000000c545 : ret 0x1874 // c27418
0x00000000000132c4 : ret 0x1be // c2be01
0x0000000000015440 : ret 0x1db // c2db01
0x000000000000c248 : ret 0x1f0f // c20f1f
0x000000000000ea2d : ret 0x200 // c20002
0x0000000000004070 : ret 0x21 // c22100
0x000000000000b542 : ret 0x2140 // c24021
0x00000000000096b5 : ret 0x216e // c26e21
0x000000000000961e : ret 0x216f // c26f21
0x00000000000080ce : ret 0x2184 // c28421
0x000000000000778a : ret 0x218d // c28d21
0x0000000000004eb1 : ret 0x21b5 // c2b521
0x00000000000039b2 : ret 0x21b8 // c2b821
0x00000000000037b2 : ret 0x21b9 // c2b921
0x00000000000035b2 : ret 0x21ba // c2ba21
0x0000000000003ce5 : ret 0x21c8 // c2c821
0x000000000000a07c : ret 0x2ae9 // c2e92a
0x000000000000e710 : ret 0x2ce9 // c2e92c
0x000000000000d8ac : ret 0x2e0f // c20f2e
0x000000000000c666 : ret 0x2eb9 // c2b92e
0x0000000000013069 : ret 0x30be // c2be30
0x0000000000013546 : ret 0x3145 // c24531
0x0000000000010154 : ret 0x3174 // c27431
0x0000000000014adb : ret 0x3273 // c27332
0x000000000000d122 : ret 0x3374 // c27433
0x0000000000014644 : ret 0x348 // c24803
0x0000000000015af6 : ret 0x3840 // c24038
0x000000000000bfed : ret 0x3948 // c24839
0x00000000000104e9 : ret 0x3949 // c24939
0x0000000000013c01 : ret 0x4173 // c27341
0x0000000000005a66 : ret 0x4801 // c20148
0x0000000000008759 : ret 0x4808 // c20848
0x000000000000d05a : ret 0x4810 // c21048
0x000000000000e45a : ret 0x4830 // c23048
0x000000000000d105 : ret 0x4876 // c27648
0x00000000000154b9 : ret 0x48d // c28d04
0x000000000000d92f : ret 0x48f3 // c2f348
0x0000000000005672 : ret 0x4901 // c20149
0x000000000001519c : ret 0x4c01 // c2014c
0x000000000000e823 : ret 0x4d08 // c2084d
0x000000000000e5f2 : ret 0x4e9 // c2e904
0x000000000000e764 : ret 0x4f08 // c2084f
0x0000000000009b8b : ret 0x58b // c28b05
0x0000000000013350 : ret 0x5d5b // c25b5d
0x000000000000f9db : ret 0x6348 // c24863
0x000000000000eb24 : ret 0x66c3 // c2c366
0x00000000000123ea : ret 0x6eb8 // c2b86e
0x0000000000007b83 : ret 0x8080 // c28080
0x0000000000015460 : ret 0x8141 // c24181
0x00000000000096c6 : ret 0x8341 // c24183
0x0000000000005fd9 : ret 0x8348 // c24883
0x0000000000005992 : ret 0x8401 // c20184
0x000000000000fdef : ret 0x840f // c20f84
0x000000000000e439 : ret 0x8545 // c24585
0x000000000000ae66 : ret 0x8548 // c24885
0x000000000000b215 : ret 0x854d // c24d85
0x000000000000fdd3 : ret 0x8941 // c24189
0x0000000000012b5f : ret 0x8944 // c24489
0x00000000000096d0 : ret 0x8945 // c24589
0x000000000000b422 : ret 0x8948 // c24889
0x00000000000047cd : ret 0x894c // c24c89
0x000000000001339a : ret 0x894d // c24d89
0x000000000000e76b : ret 0x894f // c24f89
0x0000000000004d93 : ret 0x8b48 // c2488b
0x00000000000087e5 : ret 0x8b4c // c24c8b
0x00000000000150dd : ret 0x8d04 // c2048d
0x000000000001244c : ret 0x8d41 // c2418d
0x0000000000005e09 : ret 0x8d48 // c2488d
0x0000000000015535 : ret 0x8d49 // c2498d
0x0000000000008379 : ret 0x8d4c // c24c8d
0x000000000000953f : ret 0x970f // c20f97
0x000000000000c774 : ret 0x974 // c27409
0x0000000000003fce : ret 0xb // c20b00
0x000000000000f779 : ret 0xb1e9 // c2e9b1
0x0000000000006050 : ret 0xb60f // c20fb6
0x000000000000e69c : ret 0xb9e9 // c2e9b9
0x0000000000005d61 : ret 0xc0 // c2c000
0x0000000000004e4e : ret 0xc031 // c231c0
0x00000000000154d4 : ret 0xc148 // c248c1
0x0000000000006445 : ret 0xc208 // c208c2
0x0000000000009329 : ret 0xc2eb // c2ebc2
0x0000000000015693 : ret 0xc35b // c25bc3
0x0000000000007e12 : ret 0xc601 // c201c6
0x000000000000954c : ret 0xc985 // c285c9
0x000000000000f6be : ret 0xcaeb // c2ebca
0x00000000000087c2 : ret 0xcb75 // c275cb
0x0000000000011682 : ret 0xcbeb // c2ebcb
0x0000000000004ce8 : ret 0xd009 // c209d0
0x000000000000fe1d : ret 0xd020 // c220d0
0x00000000000127fb : ret 0xd021 // c221d0
0x000000000001226f : ret 0xd089 // c289d0
0x00000000000120dd : ret 0xd129 // c229d1
0x00000000000158e9 : ret 0xd138 // c238d1
0x0000000000013859 : ret 0xd148 // c248d1
0x000000000000830a : ret 0xd2e9 // c2e9d2
0x0000000000010cf7 : ret 0xe083 // c283e0
0x000000000001cb33 : ret 0xe0a // c20a0e
0x00000000000097ef : ret 0xe183 // c283e1
0x0000000000007b74 : ret 0xe281 // c281e2
0x000000000000e704 : ret 0xe283 // c283e2
0x00000000000117b3 : ret 0xe2ff // c2ffe2
0x00000000000154ca : ret 0xe889 // c289e8
0x000000000001174a : ret 0xe9 // c2e900
0x0000000000007f9c : ret 0xf0 // c2f000
0x0000000000006e52 : ret 0xf01 // c2010f
0x0000000000007e1a : ret 0xf375 // c275f3
0x000000000000fa84 : ret 0xf44 // c2440f
0x0000000000003ec3 : ret 0xf631 // c231f6
0x000000000000ccf1 : ret 0xf66 // c2660f
0x000000000000e632 : ret 0xf6e9 // c2e9f6
0x000000000000fd21 : ret 0xfa80 // c280fa
0x000000000000db94 : ret 0xff3 // c2f30f
0x0000000000003ef8 : ret 0xff31 // c231ff
0x000000000000f21a : ret 0xff43 // c243ff
0x000000000000b7ca : ret 0xff7e // c27eff
0x0000000000012d48 : ret 0xfff3 // c2f3ff
0x0000000000008dea : ret 0xfff6 // c2f6ff
0x000000000000426a : ret 0xfffb // c2fbff
0x000000000000c3ba : ret 0xfffc // c2fcff
0x0000000000007f20 : ret 0xfffe // c2feff
0x0000000000007447 : ret 0xffff // c2ffff
0x0000000000000470 : ret 1 // c20100
0x00000000000009e0 : ret 2 // c20200
0x0000000000007e60 : ret 4 // c20400
0x00000000000026b0 : retf // cb
0x0000000000008d12 : retf -0x15 // caebff
0x000000000000e22a : retf -0x1525 // cadbea
0x00000000000122ce : retf -0x17d // ca83fe
0x00000000000092c4 : retf -0x1d7f // ca81e2
0x000000000000c53f : retf -0x2cb7 // ca49d3
0x000000000000e441 : retf -0x2d7c // ca84d2
0x000000000000e674 : retf -0x3380 // ca80cc
0x000000000000dd92 : retf -0x3427 // cad9cb
0x0000000000006b02 : retf -0x35 // cacbff
0x000000000000c6e5 : retf -0x367b // ca85c9
0x000000000000dd8b : retf -0x3f27 // cad9c0
0x000000000000ce75 : retf -0x3fcf // ca31c0
0x00000000000120cc : retf -0x53f // cac1fa
0x000000000000e70a : retf -0x57d // ca83fa
0x0000000000012384 : retf -0x5d7 // ca29fa
0x000000000000a0c2 : retf -0x6b // ca95ff
0x000000000000a992 : retf -0x72 // ca8eff
0x0000000000007f70 : retf -0x73f1 // ca0f8c
0x000000000000883a : retf -0x74b4 // ca4c8b
0x0000000000011bd7 : retf -0x76b8 // ca4889
0x000000000001a538 : retf -0x7b // ca85ff
0x000000000000c89b : retf -0x7cb7 // ca4983
0x0000000000007306 : retf -0x7cb8 // ca4883
0x000000000001a4b4 : retf -0x7e // ca82ff
0x0000000000006af4 : retf -1 // caffff
0x000000000001bc39 : retf -2 // cafeff
0x000000000000e376 : retf -5 // cafbff
0x00000000000051d7 : retf -6 // cafaff
0x00000000000041b8 : retf 0 // ca0000
0x0000000000005442 : retf 0x107 // ca0701
0x00000000000058c7 : retf 0x14c // ca4c01
0x000000000000f6c0 : retf 0x1f0f // ca0f1f
0x00000000000039a2 : retf 0x21b8 // cab821
0x00000000000037a2 : retf 0x21b9 // cab921
0x00000000000035a2 : retf 0x21ba // caba21
0x0000000000003cde : retf 0x21c8 // cac821
0x0000000000011f35 : retf 0x3941 // ca4139
0x00000000000110a9 : retf 0x4864 // ca6448
0x0000000000007fa3 : retf 0xa7d // ca7d0a
0x0000000000006382 : retf 0xad // caad00
0x000000000000d05e : retf 0xd73 // ca730d
0x000000000000d050 : retf 0xe72 // ca720e
0x000000000000d934 : retf 0xff3 // caf30f
0x0000000000013752 : retf 1 // ca0100
0x0000000000009b12 : retf 2 // ca0200
0x000000000000c3b8 : sbb al, ch ; ret 0xfffc // 18e8c2fcff
0x000000000001cd19 : sbb edi, edi ; call rdi // 1bffffd7
0x000000000000e5a2 : scasd eax, dword ptr [rdi] ; ret 0x3948 // afc24839
0x0000000000007b72 : shl byte ptr [rcx], 1 ; ret 0xe281 // d021c281e2
0x00000000000092c2 : shl dword ptr [rcx], 1 ; retf -0x1d7f // d121ca81e2
0x0000000000004193 : stc ; ret // f9c3
0x0000000000015e71 : sub al, 0xff ; jmp rsp // 2cffffe4
0x0000000000015544 : sub eax, edx ; ret // 29d0c3
0x0000000000000ae8 : syscall // 0f05
0x000000000001b351 : test al, 0xff ; jmp rsp // a8ffffe4
0x00000000000042c9 : wait ; ret 0x21 // 9bc22100
0x000000000000c3de : xchg eax, ebp ; ret // 95c3
0x0000000000005fd8 : xchg eax, ebp ; ret 0x8348 // 95c24883
0x000000000000c76b : xchg eax, ebp ; ret 0x8548 // 95c24885
0x0000000000008d7c : xchg eax, ebp ; ret 0xb60f // 95c20fb6
0x000000000000954b : xchg eax, ebp ; ret 0xc985 // 95c285c9
0x000000000000fe1c : xchg eax, ebp ; ret 0xd020 // 95c220d0
0x00000000000158e8 : xchg eax, ebp ; ret 0xd138 // 95c238d1
0x0000000000003ef7 : xchg eax, ebp ; ret 0xff31 // 95c231ff
0x000000000000c50e : xchg eax, ecx ; ret // 91f3c3
0x00000000000042df : xchg eax, ecx ; ret 0x21 // 91c22100
0x000000000000ef93 : xchg eax, edi ; ret 0x8348 // 97c24883
0x00000000000042fa : xchg eax, edx ; ret 0x21 // 92c22100
0x00000000000146e6 : xchg eax, edx ; ret 0x348 // 92c24803
0x000000000000953e : xchg eax, edx ; ret 0x970f // 92c20f97
0x0000000000015af5 : xchg eax, esp ; ret 0x3840 // 94c24038
0x00000000000096c5 : xchg eax, esp ; ret 0x8341 // 94c24183
0x000000000000e438 : xchg eax, esp ; ret 0x8545 // 94c24585
0x000000000000fdd2 : xchg eax, esp ; ret 0x8941 // 94c24189
0x000000000000604f : xchg eax, esp ; ret 0xb60f // 94c20fb6
0x000000000001598e : xchg eax, esp ; ret 0xc031 // 94c231c0
0x0000000000006444 : xchg eax, esp ; ret 0xc208 // 94c208c2
0x0000000000004ce7 : xchg eax, esp ; ret 0xd009 // 94c209d0
0x00000000000097ee : xchg eax, esp ; ret 0xe183 // 94c283e1
0x000000000001b419 : xchg esi, edi ; jmp qword ptr [rax] // 87feff20
0x0000000000006700 : xor eax, eax ; ret // 31c0c3

Unique gadgets found: 375
