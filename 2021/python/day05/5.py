import numpy as np
from operator import itemgetter

def sol(data):
    # parse data
    with open(f"day05\{data}.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        segments = []
        for line in lines:
            # print(line)
            first, second = line.split(' -> ')[0], line.split(' -> ')[1]
            segments.append( ( int(first.split(',')[0]), int(first.split(',')[1]), int(second.split(',')[0]), int(second.split(',')[1]) ) )

    # get max for grid dimesions
    size = 0
    for seg in segments:
        if max(seg) > size:
            size = max(seg)

    # create grid
    grid = np.zeros((size + 1, size + 1))

    # populate segments on grid
    # two cases: vertical and horizontal lines
    diag = []
    for seg in segments:
        if seg[1] == seg[3]:    # y1 == y2, horz
            if seg[0] < seg[2]:
                for i in range(seg[0], seg[2] + 1):
                    grid[i, seg[1]] += 1
            else:
                for i in range(seg[2], seg[0] + 1):
                    grid[i, seg[1]] += 1

        elif seg[0] == seg[2]:  # x1 == x2, vert
            if seg[1] < seg[3]:
                for i in range(seg[1], seg[3] + 1):
                    grid[seg[0], i] += 1
            else:
                for i in range(seg[3], seg[1] + 1):
                    grid[seg[0], i] += 1

        else:                   # diag
            diag.append(seg)

    # add diagonal lines
    for seg in diag:
        # if y2 > y1 and x2 > x1, goes up right
        if seg[3] > seg[1] and seg[2] > seg[0]:
            for i in range(abs(seg[2] - seg[0]) + 1):
                grid[seg[0] + i, seg[1] + i] += 1
        # else y2 > y1 and x2 < x1, goes up left
        elif seg[3] > seg[1] and seg[2] < seg[0]:
            for i in range(abs(seg[2] - seg[0]) + 1):
                grid[seg[0] - i, seg[1] + i] += 1
        # y2 < y1 and x2 < x1, goes down left
        elif seg[3] < seg[1] and seg[2] < seg[0]:
            for i in range(abs(seg[2] - seg[0]) + 1):
                grid[seg[0] - i, seg[1] - i] += 1
        # y2 < y1 and x2 > x1
        else:
            for i in range(abs(seg[2] - seg[0]) + 1):
                grid[seg[0] + i, seg[1] - i] += 1



    print(grid)
    # print(diag)

    # count non-zeros
    return grid.size - (grid < 2).sum()


if __name__ == "__main__":
    print(sol('input'))
