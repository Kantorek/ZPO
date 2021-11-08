with open("directed_graph_blank_lines.dat", 'r') as f:
    M_graph = nx.MultiDiGraph()
    path = []
    for line in f.readlines():
        if(line.strip() != ""):
            path.append(tuple(map(int, line.strip().split(" ")[
                :-1]))+(float(line.strip().split(" ")[-1]),))
M_graph.add_weighted_edges_from(path)
print(M_graph)