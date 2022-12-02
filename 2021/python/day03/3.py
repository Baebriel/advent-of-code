### part 1 ###

with open('day03\input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

gamma = []
# iterate over bits
for i in range(len(lines[0])):
    # iterate over nums
    ones = 0
    for num in lines:
        # count ones in num position
        if int(num[i]) == 1:
            ones += 1
    if ones > int(int(len(lines))/2):
        gamma.append('1')
    else:
        gamma.append('0')

gamma = ''.join(gamma)
epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

print(int(gamma,2) * int(epsilon,2))

### part 2 ###

# lines = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

ogr = lines
ones = 0

# OGR
for i in range(len(ogr[0])):
    # get most common bit in position
    ones = 0
    for num in ogr:
        if num[i] == '1':
            ones += 1
    if ones >= len(ogr) - ones:
        most_common = '1'
    else:
        most_common = '0'

    ogr = [val for val in ogr if val[i] == most_common]

co2 = lines

# CO2
for i in range(len(co2[0])):
    # get most common bit in position
    ones = 0
    for num in co2:
        if num[i] == '1':
            ones += 1
    if ones >= len(co2) - ones:
        least_common = '0'
    else:
        least_common = '1'

    co2 = [val for val in co2 if val[i] == least_common]

    if len(co2) == 1:
        break

print(int(ogr[0],2) * int(co2[0],2))