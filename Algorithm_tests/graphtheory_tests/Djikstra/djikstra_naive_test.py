# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append('Algorithms/graphtheory/dijkstra/')

# If run from local:
#sys.path.append('../../../Algorithms/graphtheory/dijkstra/')

from dijkstra import dijkstra

class test_Dijkstra(unittest.TestCase):
    def setUp(self):
        self.G1 = {}
        self.correct_path1 = []
        self.correct_dist1 = float("inf")

        self.G2 = {1:{2:1, 4:10}, 2:{3:15}, 3:{6:5}, 4:{5:1}, 5:{6:1}, 6: {}}
        self.correct_path2 = [1,4,5,6]
        self.correct_dist2 = 12

        self.G3 = {1: {2: 1, 4: 10}, 2: {3: 15}, 3: {}, 4: {5:1}, 5: {}, 6: {}}
        self.correct_path3 = []
        self.correct_dist3 = float("inf")

        self.G4 = {1: {2: 1, 4: 10}, 2: {3: 15}, 3: {6: 5}, 4: {5: 1}, 5: {6: 1}, 6: {}}
        self.correct_path4 = [1, 4, 5]
        self.correct_dist4 = 11

    def test_emptygraph(self):
        path_to_take, distance = dijkstra(self.G1, 0, 1)
        self.assertEqual(distance, self.correct_dist1)
        self.assertEqual(path_to_take, self.correct_path1)

    def test_simplegraph(self):
        path_to_take, distance = dijkstra(self.G2, 1, 6)
        self.assertEqual(distance, self.correct_dist2)
        self.assertEqual(path_to_take, self.correct_path2)

    def test_no_path_exists(self):
        path_to_take, distance = dijkstra(self.G3, 1, 6)
        self.assertEqual(distance, self.correct_dist3)
        self.assertEqual(path_to_take, self.correct_path3)

    def test_not_endpoint(self):
        path_to_take, distance = dijkstra(self.G4, 1, 5)
        self.assertEqual(distance, self.correct_dist4)
        self.assertEqual(path_to_take, self.correct_path4)


if __name__ == '__main__':
    print("Running Djikstra tests:")
    unittest.main()