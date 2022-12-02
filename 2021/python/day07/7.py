import numpy as np

with open("day07\input.txt", "r") as f:
    lines = [int(val) for val in f.readline().split(',')]
    lines = np.array(lines)

sample = np.array([16,1,2,0,4,2,7,1,2,14])

def cost(goal_pos, data):

    goal = np.array([goal_pos for i in data])

    # cost function
    fuel = 0
    dist = abs(np.subtract(data, goal))
    # print(f'goal: {goal_pos}, dist: {dist}')

    for val in dist:
        fuel += sum(range(val+1))

    # print(f'sum {fuel}')
    return fuel

low = 999999999
lowest_goal = 999999999
for i in range(min(lines), max(lines)):
    res = cost(i, lines)
    # check value at goal = 2
    if i == 2:
        print(f'fuel at goal = 2: {res}')

    if res < low:
        low = res
        lowest_goal = i

print(f'fuel: {low}, goal: {lowest_goal}')

# sequence:
# n     1   2   3   4   5
# fuel  1   3   6   10  15  
# fuel = sum(1 to n)

# x = np.array([1,2,3])
# y = np.array([4,5,6])
# print(abs(np.subtract(x,y)))