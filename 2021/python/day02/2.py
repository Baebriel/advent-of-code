### part 1 ###

with open('day02\input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# split lines into direction and magnitude
vecs = []
for line in lines:
    direction, mag = (line.split()[0],int(line.split()[1]))
    vecs.append((direction, mag))

# step through path
x1 = 0
y1 = 0
for vect in vecs:
    if vect[0] == 'forward':
        x1 += vect[1]
    elif vect[0] == 'up':
        y1 -= vect[1]
    elif vect[0] == 'down':
        y1 += vect[1]

# print result
print(x1 * y1)

### part 2 ###
x2 = 0
y2 = 0
aim = 0

for vect in vecs:
    if vect[0] == 'forward':
        x2 += vect[1]
        y2 += aim * vect[1]
    elif vect[0] == 'up':
        aim -= vect[1]
    elif vect[0] == 'down':
        aim += vect[1]

# print result
print(x2 * y2)