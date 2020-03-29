'''
Purpose is given a number write it only as a factorization of primes.

Time complexity: O(sqrt(n)) PSEUDO-POLYNOMIAL, actually exponential!

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*   2019-03-18 Initial programming
*   2019-08-19 Noticed a bug when using. Should be correct now, but I need to implement
               more robust tests to be certain that this is a correct implementation.

'''

def primefactorization(n):
    original_value = n
    values = []

    for i in range(2, int(n**0.5) + 1):
        # Will not pass this if statement if i is not a prime number.
        # (This is because all numbers have a prime factorization)
        if n % i == 0:

            while n % i == 0:
                n /= i
                values.append(i)

    if len(values) != 0:
        values.append(int(n)) # if we have found one factor <= sqrt(n), then there will be another factor.
        print(f'Prime factorization of {original_value} is: {values}')
    else:
        print(f'There is no prime factorization because the number {original_value} is a prime')

if __name__ == '__main__':
    #primefactorization(2**2**6 + 1)
    primefactorization(123)