import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/dynamic_programming/')

# If run from local:
#sys.path.append('../../../Algorithms/dynamic_programming/')
from weighted_interval_scheduling import WeightedIntervalScheduling

class test_weighted_interval_scheduling(unittest.TestCase):
    def setUp(self):
        self.I1 = []
        self.I2 = [(0,3,10)]

    def test_simplecase(self):
        sequence_align = SequenceAlignment(self.x1, self.y1)
        editsteps, _ = sequence_align.alignment()
        self.assertEqual(self.correct_editstep1, editsteps)


if __name__ == '__main__':
    print("Running Weighted Interval Scheduling tests:")
    unittest.main()