"""Game of Life model"""
import random
import render_term

X = 80
Y = 50
gameboard = []
for y in range(Y):
    gameboard.append([])
    for x in range(X):
        gameboard[y].append(random.getrandbits(1))

gameboard_temp = []
for y in range(Y):
    gameboard_temp.append([])
    for x in range(X):
        gameboard_temp[y].append(0)

def count_neighbors(x, y, board):
    count = 0
    if y-1 >= 0 and board[y-1][x] == 1:
        count += 1
    if y-1 >= 0 and x+1 < X and board[y-1][x+1] == 1:
        count += 1
    if y-1 >= 0 and x-1 >= 0 and board[y-1][x-1] == 1:
        count += 1
    if y+1 < Y and board[y+1][x] == 1:
        count += 1
    if y+1 < Y and x+1 < X and board[y+1][x+1] == 1:
        count += 1
    if y+1 < Y and x-1 >= 0 and board[y+1][x-1] == 1:
        count += 1
    if x+1 < X and board[y][x+1] == 1:
        count += 1
    if x-1 >= 0 and board[y][x-1] == 1:
        count += 1
    return count


def calc_new_value(x, y, board):
    count = count_neighbors(x, y, board)
    if count == 0 or count == 1:
        newvalue = 0
    elif count == 2:
        newvalue = board[y][x]
    elif count == 3:
        newvalue = 1
    elif count >= 4:
        newvalue = 0
    return newvalue

while True:
    for y in range(Y):
        for x in range(X):
            gameboard_temp[y][x] = calc_new_value(x, y, gameboard)

    for y in range(Y):
        for x in range(X):
            gameboard[y][x] = gameboard_temp[y][x]

    render_term.draw(gameboard)
