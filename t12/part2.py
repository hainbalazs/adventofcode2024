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

        candidates = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        for c in candidates:
            if is_in(c, H, W) and label(T, p) == label(T, c):
                G.add_edge(flat_index(p, W), flat_index(c, W))
                
components = {
    i : c for i, c in enumerate(nx.connected_components(G))
}

component_sides = {
    k: 0 for k in list(components.keys())
}
component_sides[-1] = 0

def find_region(x, y):
    if x == -1 and y == -1:
        return -1
    
    for r, comp in components.items():
        if flat_index((x,y), W) in comp:
            return r
    
    return -1

def logic(prev1, prev2, prev1_idx, prev2_idx, curr1, curr2, acc):
    if curr1 != curr2:
        # only care for region boundaries
        if curr1 != prev1 and prev1 != None and prev1 != prev2:
            acc[find_region(*prev1_idx)] += 1
            
        if curr2 != prev2 and prev2 != None and prev1 != prev2:
            acc[find_region(*prev2_idx)] += 1

    else:
        if prev1 != None and prev1 != prev2:
            acc[find_region(*prev1_idx)] += 1
        if prev2 != None and prev1 != prev2:
            acc[find_region(*prev2_idx)] += 1


    prev1 = curr1
    prev2 = curr2

    return prev1, prev2

# horizontal lines
for y in range(H-1):
    prev_top_idx, prev_bottom_idx = None, None
    prev_top, prev_bottom = None, None
    for x in range(W):
        top, bottom = label(T, (x,y)), label(T, (x, y+1))
        prev_top, prev_bottom = logic(prev_top, prev_bottom, prev_top_idx, prev_bottom_idx, top, bottom, component_sides)
        prev_top_idx, prev_bottom_idx = (x,y), (x,y+1)
    if prev_top != prev_bottom:
        component_sides[find_region(*prev_top_idx)] += 1
        component_sides[find_region(*prev_bottom_idx)] += 1

# top and bottom edges
y = 0
prev_top, prev_bottom = 'OUTSIDE', None
top = 'OUTSIDE'
for x in range(W):
    bottom = label(T, (x,y))
    prev_top, prev_bottom = logic(prev_top, prev_bottom, prev_top_idx, prev_bottom_idx, top, bottom, component_sides)
    prev_top_idx, prev_bottom_idx = (-1, -1), (x,y)
component_sides[find_region(*prev_bottom_idx)] += 1

y = H-1
prev_top, prev_bottom = None, 'OUTSIDE'
bottom = 'OUTSIDE'
for x in range(W):
    top = label(T, (x,y))
    prev_top, prev_bottom = logic(prev_top, prev_bottom, prev_top_idx, prev_bottom_idx, top, bottom, component_sides)
    prev_top_idx, prev_bottom_idx = (x,y), (-1, -1)
component_sides[find_region(*prev_top_idx)] += 1

# vertical lines
for x in range(W-1):
    prev_left_idx, prev_right_idx = None, None
    prev_left, prev_right = None, None
    for y in range(H):
        left, right = label(T, (x,y)), label(T, (x+1, y))
        prev_left, prev_right = logic(prev_left, prev_right,prev_left_idx, prev_right_idx, left, right, component_sides)
        prev_left_idx, prev_right_idx = (x,y), (x+1,y)
    if prev_left != prev_right:
        component_sides[find_region(*prev_left_idx)] += 1
        component_sides[find_region(*prev_right_idx)] += 1

x = 0
prev_left, prev_right = 'OUTSIDE', None
left = 'OUTSIDE'
for y in range(H):
    right = label(T, (x,y))
    prev_left, prev_right = logic(prev_left, prev_right, prev_left_idx, prev_right_idx, left, right, component_sides)
    prev_left_idx, prev_right_idx = (-1, -1), (x,y)
component_sides[find_region(*prev_right_idx)] += 1

x = W-1
prev_left, prev_right = None, 'OUTSIDE'
right = 'OUTSIDE'
for y in range(H):
    left = label(T, (x,y))
    prev_left, prev_right = logic(prev_left, prev_right, prev_left_idx, prev_right_idx, left, right, component_sides)
    prev_left_idx, prev_right_idx = (x,y), (-1, -1)
component_sides[find_region(*prev_left_idx)] += 1

total_prize = 0
for label in list(components.keys()):
    area = len(components[label])
    perimeter = component_sides[label]

    total_prize += area * perimeter

print(total_prize)