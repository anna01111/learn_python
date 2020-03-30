import string
import random
import copy

# empty ' '
# ship_alive '■'
# ship_killed 'x'
# missed '·'
# temporarily_reserved_space '/'


def create_board(size):
    board = []
    for i in range(size):
        board.append([' ' for el in range(size)])
    return board


def print_board(board):
    board_to_print = copy.deepcopy(board)
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
    print('\n')
    for i in range(len(board_to_print)):
        print(' | '.join(board_to_print[i]))
        print('__|_' * (len(board_to_print) - 1) + '__|')
    print('\n')


def define_initial_unit_of_a_ship(board):
    initial_unit_indexes = [random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)]
    ship_indexes = []
    ship_indexes.append(initial_unit_indexes)
    return ship_indexes


def define_subsequent_units(ship_indexes, ship_size):
    a = random.choice([-1, 1])
    b = [0, a]
    random.shuffle(b)
    for i in range(ship_size - 1):
        subsequent_unit_indexes = [ship_indexes[-1][0] + b[0], ship_indexes[-1][1] + b[1]]
        ship_indexes.append(subsequent_unit_indexes)
    return ship_indexes


def ship_is_correctly_defined(board, ship_indexes):
    for i in range(len(ship_indexes)):
        if 0 <= ship_indexes[i][0] < len(board) and 0 <= ship_indexes[i][1] < len(board):
            continue
        else:
            return False
    for i in range(len(ship_indexes)):
        if board[ship_indexes[i][0]][ship_indexes[i][1]] == ' ':
            continue
        else:
            return False
    return True


def reserve_space_around_a_ship(board, ship_indexes):
    for el in ship_indexes:
        # reserving horizontals and verticals
        if 0 <= el[0] + 1 < len(board):
            board[el[0] + 1][el[1]] = '/'
        if 0 <= el[0] - 1 < len(board):
            board[el[0] - 1][el[1]] = '/'
        if 0 <= el[1] + 1 < len(board):
            board[el[0]][el[1] + 1] = '/'
        if 0 <= el[1] - 1 < len(board):
            board[el[0]][el[1] - 1] = '/'
        # reserving diagonals
        if 0 <= el[0] + 1 < len(board) and 0 <= el[1] + 1 < len(board):
            board[el[0] + 1][el[1] + 1] = '/'
        if 0 <= el[0] - 1 < len(board) and 0 <= el[1] - 1 < len(board):
            board[el[0] - 1][el[1] - 1] = '/'
        if 0 <= el[0] - 1 < len(board) and 0 <= el[1] + 1 < len(board):
            board[el[0] - 1][el[1] + 1] = '/'
        if 0 <= el[0] + 1 < len(board) and 0 <= el[1] - 1 < len(board):
            board[el[0] + 1][el[1] - 1] = '/'
    return board


def put_a_ship(board, ship_size):
    ship_indexes = define_initial_unit_of_a_ship(my_board)
    define_subsequent_units(ship_indexes, ship_size)
    if ship_is_correctly_defined(board, ship_indexes):
        reserve_space_around_a_ship(board, ship_indexes)
        for i in range(len(ship_indexes)):
            board[ship_indexes[i][0]][ship_indexes[i][1]] = '■'
    else:
        put_a_ship(board, ship_size)


def put_ships(board):
    put_a_ship(board, 4)
    for i in range(2):
        put_a_ship(board, 3)
    for i in range(3):
        put_a_ship(board, 2)
    for i in range(4):
        put_a_ship(board, 1)
    remove_reserved_space(board)
    return board


def remove_reserved_space(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '/':
                board[i][j] = ' '
    return board


def fire_a_shot(board):
    pass


def winner_check(board):
    pass


my_board = create_board(10)
put_ships(my_board)
print_board(my_board)


