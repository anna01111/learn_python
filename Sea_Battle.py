
empty = ' '
ship_alive = '0'
ship_killed = 'x'
missed = '-'


def create_board(size):
    board = []
    for i in range(size):
        board.append(['o' for el in range(size)])
    return board


def print_board(board):
    board_to_print = board
    letters = ['  ', 'A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ', 'J ']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(board_to_print)):
        board_to_print[i].insert(0, numbers[i])
        board_to_print[i].append('')
    print(''.join(map(''.join, letters)))
    print('\n'.join(map('|'.join, board_to_print)))


my_board = create_board(10)
print_board(my_board)
