import graphs_2 as g

G = {
    1: [2, 4],
    2: [1, 3],
    4: [5],
    5: [2, 6],
    7: [1]
}

print(g.neighbors(G, 7, 3))


import networkx as nx
import matplotlib.pyplot as plt

    # Stwórz obiekt reprezentujący graf 
    # skierowany (directed graph) bez krawędzi wielokrotnych...
G = nx.DiGraph()
    # ...i dodaj do niego krawędzie - lista 
    # składa się z krotek, z których każda zawiera opis krawędzi:
    # (wierzchołek początkowy, wierzchołek końcowy, waga krawędzi)
G.add_weighted_edges_from([(1, 2, 1), (1, 4, 1), (2, 1, 1), (2, 3, 1),
    (4, 5, 1), (5, 2, 1), (5, 6, 1), (7, 1, 1)])

    # Zwizualizuj graf (wierzchołki wraz z 
    # etykietami, krawędzie z wagami):
    # (1) wyznacz położenie wierzchołków za 
    # pomocą algorytmu Fruchtermana-Reingolda
pos = nx.spring_layout(G)
    # (2) narysuj graf używając obliczonych 
    # położeń wierzchołków, wyświetl etykiety wierzchołków
nx.draw(G, pos=pos, with_labels=True)
    # (3) dokonaj wizualizacji wag krawędzi
nx.draw_networkx_edge_labels(G, pos, 
    edge_labels=nx.get_edge_attributes(G, 'weight'))
    # UWAGA: Diagram zostanie wyświetlony dopiero po 
    # użyciu polecenia `plt.show()`!

    # Wyznacz najkrótszą ścieżkę z wierzchołka o 
    # etykiecie 1 do wierzchołka o etykiecie 3 z użyciem
    #   algorytmu Dijkstry.
dijkstra_path_nodes = nx.dijkstra_path(G, 1, 3)
    # Na podstawie najkrótszej ścieżki stwórz listę 
    # krawędzi tworzących najkrótszą drogę.
edges_in_path = list(zip(dijkstra_path_nodes[0:], 
    dijkstra_path_nodes[1:]))
    # Zaznacz na diagramie grafu najkrótszą drogę.
nx.draw_networkx_edges(G, pos, edgelist=edges_in_path,
    width=3, alpha=0.5, edge_color='b', style='dashed')
# plt.show()

print(g.load_multigraph_from_file("directed_graph_blank_lines.dat"))
print(nx.dijkstra_path_length(G, 1, 3))
b = nx.MultiDiGraph()
b.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.2), (2, 4, 0.3), (1, 3, 1.0)])
a = g.find_min_trail(b, 1, 4)
total = 0
for i in range(len(a)):
    total += a[i].Weight
print(total)
print(nx.dijkstra_path_length(b,1,3))
print(g.trail_to_str(a))