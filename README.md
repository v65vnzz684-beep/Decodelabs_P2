#  Caesar Cipher — Basic Encryption & Decryption

A Python implementation of the classic Caesar Cipher, built as part of the **DecodeLabs Cybersecurity Industrial Training Program (Batch 2026)** — Project 2.

---

##  What Is a Caesar Cipher?

The Caesar Cipher is one of the oldest and simplest encryption techniques. Each letter in the plaintext is shifted a fixed number of positions along the alphabet. The same key is used to reverse the process (decryption), making it a **symmetric cipher**.

**Encryption formula:** `E(x) = (x + n) % 26`  
**Decryption formula:** `D(x) = (x - n) % 26`

Where `x` is the letter's position (0–25) and `n` is the shift key.

---

##  Features

- Encrypts any text using a user-defined shift key
- Decrypts the ciphertext back to the original message
- Preserves case (uppercase stays uppercase, lowercase stays lowercase)
- Non-alphabetic characters (spaces, numbers, punctuation) are passed through unchanged
- Handles large shift values gracefully using modulo 26

---



**Example session:**

```
Enter text to encrypt: Hello World
Enter shift amount (1-25): 3

Original:  Hello World
Encrypted: Khoor Zruog
Decrypted: Hello World
```

---

##  How the Code Works

```python
def encrypt(text, shift):
    shift_amount = shift % 26          # normalize large shifts

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            # subtract base → shift → wrap with % 26 → add base back
            encrypted_text += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            encrypted_text += char     # leave non-letters unchanged
```

**Step-by-step for `'A'` with shift `3`:**

| Step | Operation | Value |
|------|-----------|-------|
| Start | Character | `'A'` |
| `ord('A')` | ASCII value | `65` |
| `- base (65)` | Normalize to 0–25 | `0` |
| `+ shift (3)` | Apply cipher | `3` |
| `% 26` | Wrap around alphabet | `3` |
| `+ base (65)` | Restore ASCII range | `68` |
| `chr(68)` | Final character | `'D'` |

Decryption is the mirror: subtract the shift instead of adding.

---

##  Project Structure

```
caesar-cipher/
│
├── cipher.py       # main script with encrypt/decrypt functions
└── README.md       # project documentation
```

---

##  Limitations

The Caesar Cipher is **not secure** for real-world use. It has only 25 possible keys, making it trivially breakable by brute force. It also preserves letter frequency patterns, leaving it vulnerable to frequency analysis. It is used here as an educational exercise to understand the fundamentals of symmetric encryption.

---

##  Concepts Covered

- Symmetric encryption (same key encrypts and decrypts)
- ASCII / `ord()` and `chr()` functions in Python
- Modular arithmetic for alphabet wrapping
- IPO model (Input → Process → Output) in cryptographic systems

---

##  Part of DecodeLabs Cybersecurity Training

> **Project 2 — Cryptographic Phase: Basic Encryption & Decryption**  
> Batch 2026 | Powered by DecodeLabs  
> [www.decodelabs.tech](https://www.decodelabs.tech)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
