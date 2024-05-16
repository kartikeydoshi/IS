##p,q two primes
#n = pq
# phi
#e should be such that gcd(e,phi) == 1 and 1 < e < phi
# d = e^-1 mod phi
#public e,n priv d,n
import random


def main():
    p = int(input("Enter prime number: "))
    q = int(input("Enter prime number q: "))

    pubKey, privKey = generateKey(p, q)

    msg = input("Enter message: ")

    encrypted = encrypt(msg, pubKey)
    decrypted = decrypt(encrypted, privKey)
    print(pubKey)
    print(privKey)
    print(encrypted)
    print(decrypted)

def encrypt(msg, pubKey):
    e, n =pubKey
    res = [pow(ord(char), e,n) for char in msg]
    return res

def decrypt(msg, privKey):
    d, n = privKey
    res = [chr(pow(char, d, n)) for char in msg]
    return "".join(res)


def generateKey(p,q):
    n = p * q
    phi = (p-1) * (q-1)
    
    e = random.randint(2,phi)
    while gcd(e, phi)!=1:
        e = random.randint(2,phi)
    
    d = pow(e,-1,phi)

    return (e,n), (d,n)
    

def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a


if __name__ == "__main__":
    main()