import graphs_2 as g

G = {
    1: [2, 4],
    2: [1, 3],
    4: [5],
    5: [2, 6],
    7: [1]
}

#print(g.neighbors(G, 7, 3))


import matplotlib.pyplot as plt
import networkx as nx
from typing import List, NamedTuple
from typing import List, Set, Dict
from enum import Enum
from collections import namedtuple


# print(g.load_multigraph_from_file("directed_graph_blank_lines.dat"))
# print(nx.dijkstra_path_length(G, 1, 3))
# b = nx.MultiDiGraph()
# b.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.2), (2, 4, 0.3), (1, 3, 1.0)])
# a = g.find_min_trail(b, 1, 4)
# total = 0
# for i in range(len(a)):
#     total += a[i].Weight
# print(total)
# print(nx.dijkstra_path_length(b,1,3))
# print(g.trail_to_str(a))


# with open("directed_graph_blank_lines.dat", 'r') as f:
#     M_graph = nx.MultiDiGraph()
#     path = []
#     for line in f.readlines():
#         if(line.strip() != ""):
#             path.append(tuple(map(int, line.strip().split(" ")[
#                 :-1]))+(float(line.strip().split(" ")[-1]),))
# M_graph.add_weighted_edges_from(path)
# print(M_graph)
VertexID = int
EdgeID = int

# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]

Distance = int


class TrailSegmentEntry(NamedTuple):
    v_start: VertexID
    v_end: VertexID
    edge_id: EdgeID
    weight: float


Trail = List[TrailSegmentEntry]




def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:

    with open("directed_graph_blank_lines.dat", 'r') as f:
        M_graph = nx.MultiDiGraph()
        path = []
        for line in f.readlines():
            if(line.strip() != ""):
                path.append(tuple(map(int, line.strip().split(" ")[
                    :-1]))+(float(line.strip().split(" ")[-1]),))
    M_graph.add_weighted_edges_from(path)
    return M_graph


def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    
    path = nx.dijkstra_path(g, v_start, v_end)
    min_path = []
    for i, v in enumerate(path[:-1]):
        min_val = min([val['weight'] for key, val in g[v]
                    [path[i+1]].items() if 'weight' in val])
        edge = [key for key, val in g[v][path[i+1]].items() if min_val ==
                val['weight']][0]
        min_path.append(TrailSegmentEntry(v, path[i+1], edge, min_val))
    return min_path

def trail_to_str(trail: Trail) -> str:
    
    distance = 0
    str_path = ""
    for path in trail:
        str_path += f"{path.v_start} -[{path.edge_id}: {path.weight}]-> "
        distance += path.weight
    str_path += f"{path.v_end}  (total = {distance})"
    return str_path

G = load_multigraph_from_file("directed_graph_blank_lines.dat")
print(G)
print(find_min_trail(G, 1, 3))
print(trail_to_str(find_min_trail(G, 1, 3)))