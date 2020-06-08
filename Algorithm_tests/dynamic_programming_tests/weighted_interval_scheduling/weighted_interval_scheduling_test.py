import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/dynamic_programming/")

# If run from local:
# sys.path.append('../../../Algorithms/dynamic_programming/')
from weighted_interval_scheduling import WeightedIntervalScheduling


class test_weighted_interval_scheduling(unittest.TestCase):
    def setUp(self):
        self.I1 = []
        self.correct_maxweight1 = 0
        self.correct_intervals1 = []

        self.I2 = [(0, 3, 10)]
        self.correct_maxweight2 = 10
        self.correct_intervals2 = [(0, 3, 10)]

        self.I3 = [(0, 3, 5), (2, 5, 15), (4, 6, 5)]
        self.correct_maxweight3 = 15
        self.correct_intervals3 = [(2, 5, 15)]

        self.I4 = [(0, 3, 5), (3, 5, 15), (5, 7, 5)]
        self.correct_maxweight4 = 25
        self.correct_intervals4 = [(0, 3, 5), (3, 5, 15), (5, 7, 5)]

        self.I5 = [(0, 3, 5), (3, 5, -100), (5, 7, -50)]
        self.correct_maxweight5 = 5
        self.correct_intervals5 = [(0, 3, 5)]

        self.I6 = [(0, 50, 1), (0, 49, 1), (0, 48, 1), (15, 20, 10)]
        self.correct_maxweight6 = 10
        self.correct_intervals6 = [(15, 20, 10)]

        self.I7 = [(0, 50, 1), (0, 50, 1), (0, 50, 1), (0, 50, 1)]
        self.correct_maxweight7 = 1
        self.correct_intervals7 = [(0, 50, 1)]

        self.I8 = [(0, 50, 1), (0, 49, 1), (0, 48, 1), (0, 47, 1)]
        self.correct_maxweight8 = 1
        self.correct_intervals8 = [(0, 47, 1)]

        self.I9 = [(0, 50, 2), (0, 49, 1), (0, 48, 1), (0, 47, 1)]
        self.correct_maxweight9 = 2
        self.correct_intervals9 = [(0, 50, 2)]

    def test_empty_interval(self):
        weightedinterval = WeightedIntervalScheduling(self.I1)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight1, max_weight)
        self.assertEqual(self.correct_intervals1, best_intervals)

    def test_single_interval(self):
        weightedinterval = WeightedIntervalScheduling(self.I2)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight2, max_weight)
        self.assertEqual(self.correct_intervals2, best_intervals)

    def test_overlapping_intervals(self):
        weightedinterval = WeightedIntervalScheduling(self.I3)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight3, max_weight)
        self.assertEqual(self.correct_intervals3, best_intervals)

    def test_no_overlapping_intervals(self):
        weightedinterval = WeightedIntervalScheduling(self.I4)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight4, max_weight)
        self.assertEqual(self.correct_intervals4, best_intervals)

    def test_negative_weights(self):
        weightedinterval = WeightedIntervalScheduling(self.I5)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight5, max_weight)
        self.assertEqual(self.correct_intervals5, best_intervals)

    def test_interval_contained_in_all_intervals(self):
        weightedinterval = WeightedIntervalScheduling(self.I6)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight6, max_weight)
        self.assertEqual(self.correct_intervals6, best_intervals)

    def test_all_intervals_same(self):
        weightedinterval = WeightedIntervalScheduling(self.I7)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight7, max_weight)
        self.assertEqual(self.correct_intervals7, best_intervals)

    def test_earliest_finish_time(self):
        weightedinterval = WeightedIntervalScheduling(self.I8)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight8, max_weight)
        self.assertEqual(self.correct_intervals8, best_intervals)

    def test_earliest_finish_time_not_best(self):
        weightedinterval = WeightedIntervalScheduling(self.I9)
        max_weight, best_intervals = weightedinterval.weighted_interval()
        self.assertEqual(self.correct_maxweight9, max_weight)
        self.assertEqual(self.correct_intervals9, best_intervals)


if __name__ == "__main__":
    print("Running Weighted Interval Scheduling tests:")
    unittest.main()
