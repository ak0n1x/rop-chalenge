# write4 — ARMv5

## Objective

Use ROP gadgets to write a string into writable memory
and pass its address to a target function.

## Binary Information

- **Architecture:** ARM 32-bit
- **Format:** ELF
- **Offset:** 36 bytes

## Exploitation

The exploit uses a memory-write gadget to store
the string `flag.txt` in the `.bss` section.

### Memory Write

```text
.bss + 0x00 -> "flag"
.bss + 0x04 -> ".txt"
```

The following gadgets are used:

- `pop {r3, r4, pc}`: Load a value and a destination address.
- `str r3, [r4]`: Write four bytes into memory.
- `pop {r0, pc}`: Pass the string address as a function argument.

### ROP Chain

```text
Buffer overflow
      |
      v
Write "flag" to .bss
      |
      v
Write ".txt" to .bss + 4
      |
      v
R0 = .bss address
      |
      v
print_file()
```

## Key Concepts

- Arbitrary memory writes
- ROP gadgets
- Writable memory (.bss)
- ARM register manipulation
- Function arguments
