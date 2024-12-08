with open('input_mini.txt') as f:
    grid = f.readlines()

def num_visited_fields(table):
    return sum(sum(row) for row in table)

def all_visited(table):
    return all(all(row) for row in table)

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == '^':
            guard_pos = (x, y)
            initial_guard_pos = (x, y)
            break

H, W = len(grid), len(grid[0]) - 1
print(H, W, guard_pos)
visited = [[False for w in range(W)] for h in range(H)]
visited[guard_pos[1]][guard_pos[0]] = True
direction = (0,-1)

def rotate(direction, step=1):
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    i = dirs.index(direction)
    return dirs[(i+step)%4]

def step(g, direction, obstacles, verbose=False):
    new_dirs = [rotate(direction, step) for step in range(4)]
    new_poss = [(g[0] + dx, g[1] + dy) for dx, dy in new_dirs]
    
    for i in range(4):
        newx, newy = new_poss[i]

        if newx >= W or newy >= H or newx < 0 or newy < 0:
            if verbose:
                print(f'Stepped outside the grid at: {newx, newy}')
            return True, (newx, newy), new_dirs[i]
        elif grid[newy][newx] == '#':
            if verbose:
                print(f"Turned at {newx, newy}")
            obstacles.append((newx, newy))
            continue
        else:
            if verbose:
                print(f'Moved forward at position: {newx, newy}, direction: {new_dirs[i]}')
            return False, (newx, newy), new_dirs[i]
        
    
    print("After taking 4 turns, there are no possible moves.")
    print("Guard position: ", g)
    for i in range(4):
        print(f"Lookahead after moving to direction {new_dirs[i]}: {grid[new_poss[i]][new_poss[i]]}")
    assert("Stuck.")
    
finished = False
obstacles = []
while(not finished and not all_visited(visited)):
    finished, guard_pos, direction = step(guard_pos, direction, obstacles, verbose=False)
    if not finished:
        visited[guard_pos[1]][guard_pos[0]] = True

print(num_visited_fields(visited))