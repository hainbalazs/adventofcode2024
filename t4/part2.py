path = "input.txt"
with open(path, 'r') as f:
    grid = f.readlines()

h, w = len(grid), len(grid[0]) - 1
print(f"Grid dimensioins: W = {w}, H = {h}")

b = 3
acc = 0

# go over each 3x3 boxes in the grid and check the diagonals
for y in range(h- b + 1):
    for x in range(w - b + 1):
        d1 = "".join([grid[y+i][x+i] for i in range(b)])
        d2 = "".join([grid[y+b-i-1][x+i] for i in range(b)])
        if (d1 == "MAS" or d1 == "MAS"[::-1]) and (d2 == "MAS" or d2 == "MAS"[::-1]):
            acc += 1

print(acc)
