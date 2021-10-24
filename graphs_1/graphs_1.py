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
    def dfs_recursive_visited(G, s, visited = None):
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


A = [
    [1, 3, 0],
    [0, 0, 2],
    [1, 2, 0]
]

G = {
    1: [2, 3, 5],
    2: [1, 4, 6],
    3: [1, 7],
    4: [2],
    5: [1, 6],
    6: [2, 5],
    7: [3]
}

print(A)
print(adjmat_to_adjlist(A))
print(dfs_recursive(G, 1))
print(dfs_iterative(G, 1))