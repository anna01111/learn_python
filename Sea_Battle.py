import string
import random

# defining a cell status
empty = ' '
ship_alive = '■'
ship_killed = 'x'
missed = '·'


def create_board(size):
    board = []
    for i in range(size):
        board.append([' ' for el in range(size)])
    return board


def print_board(board):
    board_to_print = board
    letters = list(string.ascii_uppercase)
    letters.insert(0, ' ')
    letters = letters[:len(board) + 1]
    letters.append('')
    numbers = [num for num in range(len(board) + 1)]
    numbers = list(map(str, numbers))
    for i in range(len(board_to_print)):
        board_to_print[i].insert(0, numbers[i])
        board_to_print[i].append('')
    board_to_print.insert(0, letters)
    for i in range(len(board_to_print)):
        print(' | '.join(board_to_print[i]))
        print('__|_' * (len(board_to_print) - 1) + '__|')


def put_ships(board):  # one of core functions
    pass


def put_a_ship(board, ship_size):
    pass


def check_if_correct_placement(board):
    pass


def reserve_space_around_a_ship(board):
    pass


def fire_a_shot(board):  # one of core functions
    pass


def winner_check(board):  # one of core functions
    pass


my_board = create_board(10)
print_board(my_board)


