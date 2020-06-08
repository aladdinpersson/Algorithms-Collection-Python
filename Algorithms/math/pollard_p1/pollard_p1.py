"""
Purpose is given a number write it only as a factorization of primes.

Time complexity:

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*   2019-08-22 Initial programming

"""

from math import gcd


def pollard_p1(n):
    r = 2

    for i in range(2, 100):
        r = r ** i % n

        if gcd(r - 1, n) != 1:
            print("One factor found was: " + str(gcd(r - 1, n)))
            print("Number of iterations was: " + str(i))
            return gcd(r - 1, n)

    print("No factorization was found")


if __name__ == "__main__":
    pollard_p1(703425623)
