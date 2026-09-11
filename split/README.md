# split — ARMv5

## Objective

Exploit a stack-based buffer overflow using a ROP chain to control a function argument.

## Binary Information

- **Architecture:** ARM 32-bit
- **Format:** ELF
- **Linking:** Dynamically linked
- **Offset:** 36 bytes

## Exploitation

Unlike `ret2win`, this challenge requires chaining ROP gadgets to manipulate CPU registers.

According to the ARM calling convention, the first function argument is passed through register `R0`.

The exploit aims to load the address of a useful string into `R0` before transferring execution to the target function.

### ROP Chain

```text
Padding (36 bytes)
       |
       v
pop {r3, pc}
       |
       v
Useful string address
       |
       v
mov r0, r3
       |
       v
Target function
````

The exact gadget sequence and stack adjustments can be found in `exploit.py`.

## Key Concepts

* Return-Oriented Programming (ROP)
* ARM calling convention
* ROP gadgets
* Register manipulation
* Function argument control
