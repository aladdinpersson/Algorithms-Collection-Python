'''
Selection sort algorithm. T(n) = O(n^2)

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*    2019-03-05 Initial coding

'''

# Selection sort that creates a copy. More "intuitive" but requires extra memory.
def selectionsort_intuitive(L):
    correctly_sorted = []

    while L:
        min = L[0]

        for element in L:
            min=element if element < min else min

        correctly_sorted.append(min)
        L.remove(min)

    return correctly_sorted


def selectionsort(L):
    for i in range(len(L)-1):
        min_index = i

        # Look through entire list, look which is the smallest element
        for j in range(i+1, len(L)):
            if L[j] < L[min_index]:
                min_index = j

        # If the smallest isn't the index itself, then swap
        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]

    return L

if __name__ == '__main__':
    unsorted = [10000,2,7,4,1,5,3,15,13,169]
    sorted = selectionsort_intuitive(unsorted)
    print(sorted)