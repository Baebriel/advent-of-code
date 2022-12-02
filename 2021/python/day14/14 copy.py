import collections

def sol(original_template, steps):

    # setup counts dict
    counts = dict()
    # count frequency of atoms
    for char in original_template:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    # count frequency of pairs
    for i in range(len(original_template) - 1):
        if original_template[i:i+2] in counts:
            counts[original_template[i:i+2]] += 1
        else:
            counts[original_template[i:i+2]] = 1
    
    print(f'original counts: {counts}')

    # call steps function
    for i in range(steps):
        counts = step(counts)

    # get diff between max and min
    maxx = 0
    minn = 999999999999999999
    length = 0
    for keyy, vall in counts.items():
        if len(keyy) == 1 and counts[keyy] > maxx:
            maxx = counts[keyy]
        elif len(keyy) == 1 and counts[keyy] < minn and counts[keyy] != 0:
            minn = counts[keyy]
        if len(keyy) == 1:
            length += counts[keyy]

    print(f'counts: {counts}')
    print(f'max: {maxx},  min: {minn}')
    print(f'length: {length} after {steps} steps')
    return maxx - minn


def step(counts):
    new_counts = counts.copy()
    for key, val in counts.items():
        if len(key) == 2 and counts[key] > 0:
            # update pairs, ex: 'NN' -> 'NC'++, 'CN'++, 'NN'--
            new_left = key[0] + rules[key]
            new_right = rules[key] + key[1]

            print(f'{key} turns into {key[0] + rules[key] + key[1]} * {counts[key]}')

            if new_left in new_counts:
                new_counts[new_left] += counts[key]
            else:
                new_counts[new_left] = counts[key]
            if new_right in new_counts:
                new_counts[new_right] += counts[key]
            else:
                new_counts[new_right] = counts[key]

            # update atoms, ex: 'NN' -> 'C'++
            if rules[key] in new_counts:
                new_counts[rules[key]] += counts[key]
            else:
                new_counts[rules[key]] = counts[key]

            new_counts[key] = 0

    print('----------------')
    return new_counts
    
if __name__ == "__main__":
    with open("day14\sample.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    original_template = lines[0]
    data = lines[2:]
    rules = dict()

    for rule in data:
        left, right = rule.split(' -> ')
        rules[left] = right

    num_steps = 10
    diff = sol(original_template, num_steps)
    print(f'diff: {diff}')