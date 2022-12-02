import numpy as np

# define function to read input
# return: numpy grid of input
def get_input(inputname):
    with open(f"day11\{inputname}.txt", "r") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    return np.asarray(lines, dtype=int)

# define function to get neighbours
# params: grid, location (x, y)
def neighbours(grid, loc):
    h,w = grid.shape
    i,j = loc

    possible_nbs = [(i,j-1),(i,j+1),(i-1,j),(i+1,j),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    actual_nbs = []

    for nb in possible_nbs:
        if nb[0] < 0 or nb[1] < 0 or nb[0] > h - 1 or nb[1] > w - 1: continue
        else: actual_nbs.append(nb)

    return actual_nbs


# define function for a single step
# params: grid, location, list of locations having flashed, previous flash count
# return: grid, updated flashed list, updated flash count
# def step(grid, loc, flashed, flashes):
#     print(grid)

#     # check if loc is greater than 9
#     if grid[loc] > 9 and loc not in flashed:
#         # print('flashing loc')
#         flashed.add(loc)
#         flashes += 1
#         for flashed_nb in neighbours(grid,loc):
#             grid[flashed_nb] += 1

#     # check if any neighbours are greater than 9
#     for nb in neighbours(grid, loc):
#         if grid[nb] > 9 and nb not in flashed:
#             # print('flashing nb')
#             flashed.add(nb)
#             flashes += 1
#             for flashed_nb_nb in neighbours(grid,nb):
#                 grid[flashed_nb_nb] += 1
#             grid, flashed, flashes = step(grid, nb, flashed, flashes)

#     # print(flashed)
#     return grid, flashed, flashes



if __name__ == "__main__":
    # get input
    data = get_input('sample')

    # run through 100 steps
    total_flashes = 0
    for i in range(3):
        # increase energy level of all octopi by 1
        data += 1

        while True:
            flashed = set()
            for ii in range(data.shape[0]):
                for jj in range(data.shape[1]):
                    if data[(ii,jj)] == 10:
                        flashed.add((ii,jj))


                    if data[(ii,jj)] > 9 and (ii,jj) not in flashed:
                        finished = False
                        flashed.add((ii,jj))
                        for neighbour in neighbours(data, (ii,jj)):
                            data[neighbour] += 1
                            total_flashes += len(flashed)
                            

            for loc in flashed:
                data[loc] = 0

        print(flashed)
        print(data)
        print('-----------')

    print(f'total flashes: {total_flashes}')

    
