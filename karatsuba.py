# Purpose is to implement karatsuba multiplication, a way of computing
# x * y which is faster than the normal method taught which has a time complexity of O(n^2) which
# is very slow. This method produces a way which is much faster approx. O(n^(1.59))

# import random to check if implementation is correct
import random

def karatsuba(x,y):
    # handle negative numbers multiplication
    if x < 0:
        return -1 * karatsuba(-x,y)
    if y < 0:
        return -1 * karatsuba(x,-y)

    # Base case (two numbers from 1-9 multiplication)
    if len(str(x)) == 1 or len(str(y)) == 1:
        return (x*y)

    n = max(len(str(x)), len(str(y))) // 2

    # split about middle (can be done in multiple ways, found on github, thought was rly clever)
    a = x // 10**n
    b = x % 10**n
    c = y // 10**n
    d = y % 10**n

    # Compute the terms using recursion
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba(a+b,c+d) - ac - bd

    # calculate x * y
    product = ac * (10**(2*n)) + ad_bc * (10**n) + bd

    # return x * y
    return product

# Following checks if implementation is correct
# if __name__ == '__main__':
#     for _ in range(100000):
#         a = random.randint(-100000, 100000)
#         b = random.randint(-100000, 100000)
#         karatsuba_result = karatsuba(a, b)
#         correct_result = a * b
#
#         if karatsuba_result != correct_result:
#             print('mismatch for %s and %s' % (a, b))
#             print(f'Correct result was {correct_result}')
#             print(f'Karatsuba method got it to {karatsuba_result}')
#             break


# For Programming Assignment 1
if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    print(karatsuba(x,y))
    print(x*y)
