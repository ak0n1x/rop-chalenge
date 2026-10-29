# callme — ARMv5

## Objective

Exploit a stack buffer overflow to call three functions
sequentially with specific arguments using ROP.

## Binary Information

- **Architecture:** ARM 32-bit
- **Format:** ELF
- **Offset:** 36 bytes

## Exploitation

The exploit uses a ROP gadget to control registers
`R0`, `R1`, and `R2`, which hold the first three
function arguments according to the ARM calling convention.

### Required Arguments

```text
R0 = 0xdeadbeef
R1 = 0xcafebabe
R2 = 0xd00df00d
```

### ROP Chain

```text
Buffer overflow
      |
      v
pop {r0, r1, r2, lr, pc}
      |
      v
callme_one()
      |
      v
callme_two()
      |
      v
callme_three()
```

The chain prepares the arguments before each
function call using a multi-register POP gadget.

## Key Concepts

- ARM calling convention
- Multi-register ROP gadgets
- Function chaining
- Stack manipulation
