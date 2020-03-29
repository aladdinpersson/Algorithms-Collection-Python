# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/sorting')

# If run from local:
# sys.path.append('../../Algorithms/sorting')

from bubblesort import bubblesort
from insertionsort import insertionsort
from mergesort import merge_sort, merge
from quicksort import quicksort_firstpivot, quicksort_lastpivot
from randomized_quicksort import quicksort_randomized
from selectionsort import selectionsort

# Test cases we wish to run
L1 = [1,2,3,4,5,6,7,8,9]
L1_sorted = [1,2,3,4,5,6,7,8,9]

L2 = [9,8,7,6,5,4,3,2,1]
L2_sorted = [1,2,3,4,5,6,7,8,9]

L3 = [1,1,1,1,1,1,1,1,1]
L3_sorted = [1,1,1,1,1,1,1,1,1]

L4 = [6,7,3,5,1,3]
L4_sorted = [1,3,3,5,6,7]

L5 = []
L5_sorted = []

L6 = [-1,-2,-3]
L6_sorted = [-3,-2,-1]

L7 = [-5,-7,-1,-3,-4]
L7_sorted = [-7,-5,-4,-3,-1]

class test_sorting(unittest.TestCase):

    def test_bubblesort(self):
        self.assertEqual(bubblesort(L1), L1_sorted)
        self.assertEqual(bubblesort(L2), L2_sorted)
        self.assertEqual(bubblesort(L3), L3_sorted)
        self.assertEqual(bubblesort(L4), L4_sorted)
        self.assertEqual(bubblesort(L5), L5_sorted)
        self.assertEqual(bubblesort(L6), L6_sorted)
        self.assertEqual(bubblesort(L7), L7_sorted)
        self.assertEqual(bubblesort(L7), L7_sorted)

    def test_insertionsort(self):
        self.assertEqual(insertionsort(L1), L1_sorted)
        self.assertEqual(insertionsort(L2), L2_sorted)
        self.assertEqual(insertionsort(L3), L3_sorted)
        self.assertEqual(insertionsort(L4), L4_sorted)
        self.assertEqual(insertionsort(L5), L5_sorted)
        self.assertEqual(insertionsort(L6), L6_sorted)
        self.assertEqual(insertionsort(L7), L7_sorted)

    def test_mergesort(self):
        self.assertEqual(merge_sort(L1), L1_sorted)
        self.assertEqual(merge_sort(L2), L2_sorted)
        self.assertEqual(merge_sort(L3), L3_sorted)
        self.assertEqual(merge_sort(L4), L4_sorted)
        self.assertEqual(merge_sort(L5), L5_sorted)
        self.assertEqual(merge_sort(L6), L6_sorted)
        self.assertEqual(merge_sort(L7), L7_sorted)

    def test_quicksort(self):
        self.assertEqual(quicksort_firstpivot(L1), L1_sorted)
        self.assertEqual(quicksort_firstpivot(L2), L2_sorted)
        self.assertEqual(quicksort_firstpivot(L3), L3_sorted)
        self.assertEqual(quicksort_firstpivot(L4), L4_sorted)
        self.assertEqual(quicksort_firstpivot(L5), L5_sorted)
        self.assertEqual(quicksort_firstpivot(L6), L6_sorted)
        self.assertEqual(quicksort_firstpivot(L7), L7_sorted)

        self.assertEqual(quicksort_lastpivot(L1), L1_sorted)
        self.assertEqual(quicksort_lastpivot(L2), L2_sorted)
        self.assertEqual(quicksort_lastpivot(L3), L3_sorted)
        self.assertEqual(quicksort_lastpivot(L4), L4_sorted)
        self.assertEqual(quicksort_lastpivot(L5), L5_sorted)
        self.assertEqual(quicksort_lastpivot(L6), L6_sorted)
        self.assertEqual(quicksort_lastpivot(L7), L7_sorted)



    def test_selectionsort(self):
        self.assertEqual(selectionsort(L1), L1_sorted)
        self.assertEqual(selectionsort(L2), L2_sorted)
        self.assertEqual(selectionsort(L3), L3_sorted)
        self.assertEqual(selectionsort(L4), L4_sorted)
        self.assertEqual(selectionsort(L5), L5_sorted)
        self.assertEqual(selectionsort(L6), L6_sorted)
        self.assertEqual(selectionsort(L7), L7_sorted)

    def test_quicksort_randomized(self):
        self.assertEqual(quicksort_randomized(L1), L1_sorted)
        self.assertEqual(quicksort_randomized(L2), L2_sorted)
        self.assertEqual(quicksort_randomized(L3), L3_sorted)
        self.assertEqual(quicksort_randomized(L4), L4_sorted)
        self.assertEqual(quicksort_randomized(L5), L5_sorted)
        self.assertEqual(quicksort_randomized(L6), L6_sorted)
        self.assertEqual(quicksort_randomized(L7), L7_sorted)


if __name__ == '__main__':
    print("Running sorting tests:")
    unittest.main()