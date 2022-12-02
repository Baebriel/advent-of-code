### part 1 ###

with open('day01\input.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]

cnt1 = 0

for i in range(len(lines)-1):
    if lines[i+1] > lines[i]:
        
        cnt1 += 1

print(cnt1)

### part 2 ###
cnt2 = 0
cur_sum = 0
prev_sum = lines[0] + lines[1] + lines[2]

for i in range(len(lines)-2):
    cur_sum = lines[i] + lines[i+1] + lines[i+2]
    
    if cur_sum > prev_sum:
        cnt2 += 1

    prev_sum = cur_sum

print(cnt2)