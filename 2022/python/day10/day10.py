import pytest


def process_part1(input):

    register = 1
    cycle = 0
    strengths = []

    for line in input.splitlines():
        parts = line.split(' ')
        if parts[0] == "noop":
            cycle += 1

            strengths = add_strength(cycle, register, strengths)

        else:
            cycle += 1

            strengths = add_strength(cycle, register, strengths)

            cycle += 1

            strengths = add_strength(cycle, register, strengths)

            register += int(parts[1])

    return sum(strengths)


def add_strength(cycle, register, strengths):
    if (cycle - 20) % 40 == 0:
        strengths.append(register * cycle)
    return strengths


def process_part2(input):

    register = 1
    cycle = 0
    rows = ""

    for ind, line in enumerate(input.splitlines()):

        parts = line.split(' ')
        if parts[0] == "noop":
            cycle += 1

            rows = print_crt(cycle, register, rows)

        else:
            cycle += 1

            rows = print_crt(cycle, register, rows)

            cycle += 1

            rows = print_crt(cycle, register, rows)

            register += int(parts[1])

    return rows


def print_crt(cycle, register, rows):

    # begin new row
    if len(rows.split("\n")[-1]) == 40:
        rows += "\n"

    # check if sprite overlaps register
    if abs(len(rows.split("\n")[-1]) - register) <= 1:
        rows += "#"
    else:
        rows += "."

    return rows


class TestExamples:

    @pytest.fixture(scope="class")
    def example_input(self):
        with open('./example.txt') as f:
            input = f.read()
        return input

    def test_part1(self, example_input):
        assert process_part1(example_input) == 13140

    def test_part2(self, example_input):
        with open('./example_output.txt') as f:
            example_output = f.read()
        assert process_part2(example_input) == example_output


if __name__ == '__main__':

    with open('./input.txt') as f:
        input = f.read()

    print(f'Part 1: {process_part1(input)}')
    print(f'Part 2: \n\n{process_part2(input)}')
