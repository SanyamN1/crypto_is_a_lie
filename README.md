# crypto_is_a_lie

> A plug-and-play crypto reconnaissance tool for CTF players, hackers, and curious cryptomancers. Built for speed, depth, and versatility.

`crypto_is_a_lie` is your ultimate Swiss Army knife for cracking, analyzing, and understanding encoded/encrypted strings during CTF challenges or malware analysis. It supports automated detection, brute-forcing, decoding, and modular extension of common cryptographic/obfuscation methods — because no flag deserves to hide in Base58 forever.

---

## ⚙️ Features

- 🔍 **Auto-detection** of common encodings and ciphers
- 🧠 **Brute-force decoding** for:
  - Caesar / ROT / Shift Ciphers
  - Vigenère (wordlist-based)
  - XOR (single/multi-byte)
  - Base64/Base32/Base58/Base85
  - Hex, URL, Binary, Morse, Bacon
  - Rail Fence, Atbash, Affine, and more
- 🧩 **Modular Design** — Add new analyzers in seconds
- 📦 File-based input/output support
- 📊 Verbose and silent modes (ideal for automation)
- 🛠️ Optimized for Capture the Flag, red-teaming, and OSINT workflows

---

## 🧪 Sample Usage

```bash
$ python3 crypto_analyzer.py -i input.txt
OR
$ python3 crypto_analyzer.py -s "Uryyb Jbeyq!"
OR with brute force
$ python3 crypto_analyzer.py -s "Uryyb Jbeyq!" --brute
Analyze everything, dump results to a file:
$ python3 crypto_analyzer.py -i input.txt -o results.txt --all

