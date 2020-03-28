'''
Purpose of this is to find a target element in an already sorted list L.
We use the fact that it is already sorted and get a O(log(n)) search algorithm.

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
#   2019-03-12 Initial programming

'''


def binarysearch_iterative(L, target):
    low = 0
    high = len(L) - 1

    while low <= high:
        middle = (low+high)//2

        if target == L[middle]:
            return True, middle

        elif target < L[middle]:
            high = middle - 1

        else:
            low = middle + 1

    return False, None

def binarysearch_recursive(L, target, low, high):
    middle = (low+high)//2

    if low > high:
        return False, None

    elif target == L[middle]:
        return True, middle

    elif target < L[middle]:
        return binarysearch_recursive(L, target, low, middle-1)

    else:
        return binarysearch_recursive(L, target, middle+1, high)



if __name__ == '__main__':
    target = 1
    sorted_array = [1,1,1,1,1,1,1,1]

    exists, idx = binarysearch_iterative(sorted_array, target)
    print(f'The target {target} exists in array: {exists}. The idx of it is: {idx}')

    exists, idx = binarysearch_recursive(sorted_array, target, 0, len(sorted_array)-1)
    print(f'The target {target} exists in array: {exists}. The idx of it is: {idx}')

