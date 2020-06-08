"""
Purpose is given two sets A,B find the intersection of them. I know there must be more efficients ways than what I,
am doing here but havn't figured out how yet.

Complexity: O(nlog(n)) + O(mlog(m)) + O(n+m) = O(max(n*log(n), m*log(m))

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*   2019-03-13 Initial programming

"""


def intersection(A, B):
    # n = length of A, m = length of B
    # O(nlog(n) + mlog(n)) cost for sorting
    A = sorted(A)
    B = sorted(B)

    i, j = 0, 0

    AB_intersection = []

    # complexity O(n+m)
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1

        elif B[j] < A[i]:
            j += 1

        elif A[i] == B[j]:
            AB_intersection.append(A[i])
            i += 1
            j += 1

    return AB_intersection


if __name__ == "__main__":
    A = [1, 3, 5, 8, 12]
    B = [2, 3, 5, 10, 12]

    intersection_AB = intersection(A, B)
    print(intersection_AB)
