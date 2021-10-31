#!/usr/bin/python
# -*- coding: utf-8 -*-
# Jakub Klimek, 407457

from typing import List, Set, Dict
import networkx as nx


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

EdgeID = int

# Nazwana krotka reprezentująca segment ścieżki.
class TrailSegmentEntry:
    Start_ver: VertexID
    End_ver: VertexID
    Edge: EdgeID
    Weight: float
 
 
Trail = List[TrailSegmentEntry]
 
 
def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.
 
    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
 
    raise NotImplementedError()
 
 
def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.
 
    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    raise NotImplementedError()
 
 
def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.
 
    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    raise NotImplementedError()