import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
# sys.path.append('Algorithms/cryptology/ceasar_shifting_cipher')

# If run from local:
sys.path.append('../../Algorithms/dynamic_programming/knapsack/')
from knapsack_bottomup knapsack, find_opt

class test_KnapSack(unittest.TestCase):

    def test_findopt(self):
        pass

    def test_correctvalue(self):
        pass

    def test_(self):
        pass


if __name__ == '__main__':
    print("Running bellman ford tests:")
    unittest.main()