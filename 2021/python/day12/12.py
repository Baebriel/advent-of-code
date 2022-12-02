from collections import defaultdict

with open("day12\input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

graph = defaultdict(set)

for line in lines:
    a,b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

def findPaths(cur, visited, path, twice):
    visited.append(cur)
    path.append(cur)

    count = 0
    if cur == 'end':
        # print(path)
        count += 1
    else:
        for node in graph[cur]:
            if node not in visited or node.isupper():
                count += findPaths(node, visited, path, twice)
            elif node != 'start' and twice:
                count += findPaths(node, visited, path, False)

    path.pop()
    visited.pop()

    return count

n_paths = findPaths('start', [], [], False)
print(n_paths)

n_paths = findPaths('start', [], [], True)
print(n_paths)