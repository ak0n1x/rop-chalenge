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
