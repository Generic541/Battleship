from Battleship_core import set_board_state
from Battleship_core import get_board_state
from Battleship_core import set_board_size
from Battleship_core import print_board
from Battleship_core import create_battleship
from Battleship_core import set_remain_life
from Battleship_core import get_remain_life
from Battleship_core import get_blank_tile_col
from Battleship_core import get_blank_tile_row
from Battleship_core import SHIP_EXISTS
from Battleship_core import SHIP_SUNK
from Battleship_core import MISSED

def fire(row_pos, col_pos):
    if get_board_state(row_pos, col_pos) == SHIP_EXISTS:
        print("You find an enemy's battleship!")
        set_board_state(row_pos, col_pos, SHIP_SUNK)
    elif get_board_state(row_pos, col_pos) == SHIP_SUNK or get_board_state(row_pos, col_pos) == MISSED:
        print("You have already fired there. try again")
    else:
        print("You missed! lose one of your life.")
        set_board_state(row_pos, col_pos, MISSED)



def check_remain_ships():
    if get_blank_tile_col == -1 and get_blank_tile_row == -1:
        return 9999

def check_life():
    if get_remain_life() <= 1:
        print("You Lose!")
        return -1
    else:
        set_remain_life(get_remain_life() - 1)
        return 0

def welcomeDisplay():
    print("  ____        _   _   _           _     _       ")
    print(" |  _ \      | | | | | |         | |   (_)      ")
    print(" | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ")
    print(" |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ ")
    print(" | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |")
    print(" |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ ")
    print("                                         | |    ")
    print("                                         |_|    ")
    print("Welcome to Battleship prototype!")
    print("In this version, only few functions are implemented:")
    print("1. 1 * 1 size battleships only.")
    print("2. Only single-player mode, no opponents.")
    print("Although there are a lot of unskilled functions, please enjoy! :D \n")
    print("To quit, type \'quit\' on the console.")

# How could i implement the restart function? i wonder.
def restart(userInput):
    pass

if __name__ == "__main__":
    # Display only once
    welcomeDisplay()
    userInput = input(">>")

    while userInput is not 'quit':
        try:
            # If there's a carriage return, you should filter it. Code enhancement required.
            set_board_size(int(input("Board width? : ")), int(input("Board height? : ")))
            create_battleship(int(input("Ship amount? ")))
        except ValueError:
            print("Oops. it seems you just entered wrong value. only natural number is allowed.")
            print("and the board's width and height must be greater than 0, less than 50.")
            continue
        while True:
            try:
                print("Your turn. remaining life is " + str(get_remain_life()))
                fire(int(input("row? : ")), int(input("col? : ")))
                print_board()

                if check_life() == -1:
                    print("Do you want to restart a game? if yes, press any key. or please just shut down game manually.")
                    if input() is not "\n":
                        break

                if check_remain_ships() == 9999:
                    print("You win! do you want to restart a game? if you want, type \'y\' on console. or you can just shut down the game.")
                    break
            except ValueError:
                print("Oops. it seems you just entered wrong value. only natural number is allowed.")
                continue