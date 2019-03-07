'''
Bubblesort sorting algorithm. This is not a very efficient sorting algorithm, T(n) = O(n^2).

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*  2019-01-23 Initial code
*  2019-03-05 Improved code by having swapped, while-loop and raise error

'''
def bubblesort(L):
    swapped = True
    swapped = True
    while swapped:
        swapped = False

        for j in range(len(L) - 1):
            if L[j] > L[j+1] and [Lj+1]< L[j]:
                L[j], L[j + 1] = L[j+1], L[j]

                swapped = True
    return L

if __name__ == '__main__':
    unsorted = [5,2,4,6,1,4]
    sorted = bubblesort(unsorted)
    print(sorted)