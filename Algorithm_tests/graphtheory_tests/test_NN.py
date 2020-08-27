import unittest
import sys

# Import from different folder
sys.path.append("Algorithms/graphtheory/nearest-neighbor-tsp/")

import NearestNeighborTSP


class TestNN(unittest.TestCase):
    def setUp(self):
        self.G1 = [[0,3,-1],[3,0,1],[-1,1,0]]
        self.correct_path1 = [0,1,2,0]

        # No possible solution for this one so its a dead end
        self.G2 = [[0, 2, -1,-1,-1], [2, 0,5,1,-1], [-1, 5, 0, -1, -1],[-1, 1, -1, 0, 3], [-1, -1, -1, 3, 0]]
        self.correct_path2 = [0,1,3,4]

        # No possible solution for this one so its a dead end
        self.G3 = [[0, 2, -1,-1,-1], [2, 0,5,1,-1], [-1, 5, 0, -1, -1],[-1, 1, -1, 0, -1], [-1, -1, -1, -1, 0]]
        self.correct_path3 = [0, 1, 3]

        # Multiple possible solutions
        self.G4 = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
        self.correct_path4 = [0, 1, 2, 3, 0]


    # adjacency matrix of a graph for testing
    adjMatrix = [[0,2,5,-1,3],[2,0,2,4,-1],[5,2,0,5,5],[-1,4,5,0,2],[3,-1,5,2,0]]
    # correct rank of each node's neighbors
    correctNeighbors = [[1,4,2],[0,2,3],[1,0,3,4],[4,1,2],[3,0,2]]


    def test_0_rankNeighbors(self):
        for i in range(0,4):
            self.assertEqual(NearestNeighborTSP.rankNeighbors(i, self.adjMatrix), self.correctNeighbors[i], "Check if order is different.")


    def test_1_nnTSP(self):
        path=NearestNeighborTSP.nnTSP(self.adjMatrix)
        # Test if path is null
        self.assertIsNotNone(path,"Output is empty")
        # Test if path is not complete
        self.assertEqual(len(path),len(self.adjMatrix)+1,"Path in incomplete")


    def test_linear_graph(self):
        #print(NearestNeighbor.nnTSP(self.G2))
        path = NearestNeighborTSP.nnTSP(self.G1)
        self.assertEqual(path,self.correct_path1)


    def test_simple_graph(self):
        path = NearestNeighborTSP.nnTSP(self.G2)
        self.assertEqual(path,self.correct_path2)


    def test_disconnected_graph(self):
        path = NearestNeighborTSP.nnTSP(self.G3)
        self.assertEqual(path, self.correct_path3)


    def test_complete_graph(self):
        path = NearestNeighborTSP.nnTSP(self.G4)
        self.assertEqual(path, self.correct_path4)

if __name__ == '__main__':
    print("Running Nearest Neighbor TSP solver tests:")
    unittest.main()