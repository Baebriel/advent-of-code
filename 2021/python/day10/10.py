import math

with open("day10\input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def opp(character):
    if character == '(':
        return ')'
    elif character == '[':
        return ']'
    elif character == '{':
        return '}'
    else:
        return '>'

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# part 1
score = 0
for data in lines:
    stack = []
    for char in data:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            if char == opp(stack[-1]):
                stack.pop()
            else:
                # line is corrupted
                score += scores[char]
                break

print(f'part 1: {score}')

# part 2
scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

incomplete_scores = []
for data in lines:
    corrupted = False
    stack = []
    for char in data:
        if char in ['(','[','{','<']:
            stack.append(char)
        else:
            if char == opp(stack[-1]):
                stack.pop()
            else:
                # line is corrupted
                corrupted = True
    
    if not corrupted:
        print(stack)
        score = 0
        for opening in reversed(stack):
            closing = opp(opening)
            score *= 5
            score += scores[closing]
        incomplete_scores.append(score)

incomplete_scores.sort()
print(incomplete_scores[math.floor(len(incomplete_scores)/2)])
