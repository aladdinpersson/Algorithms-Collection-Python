# "Euclidean algorithm is one of the oldest algorithms in common use".
# The purpose is to find the greatest common divisor between two numbers a,b.

# Example: gcd(21, 7) = 7

# Programmed by Aladdin Persson
#   2019-02-19 Initial programming

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd_iterative(a,b):
    while b != 0:
        a, b = b, a%b

    return a