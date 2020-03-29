# Quicksort with pivot always using first index as pivot

def quicksort_firstpivot(L):
    if len(L) <= 1:
        return L

    pivot = L[0]

    i = 0

    for j in range(1, len(L)):
        if L[j] < pivot:
            L[j], L[i+1] = L[i+1], L[j]
            i += 1

    L[0], L[i] = L[i], L[0]

    left = quicksort_firstpivot(L[:i])
    right = quicksort_firstpivot(L[i+1:])
    left.append(L[i])
    result = left + right
    return result

# Quicksort with pivot always using last index as pivot
def quicksort_lastpivot(x):
    if len(x) <= 1:
        return x

    x[0], x[-1] = x[-1], x[0]
    pivot = x[0]

    i = 0

    for j in range(1, len(x)):
        if x[j] < pivot:
            x[j], x[i+1] = x[i+1], x[j]
            i += 1

    x[0], x[i] = x[i], x[0]

    left = quicksort_lastpivot(x[:i])
    right = quicksort_lastpivot(x[i+1:])
    left.append(x[i])

    result = left + right
    return result