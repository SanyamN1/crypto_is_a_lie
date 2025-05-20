def analyze_and_brute(ciphertext):
    output = ["🔍 XOR Cipher Brute Force (1-byte keys):"]
    try:
        bytes_data = bytes.fromhex(ciphertext)
    except:
        try:
            bytes_data = ciphertext.encode()
        except:
            return ""

    for key in range(256):
        result = ''.join(chr(b ^ key) if 32 <= (b ^ key) <= 126 else '.' for b in bytes_data)
        output.append(f"Key {key:02X}: {result}")
    return "\n".join(output)
