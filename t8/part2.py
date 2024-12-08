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
    if len(freq) > 2:
        for a in freq:
            unique_antinodes.add(a)
    for p1, p2 in itertools.combinations(freq, 2):
        dx, dy = p1[0] - p2[0], p1[1] - p2[1]
        n = math.gcd(dx, dy)
        dx, dy = dx // n, dy // n
        
        outside = False
        c = 1
        while not outside:
            a = (p1[0] + c * dx, p1[1] + c * dy)
            outside = not inside(a)
            if not outside:
                unique_antinodes.add(a)
            c += 1

        outside = False
        c = 1
        while not outside:
            a = (p2[0] - c * dx, p2[1] - c * dy)
            outside = not inside(a)
            if not outside:
                unique_antinodes.add(a)
            c += 1

print(len(unique_antinodes))
