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


def hide_ships_in_machine_board_copy(machine_board_copy):
    for i in range(len(machine_board_copy)):
        for j in range(len(machine_board_copy[i])):
            if machine_board_copy[i][j] == '■':
                machine_board_copy[i][j] = ' '
    return machine_board_copy


def modify_board_copy(board_copy):
    letters = list(string.ascii_uppercase)
    letters.insert(0, ' ')
    letters = letters[:len(board_copy) + 1]
    letters.append('')
    numbers = [num for num in range(len(board_copy) + 1)]
    numbers = list(map(str, numbers))
    for i in range(len(board_copy)):
        board_copy[i].insert(0, numbers[i])
        board_copy[i].append('')
    board_copy.insert(0, letters)
    return board_copy


def print_board_copy(user_board_copy, machine_board_copy):
    hide_ships_in_machine_board_copy(machine_board_copy)
    modify_board_copy(machine_board_copy)
    modify_board_copy(user_board_copy)
    print('\n')
    print(' ' * 21 + 'USER BOARD' + ' ' * 48 + 'MACHINE BOARD \n')
    for i in range(len(user_board_copy)):
        print(' ' * 5 + ' | '.join(user_board_copy[i]) + ' ' * 15 + ' | '.join(machine_board_copy[i]))
        print(' ' * 5 + '__|_' * (len(user_board_copy) - 1) + '__| ' + ' ' * 15 + '__|_' * (len(machine_board_copy) - 1) + '__|')
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
    ship_indexes = define_initial_unit_of_a_ship(board)
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


my_user_board = create_board(10)
my_machine_board = create_board(10)

put_ships(my_user_board)
put_ships(my_machine_board)

my_user_board_copy = copy.deepcopy(my_user_board)
my_machine_board_copy = copy.deepcopy(my_machine_board)

# while True:

print_board_copy(my_user_board_copy, my_machine_board_copy)


