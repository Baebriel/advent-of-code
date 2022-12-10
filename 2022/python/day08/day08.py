import numpy as np
import pytest

def process_part1(map):
    
    # create same-sized ndarray for visibility flags, with edges visible already
    vis = np.zeros_like(map)
    vis[0,:] = 1
    vis[-1,:] = 1
    vis[:,0] = 1
    vis[:,-1] = 1
    
    # loop over entire input array
    it = np.nditer(map, flags=['multi_index'])
    for h in it:

        # if tree is already visible, continue to next tree in iterator
        if vis[it.multi_index]:
            continue

        # look left, right, up, down to determine visibility
        # left
        if (map[it.multi_index[0],:it.multi_index[1]] < h).all():
            vis[it.multi_index] = 1
            continue

        # right
        if (map[it.multi_index[0],it.multi_index[1]+1:] < h).all():
            vis[it.multi_index] = 1
            continue

        # up
        if (map.T[it.multi_index[1],:it.multi_index[0]] < h).all():
            vis[it.multi_index] = 1
            continue

        # down
        if (map.T[it.multi_index[1],it.multi_index[0]+1:] < h).all():
            vis[it.multi_index] = 1
            continue

    return np.sum(vis)


def process_part2(map):

    # create same-sized ndarray for scores with zero-score edges
    score = np.ones_like(map)
    score[0,:] = 0
    score[-1,:] = 0
    score[:,0] = 0
    score[:,-1] = 0

    # loop over entire input array
    it = np.nditer(map, flags=['multi_index'])
    for h in it:

        # skip edge trees
        if score[it.multi_index] == 0:
            continue

        # left
        score[it.multi_index] *= find_distance(np.flip(map[it.multi_index[0],:it.multi_index[1]]), h)

        # right
        score[it.multi_index] *= find_distance(map[it.multi_index[0],it.multi_index[1]+1:], h)

        # up
        score[it.multi_index] *= find_distance(np.flip(map.T[it.multi_index[1],:it.multi_index[0]]), h)

        # down
        score[it.multi_index] *= find_distance(map.T[it.multi_index[1],it.multi_index[0]+1:], h)

    return np.max(score)


def find_distance(trees,h):

    cnt = 0
    for tree in trees:
        cnt += 1
        if tree >= h:
            break

    return cnt


class TestExamples:

    @pytest.fixture
    def example_input(scope="class"):
        return np.genfromtxt('example.txt', delimiter=1)

    def test_part1(self,example_input):
        assert process_part1(example_input) == 21

    def test_part2(self,example_input):
        assert process_part2(example_input) == 8


if __name__ == '__main__':

    input = np.genfromtxt('input.txt', delimiter=1)

    print(f'Part 1: {process_part1(input)}')
    print(f'Part 2: {process_part2(input)}')