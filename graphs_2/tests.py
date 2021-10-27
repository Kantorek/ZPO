import graphs_2 



G = {
    1: [2, 4],
    2: [3],
    4: [5],
    5: [2, 6],
    7: [1]
}

print(graphs_2.neighbors(G, 1, 2))
