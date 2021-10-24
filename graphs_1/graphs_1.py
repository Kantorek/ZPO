#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict
 
def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dictonary = {}
    for start, row in enumerate(adjmat, 1):
        dictonary[start] = []
        for stop, num_of_edges in enumerate(row, 1):
            dictonary[start].extend([stop] * num_of_edges)
        if not dictonary[start]:
            del dictonary[start]
    return dictonary

def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    def dfs_recursive_visited(G: Dict[int, List[int]], s: int, 
    visited: List[int] = None) -> List[int]:
        if visited is None:
            visited = []
        visited.append(s)
        for u in G[s]:
            if u not in visited:
             dfs_recursive_visited(G, u, visited)
        return visited
    return dfs_recursive_visited(G, s)
 
def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = []
    visited = []
    stack.append(s)
    while stack:
        looking_stack = []
        s = stack[0]
        stack.pop(0)
        if s not in visited:
            visited.append(s)
            for u in G[s]:
                if u in visited:
                    stack.append(u)
                else:
                    looking_stack.append(u)
                    stack = looking_stack + stack
    return visited

def is_acyclic(G: Dict[int, List[int]]) -> bool:
    def dfs_acyclic_test(G: Dict[int, List[int]], s: int, 
    visited: List[int] = None) -> bool:
        if visited is None:
            visited = []
        visited.append(s)
        if s in G:
            for u in G[s]:
                if u in visited:
                    return True
                if dfs_acyclic_test(G, u, visited[:]):
                    return True
            return False

    for key in G:
        if dfs_acyclic_test(G, key):
            return False
    return True