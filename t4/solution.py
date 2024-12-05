path = "input.txt"
with open(path, 'r') as f:
    grid = f.readlines()

h, w = len(grid), len(grid[0]) - 1
print(f"Grid dimensioins: W = {w}, H = {h}")

l = len("XMAS")

"""
Cases:
- horizontal forward            H_FW    H
- horizontal backward           H_BW    
- vertical up-down              V_UD    V
- vertical down-up              V_DU
- diagonal left-rigth up-down   D_LR_UD D_LR
- diagonal left-rigth down-up   D_LR_DU
- diagonal right-left up-down   D_RL_UD D_RL
- diagonal right-left down-up   D_RL_DU
"""

acc = 0

# H
for y in range(h):
    for x in range(w):
        seq = grid[y][x:x+4]
        if seq == "XMAS" or seq == "XMAS"[::-1]:
            acc += 1

# V
for y in range(h - l + 1):
    for x in range(w):
        seq = "".join([grid[y+i][x] for i in range(l)])
        if seq == "XMAS" or seq == "XMAS"[::-1]:
            acc += 1

# # DLR
for y in range(h - l + 1):
    for x in range(w - l + 1):
        seq = "".join([grid[y+i][x+i] for i in range(l)])
        if seq == "XMAS" or seq == "XMAS"[::-1]:
            acc += 1

# # DLR
for y in range(l - 1, h):
    for x in range(w - l + 1):
        seq = "".join([grid[y-i][x+i] for i in range(l)])
        if seq == "XMAS" or seq == "XMAS"[::-1]:
            acc += 1

print(acc)



