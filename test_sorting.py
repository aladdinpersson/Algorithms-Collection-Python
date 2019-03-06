# Import folder where sorting algorithms
import sys
sys.path.append('../../Algorithms/sorting')

# from bubblesort import bubblesort

from bubblesort import bubblesort

L1 = [1,2,3,4,5,6,7,8,9]
L1_sorted = sorted(L1)

L2 = [9,8,7,6,5,4,3,2,1]
L2_sorted = sorted(L2)

L3 = [1,1,1,1,1,1,1,1,1]
L3_sorted = sorted(L3)

L4 = [6,7,3,5,1,3]
L4_sorted = sorted(L4)

L5 = []
L5_sorted = []


# Bubblesort
def test_bubblesort():
    assert bubblesort(L1) == L1_sorted, "Not correctly sorted"
    assert bubblesort(L4) == L4_sorted, "Not correctly sorted"
    assert bubblesort(L4) == L4_sorted, "Not correctly sorted"
    assert bubblesort(L4) == L4_sorted, "Not correctly sorted"
    assert bubblesort(L4) == L4_sorted, "Not correctly sorted"

# Selectionsort
# assert sorted(L4) == L4_sorted, "Not correctly sorted"
# assert sorted(L4) == L4_sorted, "Not correctly sorted"
# assert sorted(L4) == L4_sorted, "Not correctly sorted"
# assert sorted(L4) == L4_sorted, "Not correctly sorted"
# assert sorted(L4) == L4_sorted, "Not correctly sorted"

# Heapsort

# Quicksort

# Mergesort

if __name__ == '__main__':
    pass
    #run_tests()
    #print("All tests OK!")