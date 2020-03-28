# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/other')

# If run from local:
#sys.path.append('../../Algorithms/other')

from binarysearch import binarysearch_iterative, binarysearch_recursive


class test_binarysearch(unittest.TestCase):

    def setUp(self):
        # test cases we wish to run
        self.L1 = [1, 3, 5, 8, 10, 12]
        self.L1_target = 5
        self.L1_correct = True, 2

        self.L2 = [1, 3, 5, 8, 10, 12]
        self.L2_target = 6
        self.L2_correct = False, None

        self.L3 = [1,1,1,1,1,1,1,1]
        self.L3_target = 1
        self.L3_correct = True, (0+len(self.L3)-1)//2

        self.L4 = [1, 3, 6, 11, 16, 21, 25, 27]
        self.L4_target = 27
        self.L4_correct = True, len(self.L4)-1

        self.L5 = [1, 3, 6, 11, 16, 21, 27]
        self.L5_target = 1
        self.L5_correct = True, 0

        self.L6 = []
        self.L6_target = 10
        self.L6_correct = False, None

        self.L7 = [11,12,15,19,23,41,173,298]
        self.L7_target = 12
        self.L7_correct = True, 1


    def test_binarysearch_basic(self):
        L1_result_iterative = binarysearch_iterative(self.L1, self.L1_target)
        L1_result_recursive = binarysearch_recursive(self.L1, self.L1_target, 0, len(self.L1)-1)

        self.assertEqual(L1_result_iterative, self.L1_correct)
        self.assertEqual(L1_result_recursive, self.L1_correct)

    def test_binarysearch_nonexistant(self):
        L2_result_iterative = binarysearch_iterative(self.L2, self.L2_target)
        L2_result_recursive = binarysearch_recursive(self.L2, self.L2_target, 0, len(self.L1)-1)

        self.assertEqual(L2_result_iterative, self.L2_correct)
        self.assertEqual(L2_result_recursive, self.L2_correct)

    def test_binarysearch_identical(self):
        L3_result_iterative = binarysearch_iterative(self.L3, self.L3_target)
        L3_result_recursive = binarysearch_recursive(self.L3, self.L3_target, 0, len(self.L3) - 1)

        self.assertEqual(L3_result_iterative, self.L3_correct)
        self.assertEqual(L3_result_recursive, self.L3_correct)

    def test_binarysearch_lastvalue(self):
        L4_result_iterative = binarysearch_iterative(self.L4, self.L4_target)
        L4_result_recursive = binarysearch_recursive(self.L4, self.L4_target, 0, len(self.L4) - 1)

        self.assertEqual(L4_result_iterative, self.L4_correct)
        self.assertEqual(L4_result_recursive, self.L4_correct)

    def test_binarysearch_firstvalue(self):
        L5_result_iterative = binarysearch_iterative(self.L5, self.L5_target)
        L5_result_recursive = binarysearch_recursive(self.L5, self.L5_target, 0, len(self.L5) - 1)

        self.assertEqual(L5_result_iterative, self.L5_correct)
        self.assertEqual(L5_result_recursive, self.L5_correct)

    def test_binarysearch_empty(self):
        L6_result_iterative = binarysearch_iterative(self.L6, self.L6_target)
        L6_result_recursive = binarysearch_recursive(self.L6, self.L6_target, 0, len(self.L6) - 1)

        self.assertEqual(L6_result_iterative, self.L6_correct)
        self.assertEqual(L6_result_recursive, self.L6_correct)

    def test_binarysearch_standard(self):
        L7_result_iterative = binarysearch_iterative(self.L7, self.L7_target)
        L7_result_recursive = binarysearch_recursive(self.L7, self.L7_target, 0, len(self.L7) - 1)

        self.assertEqual(L7_result_iterative, self.L7_correct)
        self.assertEqual(L7_result_recursive, self.L7_correct)


if __name__ == '__main__':
    print("Running sorting tests:")
    unittest.main()