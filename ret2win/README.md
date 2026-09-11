
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

## Disclaimer

This repository is for educational purposes only. All experiments are performed on intentionally vulnerable binaries in a controlled environment.
EOF
```

Ce README présente ton projet, les outils et les challenges sans être trop long.

---

## 4. README — ret2win

Le premier challenge consiste à exploiter un **stack buffer overflow** pour rediriger l'exécution vers une fonction existante.

On va documenter les informations que tu as obtenues.

````bash
cat > ret2win/README.md <<'EOF'
# ret2win — ARMv5

## Objective

Exploit a stack-based buffer overflow to redirect program execution to the `ret2win()` function.

## Binary Information

- **Architecture:** ARM 32-bit
- **Format:** ELF
- **Linking:** Dynamically linked
- **Offset:** 36 bytes

## Exploitation

The vulnerability allows overwriting the saved return address on the stack.

The exploit uses 36 bytes of padding followed by the address of `ret2win()`.

### Payload

```python
payload = b'A' * 36 + p32(ret2win_addr)
````

### Stack Layout

```text
+---------------------+
| Padding (36 bytes)  |
+---------------------+
| ret2win() address   |
+---------------------+
```

## Key Concepts

* Stack buffer overflow
* Return address overwrite
* Control-flow hijacking
* ARM memory layout