def main():
    msg = input("Enter plaintext: ").upper()
    key = input("Enter key: ").upper()
    new_key = key


    if len(key) != len(msg):
        new_key = (key * (len(msg)//len(key) + 1))[:len(msg)]

    ct = encrypt(msg, new_key)
    pt = encrypt(ct, new_key)
    print(ct)
    print(pt)


def encrypt(msg, key):
    result = ""
    for i in range(len(msg)):
        res = (ord(msg[i]) - ord("A"))  ^ (ord(key[i])-ord("A"))
        if res > 25:
            res %= 26
        result += chr(res + ord("A"))
    return result




if __name__ == "__main__":
    main()