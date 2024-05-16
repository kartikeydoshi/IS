def main():
    msg = input("Enter message: ").upper()
    key = input("Enter key: ").upper()
    new_key = key

    if len(key) != len(msg):
        new_key = (key * (len(msg)//len(key) + 1))[:len(msg)]
    
    ct = encrypt(msg, new_key)
    pt = decrypt(ct, new_key)
    print(ct)
    print(pt)


def encrypt(msg, key):
    result = ""
    for i in range(len(msg)):
        result += chr((ord(msg[i]) + ord(key[i]))%26 + ord('A'))
    return result

def decrypt(msg, key):
    result = ""
    for i in range(len(msg)):
        result += chr((ord(msg[i]) - ord(key[i]))%26 + ord('A'))
    return result





if __name__ == "__main__":
    main()