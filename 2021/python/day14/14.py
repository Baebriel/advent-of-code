import collections

with open("day14\sample.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

original_template = lines[0]
data = lines[2:]

rules = dict()

for rule in data:
    left, right = rule.split(' -> ')
    rules[left] = right

# print(rules)

def step(template):
    result = []
    for i in range(len(template) - 1):
        # add first char to result
        # print('left: ' + template[i])
        result.append(template[i])

        # insert new char
        # print('new: ' + rules[template[i:i+2]])
        result.append(rules[template[i:i+2]])

        # print('---------------------')

    result.append(template[-1])
    return ''.join(result)

for i in range(10):
    original_template = step(original_template)
    # print(original_template)

most_common_freq = collections.Counter(original_template).most_common()[0][1]
# print(most_common_freq)
least_common_freq = collections.Counter(original_template).most_common()[-1][1]
# print(least_common_freq)
print(most_common_freq - least_common_freq)


### test ###
test = 'NCNBCHB'
# len(test) = 7
# freq B in test = 2

pair_freqs = {
    'NC': 1,
    'CN': 1,
    'NB': 1,
    'BC': 1,
    'CH': 1,
    'HB': 1,
}

# freq B in pair_freqs = 3