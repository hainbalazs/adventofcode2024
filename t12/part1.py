import networkx as nx

with open('input.txt', 'r') as f:
    input_lines = f.readlines()

H, W = len(input_lines), len(input_lines[0]) - 1
is_in = lambda c, h, w: c[0] >= 0 and c[1] >= 0 and c[0] < h and c[1] < w
label = lambda grid, x: grid[x[1]][x[0]]
flat_index = lambda c, w: c[1] * w + c[0]

# undirected graph with no parallel edges allowed
G = nx.Graph()
for y in range(H):
    for x in range(W):
        p = (x,y)
        G.add_node(flat_index(p, W))

        candidates = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        for c in candidates:
            if is_in(c, H, W) and label(input_lines, p) == label(input_lines, c):
                G.add_edge(flat_index(p, W), flat_index(c, W))
                
total_price = 0
for component in nx.connected_components(G):
    area = len(component)
    perimeter = 0

    #print(component)
    #print(G.degree(list(component)))
    for node in component:
        degree = G.degree[node]
        if degree < 4:
            # touching another region with 0 < s <= 4 sides
            perimeter += 4 - degree

    #print(area, perimeter, area*perimeter)
    total_price += area * perimeter

print(total_price)