import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
#sys.path.append('Algorithms/dynamic_programming/')

# If run from local:
sys.path.append('../../../Algorithms/dynamic_programming/')
from weighted_interval_scheduling import WeightedIntervalScheduling

class test_weighted_interval_scheduling(unittest.TestCase):
    def setUp(self):
        self.I1 = []
        self.correct_maxweight1 = 0

        self.I2 = [(0,3,10)]
        self.correct_maxweight2 = 10

        self.I3 = [(0,3,5), (2,5,15), (4, 6, 5)]
        self.correct_maxweight3 = 5

    def test_empty_interval(self):
        weightedinterval = WeightedIntervalScheduling(self.I1)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight1, max_weight)

    def test_single_interval(self):
        weightedinterval = WeightedIntervalScheduling(self.I2)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight2, max_weight)

    def test_overlapping_intervals(self):
        weightedinterval = WeightedIntervalScheduling(self.I2)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight2, max_weight)

if __name__ == '__main__':
    print("Running Weighted Interval Scheduling tests:")
    unittest.main()