'''
Purpose is given a number write it only as a factorization of primes.

Time complexity: O(sqrt(n))

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*   2019-03-18 Initial programming

'''

def primefactorization(n):
    original_value = n
    values = []

    for i in range(2, int(n**0.5) + 1):
        # Will not pass this if statement if i is not a prime number.
        # (This is because all numbers have a prime factorization)
        if n % i == 0:
            count = 0

            while n % i == 0:
                n /= i
                values.append(i)
                count += 1

    if n == 1:
        print(f'Prime factorization of {original_value} is: {values}')
    else:
        print(f'There is no prime factorization because the number {original_value} is a prime')

if __name__ == '__main__':
    primefactorization(17)
    primefactorization(1210000)
