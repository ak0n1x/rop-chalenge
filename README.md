# ARM ROP Challenges

A personal project documenting my progress in binary exploitation and Return-Oriented Programming (ROP) on ARM architectures.

## Objectives

- Understand stack-based buffer overflows.
- Analyze ARM ELF binaries.
- Learn ARM calling conventions.
- Discover and chain ROP gadgets.
- Develop exploits using Python and Pwntools.

## Environment

- **Architecture:** ARMv5 (32-bit)
- **OS:** Linux / WSL2
- **Emulation:** QEMU
- **Tools:** GDB, Ghidra, Pwntools
- **Language:** Python 3

## Challenges

| Challenge | Technique |
|-----------|-----------|
| [ret2win](ret2win/) | Stack buffer overflow and control-flow hijacking |
| [split](split/) | ROP chain and ARM register manipulation |
| [callme](callme/) | Function chaining and ARM calling convention |
| [write4](write4/) | Arbitrary memory writes using ROP gadgets |
| [pivot](pivot/) | Stack pivoting, GOT/PLT leaks and multi-stage exploitation |
## Disclaimer

This repository is for educational purposes only. All experiments are performed on intentionally vulnerable binaries in a controlled environment.
