
def create_board():
    """Creates a 3x3 board

    Returns
    -------
    list
        A list containing three lists, each of which contains three strings
    """

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return board


def print_board(board):
    """Prints a 3x3 board

    Parameters
    ----------
    board : list
        A list containing three lists, each of which contains three strings
    """

    print(' {} | {} | {} '.format(board[0][0], board[0][1], board[0][2]))
    print('___|___|___')
    print(' {} | {} | {} '.format(board[1][0], board[1][1], board[1][2]))
    print('___|___|___')
    print(' {} | {} | {} '.format(board[2][0], board[2][1], board[2][2]))
    print('   |   |   ')


def place_sign(board, signs):
    """Places the sign on the board

    Parameters
    ----------
    board : list
        A list containing three lists, each of which contains three strings
    signs : list
        A list containing two strings - each string represents a sign
    """

    try:
        print_board(board)
        row = int(input('Enter a row to place ' + signs[0] + ' (1, 2 or 3): '))
        col = int(input('Enter a col to place ' + signs[0] + ' (1, 2 or 3): '))
        if board[row - 1][col - 1] == ' ':
            board[row - 1][col - 1] = signs[0]  # places the sign on the board if the place is free
        else:
            print('THIS PLACE IS OCCUPIED, PLEASE TRY AGAIN')
            place_sign(board, signs)
    except ValueError:  # handles a situation when user input can not be converted to an integer
        print('ERROR - ENTER VALID NUMBER ')
        place_sign(board, signs)
    except IndexError:  # handles a situation when user input is out of the board's index range
        print('ERROR - ENTER VALID NUMBER ')
        place_sign(board, signs)


def winner_check(board):
    """Checks if there is a winner

    Parameters
    ----------
    board : list
        A list containing three lists, each of which contains three strings

    Returns
    -------
    bool or str
        False if there is no winner or string representing a winner if there is a winner
    """

    winner = False
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] != ' ':  # looks for a winner in the horizontal lines
            winner = board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != ' ':  # looks for a winner in the vertical lines
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':  # looks for a winner in the diagonals
            winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
            winner = board[0][2]
    return winner


def draw_check(board):
    """Checks if there is a draw

    Parameters
    ----------
    board : list
        A list containing three lists, each of which contains three strings

    Returns
    -------
    bool
        True if there is a draw, False if there is no draw
    """

    for el in board:
        if ' ' in el:
            return False
    return True


my_signs = ['x', 'o']
my_board = create_board()
print('Welcome to my game ^ ^')
while True:
    if winner_check(my_board):
        print_board(my_board)
        print('The winner is ' + winner_check(my_board))
        break
    elif draw_check(my_board):
        print_board(my_board)
        print('There is a draw')
        break
    place_sign(my_board, my_signs)
    my_signs = my_signs[::-1]  # swaps the signs so that players can take turns





