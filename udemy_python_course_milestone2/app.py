from utils.database_sqlite import *

USER_CHOICE = """
Enter:

- 'a' to add anew book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

"""

operations = {
    'a': add_book,
    'l': list_books,
    'r': read_book,
    'd': delete_book
}


def menu():
    operation = input(USER_CHOICE)
    while operation != 'q':

        try:
            operations[operation]()
        except KeyError:
            print('Incorrect input')

        operation = input(USER_CHOICE)


menu()

