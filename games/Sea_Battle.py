import string
import random
import copy

# possible cell states are:
# empty ' '
# ship alive '■'
# ship killed 'x'
# missed '.'
# temporarily reserved space '/'


def create_board(size):
    """Creates a two-dimensional list with a given size

    Parameters
    ----------
    size : int
        Represents a number of cells. 10 would give a 10x10 square

    Returns
    -------
    list
        A game board, where each cell is initially represented with ' '
    """

    board = []
    for i in range(size):
        board.append([' ' for el in range(size)])
    return board


def modify_board(board_copy):
    """Inserts numbers and letters, which will help user identify cells

    Parameters
    ----------
     board_copy : list
        Copy of a board, which is made in purpose of further modification and printing to console
    """

    letters = list(string.ascii_uppercase)  # makes a list of uppercase letters
    letters.insert(0, ' ')
    letters = letters[:len(board_copy) + 1]  # cuts the list in order for it to align with the size of a board
    letters.append('')  # technical change to make a board look square when printing
    numbers = [num for num in range(len(board_copy) + 1)]  # makes a list of numbers
    numbers = list(map(str, numbers))  # converts each number in the list to a string
    for i in range(len(board_copy)):
        board_copy[i].insert(0, numbers[i])  # inserts a number in the beginning of each row on the board
        board_copy[i].append('')  # technical change to make a board look square when printing
    board_copy.insert(0, letters)  # inserts letters on the top of each column on the board


def print_board(user_board_copy, machine_board_copy, user_name, machine_name):
    """Prints user board and machine board with names on the top of each board.

    Parameters
    ----------
    user_board_copy : list
        User board, modified for printing
    machine_board_copy : list
        Machine board, modified for printing
    user_name : str
    machine_name : str
    """

    hide_ships(machine_board_copy)
    modify_board(machine_board_copy)
    modify_board(user_board_copy)
    print('\n')
    print(' ' * (25 - len(user_name)) + user_name.upper() + '\'s BOARD' + ' ' * 44 + machine_name.upper() + '\'s BOARD\n')
    for i in range(len(user_board_copy)):  # for every row in a board -
        # prints a row, with elements separated by |
        print(' ' * 5 + ' | '.join(user_board_copy[i]) + ' ' * 15 + ' | '.join(machine_board_copy[i]))
        # prints additional signs to make a board look square
        print(' ' * 5 + '__|_' * (len(user_board_copy) - 1) + '__| ' + ' ' * 15 + '__|_' * (len(machine_board_copy) - 1) + '__|')
    print('\n')


def define_initial_unit_of_ship(board):
    """Generates two random numbers within the range of board elements' indexes

    Parameters
    ----------
    board : list
        Game board - a two-dimensional list

    Returns
    -------
    list
        A two-dimensional list which contains indexes of the ship's first unit
    """

    initial_unit_indexes = [random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)]
    ship_indexes = []  # creates list that will contain indexes of ships
    ship_indexes.append(initial_unit_indexes)
    return ship_indexes


def define_subsequent_units(ship_indexes, ship_size):
    """Creates a ship of a given size

    Parameters
    ----------
    ship_indexes : list
        A two-dimensional list which contains indexes of the ship's first unit
    ship_size : int
        Represents a number of cells a ship consists of

    Returns
    -------
    list
        A two-dimensional list which contains indexes of the ships' units
    """

    a = random.choice([-1, 1])
    b = [0, a]
    random.shuffle(b)  # randomly decides in which direction to build the ship
    for i in range(ship_size - 1):
        subsequent_unit_indexes = [ship_indexes[-1][0] + b[0], ship_indexes[-1][1] + b[1]]
        ship_indexes.append(subsequent_unit_indexes)
    return ship_indexes


def ship_correctly_defined(board, ship_indexes):
    """Checks if the ship is within the board and does not overlap with other ships or reserved space

    Parameters
    ----------
    board : list
        Game board - a two-dimensional list
    ship_indexes : list
        A two-dimensional list which contains indexes of the ships' units

    Returns
    -------
    bool
        True if ship is correctly defined and False if not
    """

    for i in range(len(ship_indexes)):  # checks if the ship is within the board
        if 0 <= ship_indexes[i][0] < len(board) and 0 <= ship_indexes[i][1] < len(board):
            continue
        else:
            return False
    for i in range(len(ship_indexes)):  # checks if the ship overlaps with other ships or reserved space
        if board[ship_indexes[i][0]][ship_indexes[i][1]] == ' ':
            continue
        else:
            return False
    return True


def reserve_space_around_ship(board, ship_indexes):
    """For each cell in a ship, finds all neighboring cells and reserves them so that ships will not touch each other

    Parameters
    ----------
    board : list
        Game board - a two-dimensional list
    ship_indexes : list
        A two-dimensional list which contains indexes of the ships' units
    """

    for el in ship_indexes:
        # defines shifts, that will later be added to the ship unit's indexes
        # this will result in indexes of cells that will have to be reserved
        index_shift = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for i in range(len(index_shift)):
            # finds all the neighboring cells and reserves them
            if 0 <= el[0] + index_shift[i][0] < len(board) and 0 <= el[1] + index_shift[i][1] < len(board):
                board[el[0] + index_shift[i][0]][el[1] + index_shift[i][1]] = '/'


