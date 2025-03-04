import random

def miller_rabin():
    n = int(input("Sayı giriniz: "))
    s, d = 0, n-1
    result = ""
    
    while(d % 2 == 0):
        d //= 2
        s += 1
    print(n,n-1,s,d)

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
    print(result)




    



miller_rabin()