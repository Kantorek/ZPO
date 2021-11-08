import unittest
import graphs_2 as g
import networkx as nx


class Test(unittest.TestCase):

    def test(self):
        G = g.load_multigraph_from_file("directed_graph.dat")
        trail = g.find_min_trail(G, 1, 3)
        distance = 0
        for x in trail:
            distance += x.weight
    
        self.assertEqual(distance, nx.dijkstra_path_length(G, 1, 3))

if __name__ == '__main__':
    unittest.main()