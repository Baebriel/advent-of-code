def get_uniques(data):
    with open(f"day08\{data}.txt", "r") as f:
        lines = f.readlines()

    # count 1, 4, 7, 8 occurences
    uniques = 0
    for line in lines:
        words = line.split()
        for word in words[-4:]:
            if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
                uniques += 1

    print(uniques)

def decode(line):

    zero, one, two, three, four, five, six, seven, eight, nine = (set() for i in range(10))

    patterns = line.split('|')[0].split()
    output = line.split('|')[1].split()

    decoded_output = output
    decoded_patterns = patterns

    # find uniques in output
    for i in range(len(decoded_output)):
        if len(decoded_output[i]) == 2:
            decoded_output[i] = 1
        elif len(decoded_output[i]) == 3:
            decoded_output[i] = 7
        elif len(decoded_output[i]) == 4:
            decoded_output[i] = 4
        elif len(decoded_output[i]) == 7:
            decoded_output[i] = 8
    
    # print(f'decoded output: {decoded_output}')

    # find uniques in sample patterns and add letters to number sets
    for word in line.split():
        if len(word) == 2:
            one = one | set(word)
        elif len(word) == 3:
            seven = seven | set(word)
        elif len(word) == 4:
            four = four | set(word)
        elif len(word) == 7:
            eight = eight | set(word)

    # find top segment from union of seven and one
    top = seven - one
    # print(f'top segment: {top}')

    # find nine by comparing patterns to intersection of top and four
    for word in patterns:
        if len(word) == 6 and len(set(word) - four - top) == 1:
            # print(word)
            nine = set(word)

    # print(f'nine: {nine}')

    # check if nine is in output
    for j in range(len(decoded_output)):
        # print(decoded_output[j])
        if type(decoded_output[j]) == str and set(decoded_output[j]) == nine:
            # print('nine found')
            decoded_output[j] = 9

    # find bottom left segment from subtraction of nine from eight
    bottom_left = eight - nine
    # print(f'bottom left: {bottom_left}')

    # print(f'decoded output: {decoded_output}')

    # can find five and six because they only differ by the bottom left segment
    # however, eight and nine also differe by bottom left so ignore those
    for word in patterns:
        if set(word) == eight or set(word) == nine:
            continue
        for word2 in patterns:
            if set(word2) == eight or set(word2) == nine:
                continue
            if len(word2) == 6 and set(word2) - set(word) == bottom_left:
                six = set(word2)
                five = set(word)
                # print(f'five: {five}')
                # print(f'six: {six}')

    # check if five is in output
    for k in range(len(decoded_output)):
        # print(decoded_output[k])
        if type(decoded_output[k]) == str and set(decoded_output[k]) == five:
            decoded_output[k] = 5
    
    # check if six is in output
    for m in range(len(decoded_output)):
        # print(decoded_output[m])
        if type(decoded_output[m]) == str and set(decoded_output[m]) == six:
            decoded_output[m] = 6

    # print(f'decoded output: {decoded_output}')

    # left to find: two, three, zero
    # find zero: diff between zero and eight is size 1
    for word in patterns:
        if len(word) == 6 and len(eight - set(word)) == 1 and set(word) != five and set(word) != six and set(word) != nine:
            zero = set(word)
            # print(f'zero: {zero}')

    # only two and three remain, two has bottom_left
    for word in patterns:
        if set(word) != zero and set(word) != one and set(word) != four and set(word) != five and set(word) != six and set(word) != seven and set(word) != eight and set(word) != nine:
            if bottom_left.issubset(set(word)):
                # print('found two')
                two = set(word)
            else:
                # print('found three')
                three = set(word)

    # print(f'zero: {zero}, one: {one}, two: {two}, three: {three}, four: {four}, five: {five}, six: {six}, seven: {seven}, eight: {eight}, nine: {nine}')

    for n in range(len(decoded_output)):
        if type(decoded_output[n]) == str and set(decoded_output[n]) == zero:
            decoded_output[n] = 0
        if type(decoded_output[n]) == str and set(decoded_output[n]) == two:
            decoded_output[n] = 2
        if type(decoded_output[n]) == str and set(decoded_output[n]) == three:
            decoded_output[n] = 3

    # join decoded output
    strings = [str(integer) for integer in decoded_output]
    a_string = "".join(strings)
    an_integer = int(a_string)
    # print(an_integer)

    return an_integer




if __name__ == "__main__":
    # get_uniques('input')
    with open("8\input.txt", "r") as f:
        lines = f.readlines()

    summ = 0
    for line in lines:
        summ += decode(line)
    print(summ)