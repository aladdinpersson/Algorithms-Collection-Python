# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/other")

# If run from local:
# sys.path.append('../../Algorithms/other')

from interval_scheduling import interval_scheduling


class test_intervalscheduling(unittest.TestCase):
    def setUp(self):
        # test cases we wish to run
        self.R1 = [(0, 5), (3, 6), (5, 10)]
        self.R1_correct = [(0, 5), (5, 10)]

        self.R2 = []
        self.R2_correct = []

        self.R3 = [(0, 3), (3, 6), (6, 9), (9, 10)]
        self.R3_correct = [(0, 3), (3, 6), (6, 9), (9, 10)]

        self.R4 = [(1, 3), (0, 2), (1, 4), (2, 5)]
        self.R4_correct = [(0, 2), (2, 5)]

        self.R5 = [(0, 3)]
        self.R5_correct = [(0, 3)]

    def test_intervalscheduling_basic(self):
        O = []
        O = interval_scheduling(self.R1, O)
        self.assertEqual(O, self.R1_correct)

    def test_intervalscheduling_empty(self):
        O = []
        O = interval_scheduling(self.R2, O)
        self.assertEqual(O, self.R2_correct)

    def test_intervalscheduling_take_all(self):
        O = []
        O = interval_scheduling(self.R3, O)
        self.assertEqual(O, self.R3_correct)

    def test_intervalscheduling_unsorted(self):
        O = []
        O = interval_scheduling(self.R4, O)
        self.assertEqual(O, self.R4_correct)

    def test_intervalscheduling_one_element(self):
        O = []
        O = interval_scheduling(self.R5, O)
        self.assertEqual(O, self.R5_correct)


if __name__ == "__main__":
    print("Running Interval Scheduling tests:")
    unittest.main()
