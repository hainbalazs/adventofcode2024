import numpy as np

with open('input.txt', 'r') as f:
    input_lines = f.readlines()
grid = [[int(n) for n in line.strip()] for line in input_lines]

def inside(p, h, w):
    return p[0] >= 0 and p[1] >= 0 and p[0] < w and p[1] < h

def vadd(p, v):
    return (p[0] + v[0], p[1] + v[1])

def g(G, p):
    return G[p[1]][p[0]]

def f(x, y, w):
    return y*w + x

def approach_dp(grid):
    h, w = len(grid), len(grid[0])
    nine_coords = [(x,y) for x in range(w) for y in range(h) if g(grid, (x,y)) == 9]
    zero_coords = [(x,y) for x in range(w) for y in range(h) if g(grid, (x,y)) == 0]
    nine_ids = {p: i for i, p in enumerate(nine_coords)}
    
    dp = {}
    for n in range(0, 9)[::-1]:
        for y in range(h):
            for x in range(w):
                candidates = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
                for c in candidates:
                    if inside(c, h, w) and g(grid, (x,y)) == n and g(grid, c) == n+1:
                        if n == 8:
                            if (x,y) in dp:
                                dp[(x,y)].add(nine_ids[c])
                            else:
                                dp[(x,y)] = {nine_ids[c]}
                        else:
                            if c in dp:
                                if (x,y) in dp:
                                    dp[(x,y)].update(dp[c])
                                else:
                                    dp[(x,y)] = set(dp[c])

                if (x,y) not in dp:
                    dp[(x,y)] = set()

    acc = 0
    for zc in zero_coords:
        acc += len(dp[zc])
    
    return acc


def approach_adjexp(grid):
    h, w = len(grid), len(grid[0])

    # building the adjacency matrix
    flat_grid = [y*w + x for x in range(w) for y in range(h)]
    adj_mx = [[0 for p1 in flat_grid] for p2 in flat_grid]
    for y in range(h):
        for x in range(w):
            candidates = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
            for c in candidates:
                if inside(c, h, w) and g(grid, c) == g(grid, (x,y)) + 1:
                    adj_mx[f(x, y, w)][f(*c, w)] = 1


    return np.linalg.matrix_power(np.array(adj_mx, dtype=bool), 9).sum()




x = approach_dp(grid)
print(x)

# elapsed_time = timeit.timeit(lambda: approach_dp(grid), number=1)
# print(f"Elapsed time with DP: {elapsed_time:.6f} seconds")

# elapsed_time = timeit.timeit(lambda: approach_adjexp(grid), number=1)
# print(f"Elapsed time with Adjacency Matrix: {elapsed_time:.6f} seconds")
