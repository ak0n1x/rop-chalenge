# pivot — ARMv5

## Objective

Exploit a stack buffer overflow by pivoting the stack
to a controlled heap region and executing a larger ROP chain.

## Binary Information

- **Architecture:** ARM 32-bit
- **Format:** ELF
- **Offset:** 36 bytes

## Exploitation

The available stack space is insufficient for the
full ROP chain.

The exploit first places a larger payload in a
controlled heap region.

A stack-pivot gadget redirects the stack pointer
(`SP`) to this region.

### Exploitation Steps

1. Retrieve the leaked heap address.
2. Build a ROP chain in the controlled heap region.
3. Overwrite the return address.
4. Pivot the stack to the heap.
5. Leak the runtime address of `foothold_function`.
6. Calculate the address of `ret2win` using a known offset.
7. Send a second-stage payload to execute `ret2win`.

### Address Calculation

```python
ret2win_addr = foothold_leak + 0x18C
```

### Exploitation Flow

```text
Stack Overflow
      |
      v
Stack Pivot (SP -> Heap)
      |
      v
Execute Heap ROP Chain
      |
      v
Leak Function Address
      |
      v
Calculate ret2win Address
      |
      v
Second-Stage Payload
      |
      v
ret2win()
```

## Key Concepts

- Stack pivoting
- Heap-based ROP chains
- GOT and PLT
- Information disclosure
- Runtime address calculation
- Multi-stage exploitation
