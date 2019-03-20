'''


'''

import sys
sys.setrecursionlimit(100000)

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)

    else:
        gcd, x, y =  extended_euclidean(b % a, a)
        return (gcd, y - (b//a) * x, x)

if __name__ == '__main__':
    print(extended_euclidean(2, 5))
    print(extended_euclidean(56, 15))

