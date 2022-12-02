import numpy as np
test = __import__('11')

data = test.get_input('sample')
print(data)

def neighbours(grid, loc):
    h,w = grid.shape
    i,j = loc

    possible_nbs = [(i,j-1),(i,j+1),(i-1,j),(i+1,j),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
    actual_nbs = []

    for nb in possible_nbs:
        if nb[0] < 0 or nb[1] < 0 or nb[0] > h - 1 or nb[1] > w - 1: continue
        else: actual_nbs.append(nb)

    return actual_nbs