def put_a_ship(board, ship_size):
    """Puts a ship on a board

    Parameters
    ----------
    board : list
        Game board - a two-dimensional list
    ship_size : int
        Represents a number of cells a ship consists of
    """

    ship_indexes = define_initial_unit_of_ship(board)
    define_subsequent_units(ship_indexes, ship_size)
    if ship_correctly_defined(board, ship_indexes):
        reserve_space_around_ship(board, ship_indexes)
        for i in range(len(ship_indexes)):
            board[ship_indexes[i][0]][ship_indexes[i][1]] = '■'  # puts a ship, overriding reservation marks, if any
    else:
        put_a_ship(board, ship_size)  # retries, in case a ship did not meet conditions


def put_ships(board):
    """Puts one 4-cell ship, two 3-cell ships, three 2-cells ships and four 1-cell ships

    Parameters
    ----------
    board : list
        Game board - a two-dimensional list
    """

    put_a_ship(board, 4)
    for i in range(2):
        put_a_ship(board, 3)
    for i in range(3):
        put_a_ship(board, 2)
    for i in range(4):
        put_a_ship(board, 1)
    remove_reserved_space(board)


def remove_reserved_space(board):
    """Removes reserved space from the board - it was needed only on the phase of ship placement

    Parameters
    ----------
    board : list
        Game board - a two-dimensional list
    """

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '/':
                board[i][j] = ' '  # removes reservation marks from the board


def hide_ships(machine_board_copy):
    """Hides ships on the machine board so that user can no see it

    Parameters
    ----------
    machine_board_copy : list
        Copy of a board, which is made in purpose of printing to console
    """

    for i in range(len(machine_board_copy)):
        for j in range(len(machine_board_copy[i])):
            if machine_board_copy[i][j] == '■':
                machine_board_copy[i][j] = ' '  # hides machine ships from user


def random_shot(user_board, machine_name):
    """Makes a random shot on the board and prints out a message

    Parameters
    ----------
    user_board : list
        User game board - a two-dimensional list
    machine_name : str
    """

    random_index = [random.randint(0, len(user_board) - 1), random.randint(0, len(user_board) - 1)]
    if user_board[random_index[0]][random_index[1]] == '■':  # if shot hits a ship
        user_board[random_index[0]][random_index[1]] = 'x'  # marks respective unit of a ship as killed
        print('NICEEE SHOT ' + machine_name)
        # if shot hits a killed unit of a ship or a cell where there already have been an unsuccessful shot -
        # retries a shot
    elif user_board[random_index[0]][random_index[1]] == 'x' or user_board[random_index[0]][random_index[1]] == '.':
        random_shot(user_board, machine_name)
    else:
        user_board[random_index[0]][random_index[1]] = '.'  # places a dot if a shot did not hit a ship
        print('no luck for ' + machine_name)


def user_shot(machine_board, user_name):
    """Makes a shot on the board based on user input; prints out a message

    Parameters
    ----------
    machine_board : list
        Machine game board - a two-dimensional list
    user_name : str
    """

    try:
        letters = list(string.ascii_uppercase)
        letters = letters[:len(machine_board)]
        user_input = list(input('Now enter a cell where you want to shoot, like 1A:'))
        print('\n')
        # transforms user input (e.g. '2B') to an index (e.g. [2, 1])
        user_index = [int(user_input[0]), letters.index(user_input[1].upper())]
        if machine_board[user_index[0]][user_index[1]] == '■':  # if shot hits a ship
            machine_board[user_index[0]][user_index[1]] = 'x'  # marks respective unit of a ship as killed
            print('NICEEE SHOT ' + user_name)
        # if shot hits a killed unit of a ship or a cell where there already have been an unsuccessful shot -
        # prints 'no luck'
        elif machine_board[user_index[0]][user_index[1]] == 'x' or machine_board[user_index[0]][user_index[1]] == '.':
            print('no luck for ' + user_name)
        else:
            machine_board[user_index[0]][user_index[1]] = '.'  # places a dot if a shot did not hit a ship
            print('no luck for ' + user_name)
    except ValueError:
        print('ERROR - INCORRECT CELL IDENTIFIER')
        user_shot(machine_board, user_name)
    except IndexError:
        print('ERROR - INCORRECT CELL IDENTIFIER')
        user_shot(machine_board, user_name)


def loose_situation(board):
    """Checks if all the ships on the board have been shot dead

    Parameters
    ----------
    board : list
        Game board - a two-dimensional list

    Returns
    -------
    bool
        True if all the ships are dead and False if not
    """

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

# makes copy of boards in order to prepare them for printing
my_user_board_copy = copy.deepcopy(my_user_board)
my_machine_board_copy = copy.deepcopy(my_machine_board)

print_board(my_user_board_copy, my_machine_board_copy, my_user_name, my_machine_name)

while True:
    user_shot(my_machine_board, my_user_name)
    random_shot(my_user_board, my_machine_name)

    my_user_board_copy = copy.deepcopy(my_user_board)
    my_machine_board_copy = copy.deepcopy(my_machine_board)

    print_board(my_user_board_copy, my_machine_board_copy, my_user_name, my_machine_name)

    if loose_situation(my_user_board) and loose_situation(my_machine_board):
        print('it\'s a draw')
        break
    elif loose_situation(my_user_board):
        print('VICTORY GOES TO ' + my_machine_name)
        break
    elif loose_situation(my_machine_board):
        print('VICTORY GOES TO ' + my_user_name)
        break

print('\nend of the game')

