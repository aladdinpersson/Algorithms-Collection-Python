# Insertion sort sorting algorithm O(n^2). Worse case scenario is when
# all elements are sorted in decreasing order.
# Programmed by Dino Persson 2019-01-23 <aladdin.persson at hotmail dot com>

import random

def insertionsort(L):
    # loop through all except first element in list
    for j in range(1,len(L)):
        key = L[j]

        i = j - 1

        # inserts the key into the correct place
        while i >= 0 and L[i] > key:
            L[i+1] = L[i]
            i -= 1
        L[i+1] = key

    return L
