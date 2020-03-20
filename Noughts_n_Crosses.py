
def create_board():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return board


def print_board(board):
    print(' {} | {} | {} '.format(board[0][0], board[0][1], board[0][2]))
    print('___|___|___')
    print(' {} | {} | {} '.format(board[1][0], board[1][1], board[1][2]))
    print('___|___|___')
    print(' {} | {} | {} '.format(board[2][0], board[2][1], board[2][2]))
    print('   |   |   ')


def place_sign(board, signs):
    print_board(board)
    row = int(input('Enter a row to place ' + signs[0] + ' (1, 2 or 3): '))
    col = int(input('Enter a col to place ' + signs[0] + ' (1, 2 or 3): '))
    if board[row - 1][col - 1] == ' ':
        board[row - 1][col - 1] = signs[0]
    else:
        print('This place is occupied, please try again')
        place_sign(board, signs)


def winner_check(board):
    """
    :param board:
    :return: False if there is no winner, winner if there is a winner
    """
    winner = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
            winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
            winner = board[0][2]
    return winner


def draw_check(board):
    """
    :param board:
    :return: True if there is a draw ans False if not
    """
    for el in board:
        if ' ' in el:
            return False
        else:
            continue
    return True


my_signs = ['x', '0']
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
    my_signs = my_signs[::-1]
    continue





