"""Game of Life model"""
import random
import render_term

X = 20
Y = 20
gameboard = []
for i in range(Y):
    gameboard.append([])
    for j in range(X):
        gameboard[i].append(random.getrandbits(1))

gameboard_temp = []
for i in range(Y):
    gameboard_temp.append([])
    for j in range(X):
        gameboard_temp[i].append(0)


def calc_new_value(i, j, board):
    return random.getrandbits(1)


while True:
    for i in range(Y):
        for j in range(X):
            gameboard_temp[i][j] = calc_new_value(i, j, gameboard)

    for i in range(Y):
        for j in range(X):
            gameboard[i][j] = gameboard_temp[i][j]

    render_term.draw(gameboard)
