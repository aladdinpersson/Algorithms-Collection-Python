# Bubblesort sorting algorithm. This is not a very efficient sorting algorithm, T(n) = O(n^2).

# Programmed by Aladdin Persson 2019-01-23 <aladdin.persson at hotmail dot com>

def bubblesort(L):
    n = len(L) - 1

    for i in range(n):
        for j in range(n - i):
            if L[j] > L[j+1]:
                L[j], L[j + 1] = L[j+1], L[j]

    return L