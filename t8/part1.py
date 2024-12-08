import itertools
import math

with open('input.txt', 'r') as f:
    grid = f.readlines()

h, w = len(grid), len(grid[0]) -1
print(h, w)
inside = lambda x: x[0] >= 0 and x[1] >= 0 and x[0] < w and x[1] < h

nodes = {}
for y in range(h):
    for x in range(w):
        e = grid[y][x]
        if e != '.':
            if e in nodes:
                nodes[e].append((x, y))
            else:
                nodes[e] = [(x,y)]

unique_antinodes = set()
for freq in nodes.values():
    for p1, p2 in itertools.combinations(freq, 2):
        dx, dy = p1[0] - p2[0], p1[1] - p2[1]

        a1 = (p1[0] + dx, p1[1] + dy)
        a2 = (p2[0] - dx, p2[1] - dy)

        if inside(a1):
            unique_antinodes.add(a1)
        if inside(a2):
            unique_antinodes.add(a2)

print(len(unique_antinodes))
