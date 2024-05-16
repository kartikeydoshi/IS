def generate_playfair_square(key):
    # Remove duplicates from the key and create the 5x5 matrix
    key = "".join(dict.fromkeys(key.replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    # Split matrix into a 5x5 array
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def prepare_text(text):
    # Convert to uppercase, replace J with I, and split into digraphs
    text = text.upper().replace("J", "I")
    prepared = ""
    
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared += text[i] + 'X'
            i += 1
        elif text[i] == text[i + 1]:
            prepared += text[i] + 'X'
            i += 1
        else:
            prepared += text[i] + text[i + 1]
            i += 2

    return prepared

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_square(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        row1, col1 = find_position(plaintext[i], matrix)
        row2, col2 = find_position(plaintext[i + 1], matrix)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_square(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        row1, col1 = find_position(ciphertext[i], matrix)
        row2, col2 = find_position(ciphertext[i + 1], matrix)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext

# Example usage
key = "MONARCHY"
plaintext = "INSTRUMENTS"
ciphertext = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(ciphertext, key)

print(f"Key: {key}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
