from itertools import cycle

# Rail Fence Cipher (up to 10 rails)
def decrypt_rail_fence(cipher, num_rails):
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(num_rails)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(num_rails):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == num_rails-1:
            dir_down = False

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

# Vigenère
def decrypt_vigenere(cipher, key):
    decrypted = ''
    key = cycle(key)
    for c in cipher:
        k = next(key)
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            decrypted += chr((ord(c) - ord(k.lower()) + 26) % 26 + offset)
        else:
            decrypted += c
    return decrypted

def analyze_and_brute(cipher):
    output = ["🔍 Rail Fence (1-10 rails) & Vigenère (top words)"]
    for r in range(2, 11):
        output.append(f"Rail Fence ({r} rails): {decrypt_rail_fence(cipher, r)}")
    common_words = ['flag', 'key', 'ctf', 'crypto', 'hack', 'pass']
    for word in common_words:
        output.append(f"Vigenère (key='{word}'): {decrypt_vigenere(cipher, word)}")
    return "\n".join(output)
