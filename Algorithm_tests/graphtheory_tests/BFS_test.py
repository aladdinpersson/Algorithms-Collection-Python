# Import folder where sorting algorithms
import sys
import unittest
from collections import deque

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/graphtheory/breadth-first-search/")

# If run from local:
# sys.path.append('../../Algorithms/graphtheory/breadth-first-search/')
from BFS_queue_iterative import BFS


class test_BFS(unittest.TestCase):
    def setUp(self):
        self.G1 = {1: [2], 2: [1, 3], 3: [2]}
        self.correct_visited1 = [True] * 3
        self.correct_path1 = [1, 2, 3]

        self.G2 = {1: [2], 2: [1, 3, 4], 3: [2], 4: [2, 5], 5: [4]}
        self.correct_visited2 = [True] * 5

        self.G3 = {1: [2], 2: [1, 3, 4], 3: [2], 4: [2], 5: []}
        self.correct_visited3 = [True] * 4 + [False]

        self.G4 = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}
        self.correct_visited4 = [True] * 4

        self.G5 = {
            1: [2, 3, 4],
            2: [1, 5],
            3: [1, 7],
            4: [1, 6],
            5: [2],
            6: [4],
            7: [3],
        }
        self.correct_visited5 = [True] * 7

    def test_linear_graph(self):
        visited, path = BFS(self.G1, start_node=1)
        self.assertEqual(visited, self.correct_visited1)
        self.assertEqual(path, self.correct_path1)

    def test_simple_graph(self):
        visited, path = BFS(self.G2, start_node=1)
        self.assertTrue(path.index(3) < path.index(5))
        self.assertEqual(visited, self.correct_visited2)

    def test_disconnected_graph(self):
        visited, path = BFS(self.G3, start_node=1)
        self.assertEqual(visited, self.correct_visited3)

    def test_complete_graph(self):
        visited, path = BFS(self.G4, start_node=1)
        self.assertEqual(visited, self.correct_visited4)

    def test_breadth_before_depth(self):
        visited, path = BFS(self.G5, start_node=1)
        self.assertEqual(visited, self.correct_visited5)

        # Make sure it goes breadth first
        self.assertTrue(path.index(2) < path.index(5))
        self.assertTrue(path.index(2) < path.index(6))
        self.assertTrue(path.index(2) < path.index(7))
        self.assertTrue(path.index(3) < path.index(5))
        self.assertTrue(path.index(3) < path.index(6))
        self.assertTrue(path.index(3) < path.index(7))
        self.assertTrue(path.index(4) < path.index(5))
        self.assertTrue(path.index(4) < path.index(6))
        self.assertTrue(path.index(4) < path.index(7))


if __name__ == "__main__":
    print("Running BFS/DFS tests:")
    unittest.main()
