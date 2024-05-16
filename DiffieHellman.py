def main():

    p = int(input("Enter p: "))
    g = int(input("Enter g: "))
    
    if (isPrime(p) and isPrimitive(g,p)):
        #if a < p and b < p then do following
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        
        xa, xb = pow(g,a,p), pow(g,b,p)
        ak,bk = pow(xb,a,p), pow(xa,b,p)

        print(f"\nSecret Key For User 1 Is {ak}\nSecret Key For User 2 Is {bk}\n")
        print("Keys Have Been Exchanged Successfully") if ak == bk else print("Keys Have Not Been Exchanged Successfully")




def isPrime(p):
    if p <= 1:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True


def isPrimitive(g,p):
    lis = [pow(g,i,p) for i in range(p-1)]
    for i in lis: 
        if lis.count(i) > 1:
            return False
    return True



if __name__ == "__main__":
    main()