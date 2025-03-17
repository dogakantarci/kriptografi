import rsa 
import random
from sympy import primitive_root

def diffie_hellman():
    p = rsa.create_prime()
    g = primitive_root(p)
    a = random.randint(100000, 1000000)
    b = random.randint(100000, 1000000)
    print(p, g, a, b)
    A = pow(g, a, p)
    B = pow(g, b, p)

    key_alice = pow(A, b, p)
    key_bob = pow(B, a ,p)
    print(key_alice, key_bob)
    return(key_alice, key_bob)
diffie_hellman()