'''Render Game of Life boards to the terminal.'''

import os
import random
import time

def draw(board):
    os.system('clear')  # clear screen, not OS portable
    print('The Game of Life')
    print('')

    for row in board:
        for pixel in row:
            if pixel:
                print('*', end='')
            else:
                print(' ', end='')
        print('')
    print('')
    time.sleep(1)


def test():
    for i in range(100):
        board = [[random.getrandbits(1) for i in range(50)] for j in range(30)]
        draw(board)

if __name__ == '__main__':
    test()
