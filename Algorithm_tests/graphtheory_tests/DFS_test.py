# Import folder where sorting algorithms
import sys
import unittest
from collections import deque

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/graphtheory/depth-first-search/')

# If run from local:
#sys.path.append('../../Algorithms/graphtheory/depth-first-search/')
from DFS_recursive import DFS as DFS_rec
from DFS_stack_iterative import DFS as DFS_stack

class test_DFS(unittest.TestCase):

    def setUp(self):
        self.G1 = {1:[2],2:[1,3],3:[2]}
        self.correct_visited1 = [True] * 3
        self.correct_path1 = [1,2,3]
        self.DFS_recursive_visited1 = [False for i in range(1, len(self.G1) + 1)]

        self.G2 = {1:[2], 2:[1,3,4], 3:[2], 4:[2,5], 5:[4]}
        self.correct_visited2 = [True] * 5
        self.DFS_recursive_visited2 = [False for i in range(1, len(self.G2) + 1)]

        self.G3 = {1:[2], 2:[1,3,4], 3:[2], 4:[2], 5:[]}
        self.correct_visited3 = [True]*4 + [False]
        self.DFS_recursive_visited3= [False for i in range(1, len(self.G3) + 1)]

        self.G4 = {1:[2,3,4], 2:[1,3,4], 3:[1,2,4], 4:[1,2,3]}
        self.correct_visited4 = [True]*4
        self.DFS_recursive_visited4 = [False for i in range(1, len(self.G4) + 1)]


    def test_linear_graph(self):
        visited, path = DFS_stack(self.G1, start_node=1)
        self.assertEqual(visited, self.correct_visited1)
        self.assertEqual(path, self.correct_path1)

        DFS_rec(self.G1, 1, self.DFS_recursive_visited1)
        self.assertEqual(self.DFS_recursive_visited1, self.correct_visited1)

    def test_simple_graph(self):
        visited, path = DFS_stack(self.G2, start_node=1)
        self.assertEqual(visited, self.correct_visited2)

        DFS_rec(self.G2, 1, self.DFS_recursive_visited2)
        self.assertEqual(self.DFS_recursive_visited2, self.correct_visited2)

    def test_disconnected_graph(self):
        visited, path = DFS_stack(self.G3, start_node=1)
        self.assertEqual(visited, self.correct_visited3)

        DFS_rec(self.G3, 1, self.DFS_recursive_visited3)
        self.assertEqual(self.DFS_recursive_visited3, self.correct_visited3)

    def test_complete_graph(self):
        visited, path = DFS_stack(self.G4, start_node=1)
        self.assertEqual(visited, self.correct_visited4)

        DFS_rec(self.G4, 1, self.DFS_recursive_visited4)
        self.assertEqual(self.DFS_recursive_visited4, self.correct_visited4)

if __name__ == '__main__':
    print("Running BFS/DFS tests:")
    unittest.main()