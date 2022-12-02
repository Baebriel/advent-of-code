import numpy as np
import plotly.graph_objs as go

def is_min(i,j):
    num = grid[i][j]
    cnt = 0
    max_y = grid.shape[0]
    max_x = grid.shape[1]

    if i != max_y - 1:
        if grid[i+1][j] > num:
            cnt += 1
    else:
        cnt += 1
    if i != 0:
        if grid[i-1][j] > num:
            cnt += 1
    else:
        cnt += 1
    if j != max_x - 1:
        if grid[i][j+1] > num:
            cnt += 1
    else:
        cnt += 1
    if j != 0:
        if grid[i][j-1] > num:
            cnt += 1
    else:
        cnt += 1

    if cnt == 4:
        return True
    else:
        return False


with open("day09\input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

grid = np.asarray(lines, dtype=int)

points = 0

### part 1 ###
low_points = []
for h in range(grid.shape[0]):
    for w in range(grid.shape[1]):
        if is_min(h,w):
            low_points.append((h,w))
            points += grid[h][w] + 1

print(f'points: {points}')

### part 2 ###

# use recursion to find basins
basin_sizes = []
# low_points = [(0,1), (0,9), (4,6), (2,2)]

def is_in_grid(i,j,grid):
    rtn = True
    if i < 0:
        rtn = False
    if j < 0:
        rtn = False
    if i > grid.shape[0] - 1:
        rtn = False
    if j > grid.shape[1] - 1:
        rtn = False
    return rtn


def dfs(i, j, visited):

    basin_size = 1

    
    # print((i,j))

    for m,n in [(i - 1, j) , (i + 1, j) , (i, j - 1) , (i, j + 1)]:
        # check if node is out of grid
        if is_in_grid(m,n,grid):
            if (m,n) not in visited:
                visited.append((m,n))
                if grid[m][n] != 9:
                    basin_size += dfs(m, n, visited)
    return basin_size

visited_nodes = []
for low in low_points:
    visited_nodes.append((low[0],low[1]))
    basin_sizes.append(dfs(low[0],low[1],visited_nodes))

basin_sizes.sort()
# print(f'sizes: {basin_sizes}')

print(basin_sizes)
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])