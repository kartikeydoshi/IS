def encrypt_columnar_transposition(plaintext, key):
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    
    # Create the grid for the plaintext
    num_columns = len(key)
    num_rows = len(plaintext) // num_columns + (1 if len(plaintext) % num_columns != 0 else 0)
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    # Fill the grid with the plaintext characters row-wise
    index = 0
    for row in range(num_rows):
        for col in range(num_columns):
            if index < len(plaintext):
                grid[row][col] = plaintext[index]
                index += 1
    
    # Sort the columns based on the alphabetical order of the key
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    # Generate the ciphertext by reading the columns in sorted order
    ciphertext = ''
    for index, _ in key_order:
        for row in range(num_rows):
            if grid[row][index]:
                ciphertext += grid[row][index]
    
    return ciphertext


def decrypt_columnar_transposition(ciphertext, key):
    # Determine the number of columns and rows
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns + (1 if len(ciphertext) % num_columns != 0 else 0)
    
    # Sort the columns based on the alphabetical order of the key
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    # Create an empty grid to fill the characters column-wise
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    # Fill the grid with the ciphertext characters column-wise
    index = 0
    for i, _ in key_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                grid[row][i] = ciphertext[index]
                index += 1
    
    # Read the plaintext row-wise, accounting for empty cells
    plaintext = ''
    for row in range(num_rows):
        for col in range(num_columns):
            if grid[row][col]:
                plaintext += grid[row][col]
            else:
                break  # Break loop when encountering an empty cell
    
    return plaintext


def main():
    plaintext = "HELLOWORLD"
    key = "KEY"
    
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    ciphertext = encrypt_columnar_transposition(plaintext, key)
    print(f"Encrypted: {ciphertext}")
    
    decrypted_text = decrypt_columnar_transposition(ciphertext, key)
    print(f"Decrypted: {decrypted_text}")

if __name__ == "__main__":
    main()

