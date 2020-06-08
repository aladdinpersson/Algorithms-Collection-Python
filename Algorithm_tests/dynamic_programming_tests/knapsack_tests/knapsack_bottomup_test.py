import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/dynamic_programming/knapsack")

# If run from local:
# sys.path.append('../../../Algorithms/dynamic_programming/knapsack/')
from knapsack_bottomup import knapsack


class test_KnapSack(unittest.TestCase):
    def setUp(self):
        self.weights1, self.values1, self.capacity1 = [], [], 100
        self.n1 = len(self.weights1)
        self.correctvalue1, self.correctitems1 = 0, []

        self.weights2, self.values2, self.capacity2 = [10], [50], 100
        self.n2 = len(self.weights2)
        self.correctvalue2, self.correctitems2 = 50, [0]

        self.weights3, self.values3, self.capacity3 = [10, 20, 30], [-10, -20, -30], 100
        self.n3 = len(self.weights2)
        self.correctvalue3, self.correctitems3 = 0, []

        self.weights4, self.values4, self.capacity4 = (
            [1, 2, 4, 2, 5],
            [5, 3, 5, 3, 2],
            5,
        )
        self.n4 = len(self.weights4)
        self.correctvalue4, self.correctitems4 = 11, [0, 1, 3]

        self.weights5, self.values5, self.capacity5 = [10, 10, 10], [30, 30, 30], 5
        self.n5 = len(self.weights5)
        self.correctvalue5, self.correctitems5 = 0, []

    def test_noitems(self):
        total_value, items = knapsack(
            self.n1, self.capacity1, self.weights1, self.values1
        )
        self.assertEqual(self.correctvalue1, total_value)
        self.assertEqual(self.correctitems1, items)

    def test_singleitem_value(self):
        total_value, items = knapsack(
            self.n2, self.capacity2, self.weights2, self.values2
        )
        self.assertEqual(self.correctvalue2, total_value)
        self.assertEqual(self.correctitems2, items)

    def test_negativevalues(self):
        total_value, items = knapsack(
            self.n3, self.capacity3, self.weights3, self.values3
        )
        self.assertEqual(self.correctvalue3, total_value)
        self.assertEqual(self.correctitems3, items)

    def test_simpleexample(self):
        total_value, items = knapsack(
            self.n4, self.capacity4, self.weights4, self.values4
        )
        self.assertEqual(self.correctvalue4, total_value)
        self.assertEqual(self.correctitems4, items)

    def test_weight_too_heavy(self):
        total_value, items = knapsack(
            self.n5, self.capacity5, self.weights5, self.values5
        )
        self.assertEqual(self.correctvalue5, total_value)
        self.assertEqual(self.correctitems5, items)


if __name__ == "__main__":
    print("Running Knapsack tests:")
    unittest.main()
