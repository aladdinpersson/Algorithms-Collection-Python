# Bubblesort sorting algorithm. This is not a very efficient sorting algorithm, T(n) = O(n^2).
# Programmed by Dino Persson 2019-01-23 <aladdin.persson at hotmail dot com>

import random

def bubblesort(L):
    n = len(L) - 1

    for i in range(n):
        for j in range(n - i):
            if L[j] > L[j+1]:
                L[j], L[j + 1] = L[j+1], L[j]


    return L


# Test if implemented correctly comparing to Pythons built in sort function
for i in range(100):
    # Generate a random list
    L = random.sample(range(999999), i)
    L_sorted = bubblesort(L)
    correctly_sorted = sorted(L)
    if L_sorted != correctly_sorted:
        raise("This was not correctly sorted.")

# If error was not raised then it means they were all correctly sorted
print("All was correctly sorted.")