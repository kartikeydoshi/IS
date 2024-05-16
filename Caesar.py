def main():
    plaintext = input("Enter message: ")
    shift = int(input("Enter shift: "))

    ciphertext = encrypt(plaintext, shift)
    og = decrypt(ciphertext, shift)

    print("Plaintext\tshift\tciphertext\toriginaltext")
    print(f"{plaintext}\t{shift}\t{ciphertext}\t{og}")
    


def encrypt(pt, k) :
    result  = ""
    for char in pt:
        base = ord("A") if char.isupper() else ord("a")
        result += chr((ord(char) - base + k)%26 + base)
    return result

def decrypt(ct, k):
    result = ""
    for char in ct:
        base = ord("A") if char.isupper() else ord("a")
        result += chr((ord(char) - base - k)%26 + base)
    return result


if __name__ == "__main__":
    main()