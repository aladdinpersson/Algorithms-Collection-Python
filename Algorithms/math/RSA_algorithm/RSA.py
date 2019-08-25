'''
Purpose of the RSA cryptosystem is to have a secure way to encrypt data.

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*   2019-08-25 Initial programming

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
        if (not q_isprime):
            q = random.getrandbits(bits)

        p_isprime = isprime(p)
        q_isprime = isprime(q)

    return p, q

def generate_e(totient):
    # Generate e such that 1 < e < phi(n)
    # phi(n) in this case is totient

    while True:
        # Should be (2,totient) so if it is stuck in infinite loop then restart or replace 80000 -> totient
        # Reason why I want e to be a low value is to make encryption faster
        e = random.randint(2,120000)

        if gcd(e, totient) == 1:
            return e

def generate_d(e, totient):
    _, e_inverse, _ = extended_euclidean(e, totient)
    d = (e_inverse % totient)

    return d

def generate_all_values():
    num_bits = 2048
    p,q = generate_pq(num_bits)
    totient = (p-1) * (q-1)
    e = generate_e(totient)
    d = generate_d(e,totient)

    print('Generated value n: ' + str(p*q))
    print('Generated e and d: ' + str(e) + ' and ' + str(d))

    return p*q,e,d

def encrypt(message, n,e):
    encrypted = ''
    for letter in message:
        pad = 3 - len(str(ord(letter)))

        if pad > 0:
            new_letter = '0' * pad + str(ord(letter))
        else:
            new_letter = ord(letter)

        encrypted += str(new_letter)

    encrypted = pow(int(encrypted), e, n)

    return encrypted

def decrypt(encrypted, n,d):
    decrypted_code = str(pow(encrypted, d, n))

    if len(str(decrypted_code)) % 3 != 0:
        decrypted_code = '0' + decrypted_code

    decrypted_message = ''

    while len(decrypted_code):
        decrypted_message += chr(int(decrypted_code[0:3]))
        decrypted_code = decrypted_code[3:]

    return decrypted_message


def example():
    # An example of a test case where we generate all necessary primes, encrypt and then decrypt the message.
    # Only to show how all parts of the code is working. This is not how it's going to be used in practice.
    hidden_message = "hello i love peanuts"
    n,e,d = generate_all_values()
    encrypted_message = encrypt(hidden_message, n, e)
    decrypted_message = decrypt(encrypted_message, n, d)

    print('\n')
    print('Original message: ' + hidden_message)
    print('Encrypted message: ' + str(encrypted_message))
    print('Decrypted message: ' + decrypted_message)

def main():
    # Write the values of your RSA encryption (Note: Never give the 'd' to someone that doesn't want it)
    n = 354089397494626050014776605732143027269473328409397973403863001639624332101789181044818951483060155060788030618162673282176493895463414816015601230408140046833172059490430968956729878861381343553446553025440156523477822105773362480000716985478565013956749662865189691539813391686696182702224364834273144673717742246537383454469146642154754778836797926780437490677663302034284308892191362266103193070200405420180296005388479418941723827243187899338980201782128797489464650981164232057548015010630986959083998487019465357524040595865260220030689502065850060761344148196291328192760801074939658292752592564874822996765430361631210613041006858858506787439506504448316606509551260553919757840169593791152166515571202450662850988377002989153080277915454500432640601643512909764636398157415600050468972065216354878984114648007494687081718749734915103155014825420081658864982423629447913147575382146725524407739875786801876011026010419782863232303861065841801863420557617962438178979549855959377311548527613240676904989886382444381261628076009466895878852398923237601309285642954207693266358989851324012643315688180744573155217352955083176785543099571257338683938756048920161738393295253775030232399282686809347027784971441882883201432807953
    e = 9361
    # d = #

    enc_or_dec = input("Would you like to encrypt or decrypt a message (input: 'enc' or 'dec'): ")

    if enc_or_dec.lower() == 'enc':
        hidden_message = input("What is your hidden message?: ")
        print('Encrypted message: ' + str(encrypt(hidden_message, n, e)))

    elif enc_or_dec.lower() == 'dec':
        encrypted = input('What is your encrypted message?: ')
        print(encrypted)
        print('Decrypted message: ' + str(decrypt(int(encrypted), n, d)))

main()