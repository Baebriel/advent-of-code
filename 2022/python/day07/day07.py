import pytest
from anytree import Node, PostOrderIter


def init_tree(input):

    node = Node(name='root',size=0,type='dir')
    root = node

    # iterate through input and populate tree
    for line in input.splitlines()[1:]:
        parts = line.split(' ')
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    node = node.parent
                else:
                    for child in node.children:
                        if child.name == parts[2]:
                            node = child
        else:
            if parts[0] == 'dir':
                Node(name=parts[1], parent=node, size=0, type='dir')
            else:
                Node(name=parts[1], parent=node, size=int(parts[0]), type='file')

    # populate directory sizes
    for node in PostOrderIter(root, filter_=lambda n: n.name != 'root'):
        node.parent.size += node.size

    return root


def process_part1(input):

    tree = init_tree(input)

    sizes = [node.size for node in PostOrderIter(tree, filter_=lambda n: n.type == 'dir' and n.size <= 100_000)]

    return sum(sizes)


def process_part2(input):

    tree = init_tree(input)

    sizes = sorted([node.size for node in PostOrderIter(tree, filter_=lambda n: n.type == 'dir')])

    for size in sizes:
        if size >= sizes[-1] - 40_000_000:
            return size


class TestExamples:

    @pytest.fixture
    def example_input(scope="class"):
        with open('./example.txt') as f:
            input = f.read()
        return input

    def test_part1(self,example_input):
        assert process_part1(example_input) == 95437

    def test_part2(self,example_input):
        assert process_part2(example_input) == 24933642


if __name__ == '__main__':

    with open('./input.txt') as f:
        input = f.read()

    print(f'Part 1: {process_part1(input)}')
    print(f'Part 2: {process_part2(input)}')