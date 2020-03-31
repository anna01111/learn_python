import string
import random
import copy

# Possible cell states are:
# empty ' '
# ship_alive '■'
# ship_killed 'x'
# missed '.'
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


def print_board_copy(user_board_copy, machine_board_copy, user_name, machine_name):
    hide_ships_in_machine_board_copy(machine_board_copy)
    modify_board_copy(machine_board_copy)
    modify_board_copy(user_board_copy)
    print('\n')
    print(' ' * (25 - len(user_name)) + user_name.upper() + '\'s BOARD' + ' ' * 44 + machine_name.upper() + '\'s BOARD\n')
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
        index_shift = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for i in range(len(index_shift)):
            if 0 <= el[0] + index_shift[i][0] < len(board) and 0 <= el[1] + index_shift[i][1] < len(board):
                board[el[0] + index_shift[i][0]][el[1] + index_shift[i][1]] = '/'
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


def fire_a_random_shot(user_board, machine_name):
    random_index = [random.randint(0, len(user_board) - 1), random.randint(0, len(user_board) - 1)]
    if user_board[random_index[0]][random_index[1]] == '■':
        user_board[random_index[0]][random_index[1]] = 'x'
        print('NICEEE SHOT ' + machine_name)
    elif user_board[random_index[0]][random_index[1]] == 'x':
        fire_a_random_shot(user_board, machine_name)
    elif user_board[random_index[0]][random_index[1]] == '.':
        fire_a_random_shot(user_board, machine_name)
    else:
        user_board[random_index[0]][random_index[1]] = '.'
        print('no luck for ' + machine_name)
        return user_board


def fire_a_user_defined_shot(machine_board, user_name):
    try:
        letters = list(string.ascii_uppercase)
        letters = letters[:len(machine_board)]
        user_input = list(input('Now enter a cell where you want to shoot, like 1A:\n'))
        user_index = [int(user_input[0]), letters.index(user_input[1].upper())]
        if machine_board[user_index[0]][user_index[1]] == '■':
            machine_board[user_index[0]][user_index[1]] = 'x'
            print('NICEEE SHOT ' + user_name)
        elif machine_board[user_index[0]][user_index[1]] == 'x':
            print('no luck for ' + user_name)
        elif machine_board[user_index[0]][user_index[1]] == '.':
            print('no luck for ' + user_name)
        else:
            machine_board[user_index[0]][user_index[1]] = '.'
            print('no luck for ' + user_name)
            return machine_board
    except ValueError:
        print('ERROR - INCORRECT CELL IDENTIFIER')
        fire_a_user_defined_shot(machine_board, user_name)
    except IndexError:
        print('ERROR - INCORRECT CELL IDENTIFIER')
        fire_a_user_defined_shot(machine_board, user_name)


def loose_situation_happened(board):
    for el in board:
        if '■' in el:
            return False
        else:
            continue
    return True


my_user_board = create_board(10)
my_machine_board = create_board(10)

put_ships(my_user_board)
put_ships(my_machine_board)

my_user_name = input('\nWelcome to the gameeeee ^ ^\nPlease enter your name, and we\'ll generate a board for you: ')
my_machine_name = 'machine'

my_user_board_copy = copy.deepcopy(my_user_board)
my_machine_board_copy = copy.deepcopy(my_machine_board)

print_board_copy(my_user_board_copy, my_machine_board_copy, my_user_name, my_machine_name)

while True:
    fire_a_user_defined_shot(my_machine_board, my_user_name)
    fire_a_random_shot(my_user_board, my_machine_name)

    my_user_board_copy = copy.deepcopy(my_user_board)
    my_machine_board_copy = copy.deepcopy(my_machine_board)

    print_board_copy(my_user_board_copy, my_machine_board_copy, my_user_name, my_machine_name)

    if loose_situation_happened(my_user_board) and loose_situation_happened(my_machine_board):
        print('it\'s a draw')
        break
    elif loose_situation_happened(my_user_board):
        print('VICTORY GOES TO ' + my_machine_name)
        break
    elif loose_situation_happened(my_machine_board):
        print('VICTORY GOES TO ' + my_user_name)
        break

print('\nend of the game')

