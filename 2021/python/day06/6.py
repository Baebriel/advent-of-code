import numpy as np

# parse input
with open("day06\input.txt", "r") as f:
    line = f.readlines()[0].split(',')
    fishes = [int(i) for i in line]

def count_fish(days):
    freq = np.zeros(9)

    for fish in fishes:
        freq[fish] += 1

    for _ in range(days):
        # move all by 1
        zeros = freq[0]
        freq = np.roll(freq, -1)
        freq[6] += zeros

    return sum(freq)

print(count_fish(80))
print(count_fish(256))