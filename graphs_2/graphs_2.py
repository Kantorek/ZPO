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

    min_path = []
    path = nx.dijkstra_path(g, v_start, v_end)
    for p_key in range(len(path)-1):
        explore_path = TrailSegmentEntry()
        var = {}
        explore_path.Start_ver = path[p_key]
        explore_path.End_ver = path[p_key+1]
        for w_key in g[path[p_key]][path[p_key+1]]:
            var[w_key] = g[path[p_key]][path[p_key+1]][w_key]['weight']
        explore_path.Edge = min(var, key=var.get)
        explore_path.Weight = var[explore_path.Edge]
        min_path.append(explore_path)
    return min_path
 
 
def trail_to_str(trail: Trail) -> str:
    distance = 0
    str_path = ""
    for x in range(len(trail)):
        distance += trail[x].Weight
        str_path += str(f"{trail[x].Start_ver} -[{x}: {trail[x].Weight}]-> ")
    str_path += str(f"{trail[len(trail)-1].End_ver}  (total = {distance})")
    return str_path