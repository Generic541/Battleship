#
# Battleship prototype
# Powered by codecademy
# Made on 2017. 07. 27
# Author : TC_G & codecademy
# compiler option : Python 3.6.X
#

import random

# Battleship board. consists in (n rows) * (m cols)
# Default size is 5 * 5

remain_life = 3
board = []
board_width = 0
board_height = 0


# These are STATE constant, which used to describle tile's status.
# 'X' means sunk ship tile
# 'O' means not inspected tile
# 'M' means missed tile
# 'S' means that ship is here

SHIP_SUNK = 'X'
NOT_INSPECTED = 'O'
MISSED = 'M'
SHIP_EXISTS = 'S'

def set_board_width(new_amount):
    if not 0 < new_amount < 50:
        return -1
    global board_width
    board_width = new_amount

def set_board_height(new_amount):
    if not 0 < new_amount < 50:
        return -1
    global board_height
    board_height = new_amount

def get_board_width():
    global board_width
    return board_width

def get_board_height():
    global board_height
    return board_height

def set_board_size(width, height):
    set_board_width(width)
    set_board_height(height)
    for i in range(width):
        board.append([NOT_INSPECTED] * height)

def print_board():
    for row in board:
        for letter in row:
            print(letter.replace(SHIP_EXISTS, NOT_INSPECTED), end = "")
        print()

# Create battleship randomly.
def create_battleship(ship_amount):
    for i in range(ship_amount):
        if get_board_state(get_random_col(get_board_width()), get_random_row(get_board_height())) == SHIP_EXISTS:
            set_board_state(get_blank_tile_row(), get_blank_tile_col(), SHIP_EXISTS)
        else:
            set_board_state(get_random_row(board_width), get_random_col(board_height), SHIP_EXISTS)
    "Successfully created {0} battleships. \n".format(str(ship_amount))

def set_board_state(row_pos, col_pos, STATE):
    try:
        # Better indexing required. please improve
        board[row_pos][col_pos] = STATE
    except IndexError:
        return -1

def get_board_state(row_pos, col_pos):
    try:
        return board[row_pos][col_pos]
    except IndexError:
        return -1

# Only gets most prior blank tile, must be changed
def get_blank_tile_row():
    for i in range(0, board_width):
        for j in range(0, board_height):
            if board[i][j] == NOT_INSPECTED:
                return i

            return -1

# Only gets most prior blank tile, must be changed.
def get_blank_tile_col():
    for i in range(0, board_width):
        for j in range(0, board_height):
            if board[i][j] == NOT_INSPECTED:
                return j

            return -1

def get_random_col(limit):
    return random.randrange(0, limit)

def get_random_row(limit):
    return random.randrange(0, limit)

def get_remain_life():
    return remain_life

def set_remain_life(new_amount):
    global remain_life
    remain_life = new_amount
    return remain_life

