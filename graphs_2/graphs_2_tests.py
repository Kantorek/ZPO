import unittest
import graphs_2 as g
import networkx as nx


test_graph = nx.MultiDiGraph()
test_graph.add_weighted_edges_from([(1, 2, 0.7), (2, 3, 0.6), (2, 3, 0.5), (1, 3, 1.4)])
min_path = g.find_min_trail(test_graph, 1, 3)
distance = 0
for x in range(len(min_path)):
    distance += min_path[x].Weight

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(distance, nx.dijkstra_path_length(test_graph, 1, 3))

if __name__ == '__main__':
    unittest.main()