import pytest
from dataclasses import dataclass
import contextlib


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def get_move(h, t):
        """Returns the magnitudes by which to move the tail to keep up with the head."""

        # check if two steps away in x direction
        if abs(h.x - t.x) == 2 and h.y == t.y:
            return ((h.x - t.x)/abs(h.x - t.x), 0)

        # check if two steps away in y direction
        if abs(h.y - t.y) == 2 and h.x == t.x:
            return (0, (h.y - t.y)/abs(h.y - t.y))

        # check if not in same row or column
        if (h.x != t.x and h.y != t.y) and (abs(h.x - t.x) == 2 or abs(h.y - t.y) == 2):
            return ((h.x - t.x)/abs(h.x - t.x), (h.y - t.y)/abs(h.y - t.y))

        return (0, 0)


def process_part1(input):

    head = Point()
    tail = Point()

    dirs = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    visited = set()
    visited.add((0, 0))

    for line in input.splitlines():
        dir, steps = line.split(' ')
        dir = dirs[dir]

        for _ in range(int(steps)):

            head.x += dir[0]
            head.y += dir[1]

            tail_move = Point.get_move(head, tail)

            tail.x += tail_move[0]
            tail.y += tail_move[1]

            visited.add((tail.x, tail.y))

    return len(visited)


def process_part2(input):

    knots = []
    for _ in range(10):
        knots.append(Point())

    dirs = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    visited = set()
    visited.add((0, 0))

    for line in input.splitlines():
        dir, steps = line.split(' ')
        dir = dirs[dir]

        for _ in range(int(steps)):

            # move head
            knots[0].x += dir[0]
            knots[0].y += dir[1]

            for i in range(9):
                move = Point.get_move(knots[i], knots[i+1])

                knots[i+1].x += move[0]
                knots[i+1].y += move[1]

            visited.add((knots[9].x, knots[9].y))

    return len(visited)


class TestExamples:

    def test_part1(self):

        with open('./example.txt') as f:
            input = f.read()

        assert process_part1(input) == 13

    def test_part2(self):

        with open('./example2.txt') as f:
            input = f.read()

        assert process_part2(input) == 36


if __name__ == '__main__':

    with open('./input.txt') as f:
        input = f.read()

    with contextlib.redirect_stdout(None):
        part1 = process_part1(input)
        part2 = process_part2(input)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
