import sys
from random import randrange

gridy = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

me = 'x'
com = 'o'


def appear():
    counter = 0
    for i in range(3):
        print(gridy[i + counter], '|', gridy[i + counter + 1], '|', gridy[i + counter + 2])
        print('---------')
        counter += 2


def winner(th_nums):
    win = False
    th_nums.sort()
    win_tab = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]
    for i in win_tab:
        if i == th_nums:
            win = True
    return win


def th_create(xo_list):
    if len(xo_list) == 3:
        return winner(xo_list)
    elif len(xo_list) == 4:
        for i in range(4):
            xoo_list = []
            for j in range(4):
                if j == i:
                    continue
                xoo_list.append(xo_list[j])
            if winner(xoo_list):
                return True
        else:
            return False
    else:
        for i in range(5):
            xoo_list = []
            for j in range(5):
                if j == i:
                    continue
                xoo_list.append(xo_list[j])
            for k in range(4):
                xooo_list = []
                for l in range(4):
                    if k == l:
                        continue
                    xooo_list.append(xoo_list[l])
                if winner(xooo_list):
                    return True

        else:
            return False

def play_again():
    next_round = input('Do you want to play again? (y, n) ')
    if next_round == 'y':
        globals()['gridy'] = [' ', ' ', ' ',
                              ' ', ' ', ' ',
                              ' ', ' ', ' ']
        print('--- start game ---')
        globals()['turns'] = 0
        globals()['start'] = True
        globals()['x_list'] = []
        globals()['o_list'] = []
        globals()['indx_list'] = []
    else:
        sys.exit()


print('--- start game ---')
turns = 0
start = True
x_list = []
o_list = []
indx_list = []

while start:

    if globals()['turns'] < 9:
        indx = int(input('Select a spot : '))
        while indx_list.__contains__(indx - 1):
            indx = int(input('Select a spot : '))
        indx_list.append(indx - 1)
        x_list.append(indx - 1)
        gridy[indx - 1] = me
        globals()['turns'] += 1
        if len(x_list) > 2:
            if th_create(x_list):
                appear()
                print('*** You win ***')
                play_again()

    if globals()['turns'] < 9:
        r_indx = randrange(9)
        while indx_list.__contains__(r_indx):
            r_indx = randrange(9)
        indx_list.append(r_indx)
        o_list.append(r_indx)
        gridy[r_indx] = com
        globals()['turns'] += 1
        if len(o_list) > 2:
            if th_create(o_list):
                appear()
                print('*** Com wins ***')
                play_again()

    appear()
    if turns == 9:
        print('___ game draw ___')
        play_again()


