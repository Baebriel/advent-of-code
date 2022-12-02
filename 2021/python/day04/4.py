### part 1 ###

# verify board
# board is 2D list [['1','2','3','4','5'],
#                   ['6','7','8','9','10'],...]
def verify_board(board, draws):
    win = False

    for line in board:
        print(line)
    print('---------------------')

    # check for complete rows
    for row in board:
        win = all(elem in draws for elem in row)
        if win:
            # print(f'row complete: {row}')
            break

    # check for complete columns
    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        win = all(elem in draws for elem in col)
        if win:
            # print(f'col complete: {col}')
            break
    
    # if win is True, get sum of non-marked numbers
    if win:
        # print('win!')
        score = 0
        for line in board:
            for val in line:
                if val not in draws:
                    score += int(val)

        return score * int(draws[-1])

    return 0

with open('day04\input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
#         '',
#         '22 13 17 11  0',
#         ' 8  2 23  4 24',
#         '21  9 14 16  7',
#         '6 10  3 18  5',
#         '1 12 20 15 19',
#         '',
# ' 3 15  0  2 22',
#  '9 18 13 17  5',
# '19  8  7 25 23',
# '20 11 10 24  4',
# '14 21 16 12  6',
# '',
# '14 21 17 24  4',
# '10 16 15  9 19',
# '18  8 23 26 20',
# '22 11 13  6  5',
# ' 2  0 12  3  7']

draws = lines[0].split(',')

win = False
for i in range(len(draws)):
    if not win:
        draw = draws[:i+1]
        for i in range(2,int(int(len(lines)+11) / 6)):
            board = [line.split() for line in lines[6*i-10:6*i-5]]
            score = verify_board(board, draw)
            if score != 0:
                win = True
                print(score)
                break
    else:
        break

### part 2 ###
boards = 0
for x in range(len(draws)):
    draw = draws[:x+1]
    for i in range(2,1000):
        board = [line.split() for line in lines[6*i-10:6*i-5]]
        score = verify_board(board, draw)
        if score != 0:
            boards += 1
            print(f'{i}: {score}')
            break
    if boards == 120:
        print('done')
        break


