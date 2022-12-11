from dataclasses import dataclass, field
import operator
import pytest
from math import lcm

def process_part1(input):

    # init monkeys
    monkeys = Monkey.init_monkeys(input)

    # loop for each round
    rounds = 20
    for _ in range(rounds):
        for monkey in monkeys:
            for item in list(monkey.items):
                worry = monkey.operation(item, monkey.operand if monkey.operand != 'old' else item)
                worry = worry // 3

                if worry % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(worry)
                else:
                    monkeys[monkey.false_monkey].items.append(worry)

                monkey.inspected += 1
                monkey.items.remove(item)

    monkeys.sort(key=lambda x: x.inspected)
    return monkeys[-1].inspected * monkeys[-2].inspected


def process_part2(input):

    # init monkeys
    monkeys = Monkey.init_monkeys(input)

    # find lowest common monkey multiple
    lcmm = lcm(*[monkey.divisible_by for monkey in monkeys])

    # loop for each round
    rounds = 10000
    for _ in range(rounds):
        for monkey in monkeys:
            for item in list(monkey.items):
                worry = monkey.operation(item, monkey.operand if monkey.operand != 'old' else item)
                worry %= lcmm

                if worry % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(worry)
                else:
                    monkeys[monkey.false_monkey].items.append(worry)

                monkey.inspected += 1
                monkey.items.remove(item)

    monkeys.sort(key=lambda x: x.inspected)
    return monkeys[-1].inspected * monkeys[-2].inspected


@dataclass
class Monkey:
    items: "list[int]" = field(default_factory=list)
    operation: operator = operator.add
    operand: int = 0
    divisible_by: int = 0
    true_monkey: int = 0
    false_monkey: int = 0
    inspected: int = 0

    def init_monkeys(input):

        # create empty array to items for each monkey
        n_monkeys = len(input.split('\n\n'))
        monkeys = []
        for _ in range(n_monkeys):
            monkeys.append(Monkey())

        for ind, monkey_input in enumerate(input.split('\n\n')):
            lines = [line for line in monkey_input.splitlines()]

            # parse starting items
            monkeys[ind].items = [int(item.strip()) for item in lines[1].replace('  Starting items: ', '').split(',')]

            # parse operation
            ops = {'+' : operator.add, '*' : operator.mul}
            op_line = lines[2].replace('  Operation: new = old ', '')
            monkeys[ind].operation = ops[op_line[0]]

            try:
                monkeys[ind].operand = int(op_line[1:].strip())
            except:
                monkeys[ind].operand = 'old'

            # parse divisible by
            monkeys[ind].divisible_by = int(lines[3].replace('  Test: divisible by ', '').strip())

            # parse monkeys to which items are thrown
            monkeys[ind].true_monkey = int(lines[4][-1])
            monkeys[ind].false_monkey = int(lines[5][-1])

        return monkeys


class TestExamples:

    @pytest.fixture
    def example_input(scope="class"):
        with open('./example.txt') as f:
            input = f.read()
        return input

    def test_part1(self,example_input):
        assert process_part1(example_input) == 10605

    def test_part2(self,example_input):
        assert process_part2(example_input) == 2713310158


if __name__ == '__main__':

    with open('./input.txt') as f:
        input = f.read()

    print(f'Part 1: {process_part1(input)}')
    print(f'Part 2: {process_part2(input)}')