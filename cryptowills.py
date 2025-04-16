# Classical Ciphers in Python

import numpy as np

# Caesar Cipher
def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Atbash Cipher
def atbash_encrypt(text):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(base + (25 - (ord(char) - base)))
        else:
            result += char
    return result

# August Cipher (similar to Caesar but uses month number as shift)
def august_encrypt(text):
    month_shift = 8  # August is 8th month
    return caesar_encrypt(text, month_shift)

# Affine Cipher
def affine_encrypt(text, a, b):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - base) + b) % 26) + base)
        else:
            result += char
    return result

# Vigenere Cipher
def vigenere_encrypt(text, key):
    result = ''
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# Gronsfeld Cipher
def gronsfeld_encrypt(text, key):
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = int(key[key_index % len(key)])
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# Beaufort Cipher
def beaufort_encrypt(text, key):
    result = ''
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((base + (25 - (ord(char) - base - shift)) % 26))
            key_index += 1
        else:
            result += char
    return result

# Autoclave / Running Key Cipher
def autokey_encrypt(text, key):
    result = ''
    key = key + text
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].lower()) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# N-gram operations (example: bigram count)
def bigram_frequency(text):
    text = ''.join(filter(str.isalpha, text.lower()))
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    freq = {}
    for bg in bigrams:
        freq[bg] = freq.get(bg, 0) + 1
    return freq

# Hill Cipher (2x2 matrix)
def hill_encrypt(text, key_matrix):
    text = text.replace(" ", "").upper()
    if len(text) % 2 != 0:
        text += 'X'
    result = ''
    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - 65, ord(text[i+1]) - 65]
        res = np.dot(key_matrix, pair) % 26
        result += chr(res[0] + 65) + chr(res[1] + 65)
    return result

# Rail Fence Cipher
def rail_fence_encrypt(text, rails):
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    var = 1
    for i, char in enumerate(text):
        fence[rail][i] = char
        rail += var
        if rail == 0 or rail == rails - 1:
            var = -var
    return ''.join([''.join(row) for row in fence])

# Route Cipher (clockwise spiral in 2D grid)
def route_encrypt(text, rows, cols):
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    text += 'X' * ((rows * cols) - len(text))
    k = 0
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = text[k]
            k += 1

    result = ''
    top, left = 0, 0
    bottom, right = rows - 1, cols - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1): result += grid[top][j]
        top += 1
        for i in range(top, bottom + 1): result += grid[i][right]
        right -= 1
        for j in range(right, left - 1, -1): result += grid[bottom][j]
        bottom -= 1
        for i in range(bottom, top - 1, -1): result += grid[i][left]
        left += 1

    return result

# Myszkowski Cipher
def myszkowski_encrypt(text, key):
    order = sorted(list(set(key)), key=lambda x: (key.index(x), x))
    indices = [order.index(k) for k in key]
    columns = [[] for _ in range(len(key))]
    for i, char in enumerate(text):
        columns[i % len(key)].append(char)

    result = ''
    for val in sorted(set(indices)):
        for i in range(len(indices)):
            if indices[i] == val:
                result += ''.join(columns[i])
    return result

# Switch Case Interface
if __name__ == '__main__':
    print("Choose a cipher to encrypt:")
    print("1. Caesar\n2. Atbash\n3. August\n4. Affine\n5. Vigenere\n6. Gronsfeld\n7. Beaufort\n8. Autokey\n9. Bigram Frequency\n10. Hill\n11. Rail Fence\n12. Route\n13. Myszkowski")
    choice = int(input("Enter choice (1-13): "))
    text = input("Enter text: ")

    match choice:
        case 1:
            shift = int(input("Enter shift: "))
            print(caesar_encrypt(text, shift))
        case 2:
            print(atbash_encrypt(text))
        case 3:
            print(august_encrypt(text))
        case 4:
            a = int(input("Enter 'a' (must be coprime to 26): "))
            b = int(input("Enter 'b': "))
            print(affine_encrypt(text, a, b))
        case 5:
            key = input("Enter key: ")
            print(vigenere_encrypt(text, key))
        case 6:
            key = input("Enter numeric key: ")
            print(gronsfeld_encrypt(text, key))
        case 7:
            key = input("Enter key: ")
            print(beaufort_encrypt(text, key))
        case 8:
            key = input("Enter key: ")
            print(autokey_encrypt(text, key))
        case 9:
            print(bigram_frequency(text))
        case 10:
            key_matrix = [[int(x) for x in input("Enter 2x2 matrix row 1: ").split()],
                          [int(x) for x in input("Enter 2x2 matrix row 2: ").split()]]
            print(hill_encrypt(text, np.array(key_matrix)))
        case 11:
            rails = int(input("Enter number of rails: "))
            print(rail_fence_encrypt(text, rails))
        case 12:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            print(route_encrypt(text, rows, cols))
        case 13:
            key = input("Enter key: ")
            print(myszkowski_encrypt(text, key))
        case _:
            print("Invalid choice")
