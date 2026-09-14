# Project 3 — Random Password Generator
**DecodeLabs Industrial Training Kit — Batch 2026**

## What it does
Asks the user for a password length and generates a random, secure password made of letters and numbers (optionally symbols too).

## How to run
```bash
python3 password_generator.py
```
You'll be asked for:
1. Password length (8–64, 15+ recommended)
2. Whether to include special symbols (y/N)

## Why it's built this way
| Requirement | What was used | Why |
|---|---|---|
| Randomness | `secrets.choice()` | `random` uses the Mersenne Twister, which is predictable and unsafe for passwords. `secrets` pulls from the OS's cryptographically secure entropy source. |
| Character sets | `string.ascii_letters`, `string.digits`, `string.punctuation` | Avoids manually typing character arrays; consistent and less error-prone. |
| Building the string | List + `''.join()` | Strings are immutable in Python, so `password += char` in a loop creates a new string object every iteration (O(n²)). `.join()` allocates memory once (O(n)). |
| Input validation | Loop with `try/except` + range checks | Prevents crashes on bad input and blocks unreasonably short/long passwords. |
| Length guidance | NIST SP 800-63-4 (2024) | Recommends 15+ characters for high-security contexts, and up to 64 to support passphrases. |

## Example output
```
=== DecodeLabs Project 3: Random Password Generator ===

Enter the desired password length (8-64, 15+ recommended): 16
Include special symbols too? (y/N): n

Your generated password:
70oFm2YrTXg0H5TS

Estimated entropy: 95.3 bits
This is a very strong password.
```

## Files
- `password_generator.py` — main script
- `README.md` — this file
