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

A = [
    [1, 3, 0],
    [0, 0, 1],
    [1, 2, 0]
]

print(A)
print(adjmat_to_adjlist(A))
