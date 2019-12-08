"""Game of Life model"""
import random
import render_term

X = 80
Y = 50
gameboard = []
gameboard_temp = []

def init_board(rand=True):
    board = []
    for y in range(Y):
        board.append([])
        for x in range(X):
            if rand:
                board[y].append(random.getrandbits(1))
            else:
                board[y].append(0)
    return board

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

def next_board(board):
    board_next = init_board(rand=False)
    for y in range(Y):
        for x in range(X):
            board_next[y][x] = calc_new_value(x, y, board)
    return board_next

def test():
    gameboard = init_board(rand=True)
    while True:
        gameboard = next_board(gameboard)
        render_term.draw(gameboard)

if __name__ == '__main__':
    test()

