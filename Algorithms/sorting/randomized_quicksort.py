'''
Purpose is to sort a list. The reason why randomizing is better is that on average, regardless on the input
randomized quicksort will have a running time of O(n*logn). This is regardless of the ordering of the inputted list.
This is in constrast to first pivot, median pivot, etc Quicksort.

Programmed by Aladdin Persson <Aladdin.persson at hotmail dot com>
*   2019-03-08 Initial programming

'''

import random

def quicksort_randomized(L):
    if len(L) <= 1:
        return L

    # Randomly choose a pivot idx
    pivot_idx = random.randint(0, len(L)-1)
    pivot = L[pivot_idx]

    # Swap pivot_idx to the first position
    L[0], L[pivot_idx] = L[pivot_idx], L[0]

    i = 0
    # range(1, len(L)) because we the pivot element is the first element
    for j in range(1, len(L)):
        if L[j] < pivot:
            L[j], L[i+1] = L[i+1], L[j]
            i += 1

    L[0], L[i] = L[i], L[0]

    left = quicksort_randomized(L[:i])
    right = quicksort_randomized(L[i + 1:])
    left.append(L[i])

    result = left + right

    return result

if __name__ == '__main__':
    l = [6,7,3,4,5,1,3,7,123]
    sorted_l = quicksort_randomized(l)
    print(sorted_l)