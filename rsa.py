import random
import math

def miller_rabin(n):
    s, d = 0, n-1
    result = "NO!"
    
    while(d % 2 == 0):
        d //= 2
        s += 1
    #print(n,n-1,s,d)

    for i in range(8):
        a = random.randint(2, n-2)

        if(a**d % n == 1):
            result = "ok"
        elif(a**d % n == n-1):
            result = "ok"
        else:
            result = "NO!"

        if(result == "NO!"):
            for i in range(s):
                if(a**(2**i * d) % n == n-1):
                    result = "ok"
                    break
    #print(n, result)
    if(result == "ok"):
        return True
    else:
        return False

def create_prime():
    p = random.randint(10000, 100000)
    while not(miller_rabin(p)):
        p =random.randint(10000, 100000)
    #print(p)
    return(p)
#create_prime()

def rsa_key():
    d = 0
    p = create_prime() # 1. adım
    q = create_prime()
    #print(p,q)
    n = p * q # 2. adım
    lambda_n = math.lcm(p-1, q-1) # 3. adım
    while(True):
        e = random.randint(1, lambda_n)
        if(math.gcd(e, lambda_n) == 1):
            break

    for i in range(1, lambda_n):  
        if (e * i) % lambda_n == 1:
            d = i
            break


    print((n, e), (d, p, q, lambda_n))
    return((n, e), (d, p, q, lambda_n))

rsa_key()