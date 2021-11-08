# Jakub Klimek, 407457

from typing import List, Set, Dict, NamedTuple
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


class TrailSegmentEntry(NamedTuple):
    start_ver: VertexID
    end_ver: VertexID
    edge: EdgeID
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


def find_min_trail(g: nx.MultiDiGraph, start_ver: VertexID, end_ver: VertexID) -> Trail:
    
    path = nx.dijkstra_path(g, start_ver, end_ver)
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
        str_path += f"{path.start_ver} -[{path.edge}: {path.weight}]-> "
        distance += path.weight
    str_path += f"{path.end_ver}  (total = {distance})"
    return str_path