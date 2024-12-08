with open('input.txt') as f:
    grid = f.readlines()

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == '^':
            guard_pos = (x, y)
            initial_guard_pos = (x, y)
            break

H, W = len(grid), len(grid[0]) - 1

def rotate(direction, step=1):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    i = dirs.index(direction)
    return dirs[(i + step) % 4]

def step(g, direction, obstacles, grid):
    new_dirs = [rotate(direction, step) for step in range(4)]
    new_poss = [(g[0] + dx, g[1] + dy) for dx, dy in new_dirs]

    for i in range(4):
        newx, newy = new_poss[i]
        if newx >= W or newy >= H or newx < 0 or newy < 0:
            return True, (newx, newy), new_dirs[i]
        elif (newx, newy) in obstacles or grid[newy][newx] == '#':
            continue
        else:
            return False, (newx, newy), new_dirs[i]

    return True, g, direction  # If no moves are possible

def simulate_with_obstruction(grid, obstruction):
    visited_states = set()
    guard_pos = initial_guard_pos
    direction = (0, -1)
    obstacles = [obstruction] if obstruction else []

    while True:
        # Track the guards current poistion and direction. If the guards steps onto path facing the same direction that was visited before = loop.
        state = (guard_pos, direction)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        finished, guard_pos, direction = step(guard_pos, direction, obstacles, grid)
        if finished:
            return False  # Guard exited the grid

valid_positions = []
for y in range(H):
    for x in range(W):
        if grid[y][x] == '.' and (x, y) != initial_guard_pos:  # Exclude guard's start
            if simulate_with_obstruction(grid, (x, y)):
                valid_positions.append((x, y))

    print(f"finished {y}/{H}")

print(f"Number of valid positions: {len(valid_positions)}")
