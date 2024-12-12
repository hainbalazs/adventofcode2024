import networkx as nx

with open('input.txt', 'r') as f:
    T = f.readlines()

H, W = len(T), len(T[0]) - 1
is_in = lambda c, h, w: c[0] >= 0 and c[1] >= 0 and c[0] < h and c[1] < w
label = lambda grid, x: grid[x[1]][x[0]]
flat_index = lambda c, w: c[1] * w + c[0]
flat_to_c = lambda i, w: (i % w, i // w)

# undirected graph with no parallel edges allowed
G = nx.Graph()
for y in range(H):
    for x in range(W):
        p = (x,y)
        G.add_node(flat_index(p, W))

        candidates = [((x, y+1), 1), ((x, y-1), 1), ((x+1, y), 0), ((x-1, y), 0)]
        for c, axe in candidates:
            if is_in(c, H, W) and label(T, p) == label(T, c):
                G.add_edge(flat_index(p, W), flat_index(c, W), weight=axe)

total_prize = 0               
for component in nx.connected_components(G):
    S = G.subgraph(component)
    edges = S.edges(data=True)

    horizontal_edges = [(u,v) for (u, v, data) in edges if data['weight'] == 0]
    HS = S.edge_subgraph(horizontal_edges)

    vertical_edges = [(u,v) for (u, v, data) in edges if data['weight'] == 1]
    VS = S.edge_subgraph(vertical_edges)
    
    area = len(component)
    perimeter = nx.number_connected_components(HS) + nx.number_connected_components(VS)

    total_prize += area * perimeter

print(total_prize)