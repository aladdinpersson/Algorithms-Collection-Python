# Import packages
import sys
import unittest
# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/other')

# If run from local:
#sys.path.append('../../Algorithms/other')

from median_maintenance import Maintain_Median


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.data1 = [1, 3, 8, 5, 10]
        self.correct1 = 5

        self.data2 = []
        self.correct2 = []

        self.data3 = [10]
        self.correct3 = 10

        self.data4 = [1, 2, 3, 4]
        self.correct4 = 2.5

        self.data5 = [1, 10, 2, 9, 11, 4, 6, 5, 3, 8, 7]
        self.correct5 = 6


    def test_basic(self):
        maintain_median = Maintain_Median()
        median = maintain_median.main(self.data1)
        self.assertEqual(median, self.correct1)

    def test_empty(self):
        maintain_median = Maintain_Median()
        median = maintain_median.main(self.data2)
        self.assertEqual(median, self.correct2)

    def test_single(self):
        maintain_median = Maintain_Median()
        median = maintain_median.main(self.data3)
        self.assertEqual(median, self.correct3)

    def test_even(self):
        maintain_median = Maintain_Median()
        median = maintain_median.main(self.data4)
        self.assertEqual(median, self.correct4)

    def test_longer_example(self):
        maintain_median = Maintain_Median()
        median = maintain_median.main(self.data5)
        self.assertEqual(median, self.correct5)



if __name__ == '__main__':
    unittest.main()
