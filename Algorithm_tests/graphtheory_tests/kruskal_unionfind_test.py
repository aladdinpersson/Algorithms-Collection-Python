# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/graphtheory/kruskal/')

# If run from local:
#sys.path.append('../../Algorithms/graphtheory/kruskal/')
from kruskal_unionfind import kruskal

class test_Kruskal(unittest.TestCase):

    def setUp(self):
        #self.G1 = {1:[(10, 2, 1)], 2:[(10, 1, 2), (10, 3, 2)], 3:[(10, 2, 3)]}
        self.G1 = [(10, 2, 1), (10, 1, 2), (10, 3, 2), (10, 2, 3)]
        self.num_nodes1 = 3
        self.correct_cost1 = 20
        self.correct_MST1 = [(1,2,10),(2,3,10)]

        self.G2 = [(10,2,1),(10,3,1),(10,1,2),(100,3,2),(10,1,3),(100,2,3)]
        self.num_nodes2 = 3
        self.correct_cost2 = 20
        self.correct_MST2 = [(1, 2, 10), (1, 3, 10)]

        self.G3 = [(1,2,1),(1,1,2),(1,3,2),(1,4,3),(5,5,3),(1,3,4),(1,5,4),(5,3,5),(1,4,5)]
        self.num_nodes3 = 5
        self.correct_cost3 = 4
        self.correct_MST3 = [(1, 2, 1), (2,3,1), (3,4,1), (4,5,1)]

        self.G4 = [(1,2,1),(1,1,2),(1,4,3),(1,3,4)]
        self.num_nodes4 = 4
        self.correct_cost4 = 2
        self.correct_MST4 = [(1,2,1), (3,4,1)]

        self.G5 = {}
        self.num_nodes5 = 0
        self.correct_cost5 = 0
        self.correct_MST5 = []

        # Takes as input G which will have {node1: [(cost, to_node, node1), ...], node2:[(...)] }
    def test_linear_graph(self):
        MST, cost = kruskal(sorted(self.G1, key=lambda tup:tup[0]), self.num_nodes1)
        self.assertEqual(MST, self.correct_MST1)
        self.assertEqual(cost, self.correct_cost1)

    def test_triangle_graph(self):
        MST, cost = kruskal(sorted(self.G2, key=lambda tup:tup[0]),self.num_nodes2)
        self.assertEqual(MST, self.correct_MST2)
        self.assertEqual(cost, self.correct_cost2)

    def test_trickier_mst(self):
        MST, cost = kruskal(sorted(self.G3, key=lambda tup:tup[0]),self.num_nodes3)
        self.assertEqual(MST, self.correct_MST3)
        self.assertEqual(cost, self.correct_cost3)

    def test_disconnected_graph(self):
        MST, cost = kruskal(sorted(self.G4, key=lambda tup:tup[0]), self.num_nodes4)
        self.assertEqual(MST, self.correct_MST4)
        self.assertEqual(cost, self.correct_cost4)

    def test_empty_graph(self):
        MST, cost = kruskal(self.G5, self.num_nodes5)
        self.assertEqual(MST, self.correct_MST5)
        self.assertEqual(cost, self.correct_cost5)

if __name__ == '__main__':
    print("Running Kruskal tests:")
    unittest.main()