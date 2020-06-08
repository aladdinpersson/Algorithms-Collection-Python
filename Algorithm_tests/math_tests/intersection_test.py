# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/math/intersection_of_two_sets")

# If run from local:
# sys.path.append('../../Algorithms/math/intersection_of_two_sets')

from intersection_of_two_sets import intersection


class test_intersection(unittest.TestCase):
    def setUp(self):
        # test cases we wish to run
        self.L1 = [1, 3, 5, 7, 9, 10]
        self.L2 = [2, 4, 6, 11, 12]
        self.L1L2_correct = []

        self.L3 = [1, 3, 5, 10]
        self.L4 = [2, 4, 6, 10]
        self.L3L4_correct = [10]

        self.L5 = [1, 3, 5, 10]
        self.L6 = [1, 4, 6, 11]
        self.L5L6_correct = [1]

        self.L7 = [1, 2, 3, 4, 5, 6, 7]
        self.L8 = [1, 2, 3, 4, 5, 6, 7]
        self.L7L8_correct = [1, 2, 3, 4, 5, 6, 7]

        self.L9 = []
        self.L10 = []
        self.L9L10_correct = []

    def test_intersection_none(self):
        L1L2_output = intersection(self.L1, self.L2)
        self.assertEqual(L1L2_output, self.L1L2_correct)

    def test_intersection_lastelement(self):
        L3L4_output = intersection(self.L3, self.L4)
        self.assertEqual(L3L4_output, self.L3L4_correct)

    def test_intersection_firstelement(self):
        L5L6_output = intersection(self.L5, self.L6)
        self.assertEqual(L5L6_output, self.L5L6_correct)

    def test_intersection_allequal(self):
        L7L8_output = intersection(self.L7, self.L8)
        self.assertEqual(L7L8_output, self.L7L8_correct)

    def test_intersection_both_empty(self):
        L9L10_output = intersection(self.L9, self.L10)
        self.assertEqual(L9L10_output, self.L9L10_correct)


if __name__ == "__main__":
    print("Running sorting tests:")
    unittest.main()
