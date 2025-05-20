def caesar_decrypt(cipher, key):
    result = ''
    for char in cipher:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset - key) % 26 + offset)
        else:
            result += char
    return result

def atbash(cipher):
    result = ''
    for char in cipher:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr(25 - (ord(char) - offset) + offset)
        else:
            result += char
    return result

def analyze_and_brute(text):
    output = ["🔍 Classical Cipher Results (Caesar, ROT13, Atbash):"]
    for key in range(1, 26):
        output.append(f"Caesar (key={key}): {caesar_decrypt(text, key)}")
    output.append(f"ROT13: {caesar_decrypt(text, 13)}")
    output.append(f"Atbash: {atbash(text)}")
    return "\n".join(output)
