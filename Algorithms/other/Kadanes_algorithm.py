"""
Purpose of the Kadane's Algorithm is to the find the sum of the maximum 
contigous subarray of an array. Ex: [-2,1,-3,4,-1,2,1,-5,4] has [4,-1,2,1]
with the largest sum = 6

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
#   2020-03-08 Initial programming

"""


def kadane_algorithm(array):
    max_current, max_global = array[0], array[0]

    for val in array[1:]:
        max_current = max(val, max_current + val)

        if max_current > max_global:
            max_global = max_current

    return max_global


print(kadane_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
