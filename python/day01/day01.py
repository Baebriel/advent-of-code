import itertools

filename = "input.txt"

with open(filename) as file:
    data = [int(line.strip() or 0) for line in file]

data = [ list(x[1]) for x in itertools.groupby(data, lambda x: x == 0) if not x[0] ]
acc = [ list(itertools.accumulate(sub))[-1] for sub in data]

acc.sort()

print(f'Part 1: {acc[-1]}')

print(f'Part 2: {sum(acc[-3:])}')