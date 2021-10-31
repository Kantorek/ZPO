# Jakub Klimek, 407457

from typing import List, Set, Dict
import networkx as nx


VertexID = int
AdjList = Dict[VertexID, List[VertexID]]
Distance = int
 
def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    length = 0
    n_set = set()
    if max_distance < 0:
        return None
    while length < max_distance:
        if start_vertex_id in adjlist:
            for x in adjlist[start_vertex_id]:
                n_set.update(adjlist[start_vertex_id])
        n_list = list(n_set)
        length += 1
        if length < max_distance:
            for x in n_list:
                if x in adjlist: 
                    n_set.update(adjlist[x])
                n_list = list(n_set)
    return n_set

EdgeID = int

class TrailSegmentEntry:
    Start_ver: VertexID
    End_ver: VertexID
    Edge: EdgeID
    Weight: float
 
Trail = List[TrailSegmentEntry]
  
def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:

    with open(filepath) as file:
        weights = []
        for line in file:
            if line.strip():
                v = line.split()
                s_val = (int(v[0]), int(v[1]), float(v[2]))
                weights.append(s_val)
        M_Graph = nx.MultiDiGraph()
        M_Graph.add_edges_from(weights)
    return M_Graph
 
 
def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.
 
    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """

 
 
    return
    raise NotImplementedError()
 
 
def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.
 
    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    raise NotImplementedError()