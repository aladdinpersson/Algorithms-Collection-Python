# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/graphtheory/kahns-toposort/")

# If run from local:
# sys.path.append('../../Algorithms/graphtheory/kahns-toposort')

from kahn_topological_ordering import topological_ordering
from collections import defaultdict


class test_TopologicalOrdering(unittest.TestCase):
    def setUp(self):
        self.G1 = {}
        self.degree_incoming1 = defaultdict(int, {})
        self.correct_isDAG1 = False
        self.correct_path1 = []

        self.G2 = {"1": ["2"], "2": ["3"], "3": ["4"], "4": ["5"], "5": []}
        self.degree_incoming2 = defaultdict(int, {"2": 1, "3": 1, "4": 1, "5": 1})
        self.correct_isDAG2 = True
        self.correct_path2 = ["1", "2", "3", "4", "5"]

        self.G3 = {
            "1": ["2", "3", "4", "5"],
            "2": ["3", "4", "5"],
            "3": ["4", "5"],
            "4": ["5"],
            "5": [],
        }
        self.degree_incoming3 = defaultdict(int, {"2": 1, "3": 2, "4": 3, "5": 4})
        self.correct_isDAG3 = True
        self.correct_path3 = ["1", "2", "3", "4", "5"]

        self.G4 = {
            "1": ["2", "3", "4", "5"],
            "2": ["3", "4", "5"],
            "3": ["2", "4", "5"],
            "4": ["5"],
            "5": [],
        }
        self.degree_incoming4 = defaultdict(int, {"2": 2, "3": 2, "4": 3, "5": 4})
        self.correct_isDAG4 = False
        self.correct_path4 = []

    def test_emptygraph(self):
        path_to_take, is_DAG = topological_ordering(self.G1, self.degree_incoming1)
        self.assertEqual(path_to_take, self.correct_path1)
        self.assertEqual(is_DAG, self.correct_isDAG1)

    def test_clear_ordering(self):
        path_to_take, is_DAG = topological_ordering(self.G2, self.degree_incoming2)
        self.assertEqual(path_to_take, self.correct_path2)
        self.assertEqual(is_DAG, self.correct_isDAG2)

    def test_more_complicated_graph(self):
        path_to_take, is_DAG = topological_ordering(self.G3, self.degree_incoming3)
        self.assertEqual(path_to_take, self.correct_path3)
        self.assertEqual(is_DAG, self.correct_isDAG3)

    def test_no_topological_ordering(self):
        path_to_take, is_DAG = topological_ordering(self.G4, self.degree_incoming4)
        self.assertEqual(path_to_take, self.correct_path4)
        self.assertEqual(is_DAG, self.correct_isDAG4)


if __name__ == "__main__":
    print("Running Topological Ordering tests:")
    unittest.main()
