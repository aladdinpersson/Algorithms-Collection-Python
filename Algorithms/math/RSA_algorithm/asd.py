'''
Purpose of the RSA cryptosystem is to have a secure way to encrypt data.

Time complexity:



'''

from math import gcd
from sympy import isprime
import random

from euclid_gcd import extended_euclidean

def generate_pq(bits):
    p = random.getrandbits(bits)
    q = random.getrandbits(bits)
    p_isprime = isprime(p)
    q_isprime = isprime(q)

    while (not (p_isprime and q_isprime)):
        if (not p_isprime):
            p = random.getrandbits(bits)
            p_isprime = isprime(p)

        if (not q_isprime):
            q = random.getrandbits(bits)
            q_isprime = isprime(q)



    return p,q

def generate_e(totient):
    # Generate e such that 1 < e < phi(n)
    # phi(n) in this case is totient

    while True:
        e = random.randrange(2, totient)

        if gcd(e, totient) == 1:
            return e



if __name__ == '__main__':
    # num_bits = 52 # we want to generate p,q so that they are larger than 2**52 but smaller than 2**53
    # p,q = generate_pq(num_bits)
    p = 61
    q = 53
    totient = (p-1)*(q-1)
    print(totient)
    e = generate_e(totient)
    print(e)

    _, ok, ok2 = extended_euclidean(p,q)



