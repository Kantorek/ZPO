#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Set, Dict
 
# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int
 
# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
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
    raise NotImplementedError()