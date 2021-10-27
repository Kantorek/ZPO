import graphs_2 as g

G = {
    1: [2, 4],
    2: [3],
    4: [5],
    5: [2, 6],
    7: [1]
}

print(g.neighbors(G, 3, 2))