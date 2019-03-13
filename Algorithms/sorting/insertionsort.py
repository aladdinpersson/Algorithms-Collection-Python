'''
Insertion sort algorithm O(n^2).

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*    2019-01-23 Initial programming
*    2019-03-05 Made code cleaner
'''

def insertionsort(L):
    # loop through all except first element in list
    for index in range(1, len(L)):
        value = L[index]

        position = index - 1

        # inserts the key into the correct place
        while position >= 0 and L[position] > value:
            L[position+1] = L[position]
            position -= 1

        L[position + 1] = value

    return L


if __name__ == '__main__':
    unsorted = [7,2,4,1,5,3]
    sorted = insertionsort(unsorted)
    print(sorted)