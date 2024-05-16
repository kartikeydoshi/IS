def encrypt(plaintext, mat):
    cipher = ""
    for i in range(0,len(plaintext),2):
        row1, col1 = find(plaintext[i], mat)
        row2, col2 = find(plaintext[i+1],mat)

        if row1 == row2:
            cipher += mat[row1][(col1 + 1)%5]
            cipher += mat[row1][(col2 + 1)%5]
        
        elif col1 == col2:
            cipher += mat[(row1 + 1)%5][col1]
            cipher += mat[(row2 + 1)%5][col2]
        else:
            cipher += mat[row1][col2]
            cipher += mat[row2][col1]
    return cipher
            




def find(char, mat):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == char:
                return i,j
            



def clean(plaintext):
    plaintext = plaintext.replace("J","I")
    clean = ""

    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            clean += plaintext[i] + 'X'
            i += 1
        elif plaintext[i] == plaintext[i+1]:
            clean += plaintext[i] + 'X'
            i += 1
        else:
            clean += plaintext[i] + plaintext[i+1]
            i += 2

    return clean
            

def generateMatrix(key):
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    key = "".join(dict.fromkeys(key.replace("J","I")))

    for i in key:
        if i not in matrix:
            matrix.append(i)

    for char in alpha:
        if char not in matrix:
            matrix.append(char)

    matrix = [matrix[i * 5:(i+1)*5] for i in range(5)]
    print(matrix)

    return matrix



def main():
    key = "MONARCHY"
    plaintext = "INSTRUMENTS"

    mat = generateMatrix(key)
    plaintext = clean(plaintext)

    ct = encrypt(plaintext, mat)
    print(ct)

main()


