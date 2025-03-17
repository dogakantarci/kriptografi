import random
import math

def miller_rabin(n):    # n-1'i 2**s * d olarak hesapla
    s, d = 0, n-1       # sonra d kalana kadar 2'ye bölüyoruz
    result = "NO!"      # 8 farklı rastgele a var, eğer a**d mod n (n-1) veya 1 değilse
                        # 2'nin kuvvetini 1 artırıyorum ve yeniden s'ye kadar deniyoruz
    while(d % 2 == 0):  # false dönerse sayı asal değildir
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
    p = create_prime() # 1. adım 2 tane asal sayı
    q = create_prime()
    #print(p,q)
    n = p * q # 2. adım onların çarpımları
    lambda_n = math.lcm(p-1, q-1) # 3. adım sayıların 1 eksiğinin ekoku
    while(True):
        e = random.randint(1, lambda_n) # e ile lambda_n aralarında asal olmalı
        if(math.gcd(e, lambda_n) == 1): # aralarında asallık kontrolü
            break

    d = pow(e, -1, lambda_n)  # e'nin mod lambda_n'ye göre tersini alıyoruz



    #print((n, e), (d, p, q, lambda_n)) # genel anahtarlar, özel anahtarlar
    return((n, e), (d, p, q, lambda_n)) 
 
rsa_key()

