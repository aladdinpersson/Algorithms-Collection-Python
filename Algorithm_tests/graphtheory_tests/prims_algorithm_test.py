# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/graphtheory/prims/")

# If run from local:
# sys.path.append('../../Algorithms/graphtheory/prims/')
from prim_heap import prims_algo


class test_primsHeap(unittest.TestCase):
    def setUp(self):
        # How I've decided to construct the graph is confusing, but the reason is because we're using a min heap and
        # want first element in the tuple to be the cost of the edge. However when I return the MST, we want it to be
        # returned as: from_node, to_node, edge_cost, rather than the reverse for constructing the graph.

        self.G1 = {1: [(10, 2, 1)], 2: [(10, 1, 2), (10, 3, 2)], 3: [(10, 2, 3)]}
        self.correct_cost1 = 20
        self.correct_MST1 = [(1, 2, 10), (2, 3, 10)]

        self.G2 = {
            1: [(10, 2, 1), (10, 3, 1)],
            2: [(10, 1, 2), (100, 3, 2)],
            3: [(10, 1, 3), (100, 2, 3)],
        }
        self.correct_cost2 = 20
        self.correct_MST2 = [(1, 2, 10), (1, 3, 10)]

        self.G3 = {
            1: [(1, 2, 1)],
            2: [(1, 1, 2), (1, 3, 2)],
            3: [(1, 4, 3), (5, 5, 3)],
            4: [(1, 3, 4), (1, 5, 4)],
            5: [(5, 3, 5), (1, 4, 5)],
        }
        self.correct_cost3 = 4
        self.correct_MST3 = [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)]

        self.G4 = {1: [(1, 2, 1)], 2: [(1, 1, 2)], 3: [(1, 4, 3)], 4: [(1, 3, 4)]}
        self.correct_cost4 = 1
        self.correct_MST4 = [(1, 2, 1)]

        self.G5 = {}
        self.correct_cost5 = 0
        self.correct_MST5 = []

        # Takes as input G which will have {node1: [(cost, to_node, node1), ...], node2:[(...)] }

    def test_linear_graph(self):
        MST, cost = prims_algo(self.G1, start=1)
        self.assertEqual(MST, self.correct_MST1)
        self.assertEqual(cost, self.correct_cost1)

    def test_triangle_graph(self):
        MST, cost = prims_algo(self.G2, start=1)
        self.assertEqual(MST, self.correct_MST2)
        self.assertEqual(cost, self.correct_cost2)

    def test_trickier_mst(self):
        MST, cost = prims_algo(self.G3, start=1)
        self.assertEqual(MST, self.correct_MST3)
        self.assertEqual(cost, self.correct_cost3)

    def test_disconnected_graph(self):
        MST, cost = prims_algo(self.G4, start=1)
        self.assertEqual(MST, self.correct_MST4)
        self.assertEqual(cost, self.correct_cost4)

    def test_empty_graph(self):
        MST, cost = prims_algo(self.G5, start=1)
        self.assertEqual(MST, self.correct_MST5)
        self.assertEqual(cost, self.correct_cost5)


if __name__ == "__main__":
    print("Running Prims Heap tests:")
    unittest.main()
