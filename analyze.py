from modules import base_encodings, classical_ciphers, xor_cipher, bacon_morse, railfence_vigenere
from utils import write_output

def full_analysis(text):
    results = []

    results.append(base_encodings.analyze_and_decode(text))
    results.append(classical_ciphers.analyze_and_brute(text))
    results.append(xor_cipher.analyze_and_brute(text))
    results.append(bacon_morse.analyze_and_decode(text))
    results.append(railfence_vigenere.analyze_and_brute(text))

    write_output("decryption_attempts.txt", results)

if __name__ == "__main__":
    ciphertext = input("🔐 Enter suspected encrypted text: ").strip()
    full_analysis(ciphertext)
    print("✅ Decryption attempts saved to 'decryption_attempts.txt'")
