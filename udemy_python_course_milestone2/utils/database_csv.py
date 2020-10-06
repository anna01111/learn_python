import csv
from distutils.util import strtobool

"""Concerned with storing and retrieving books from a csv file"""

# book format -> {'name': 'Harry Potter', 'author': 'Joanne Rowling', 'read': False}

books = []


def _read_from_file():
    global books
    try:
        with open('books.csv', 'r') as f:
            books = list(csv.DictReader(f))

        # here we convert str 'False' or 'True' to a bool False or True
        # strtobool() is taken from distutils standard library module
        for book in books:
            book['read'] = bool(strtobool(book['read']))
    except FileNotFoundError:
        pass


def _write_to_file():
    global books
    with open('books.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'author', 'read'])
        writer.writeheader()
        writer.writerows(books)


def add_book():
    _read_from_file()
    name = input('Enter name:\n')
    author = input('Enter author:\n')
    books.append({'name': name, 'author': author, 'read': False})
    _write_to_file()
    print('Book successfully added')


def list_books():
    _read_from_file()
    for book in books:
        print(book)


def read_book():
    _read_from_file()
    user_input = input('Enter name of a book you want to mark as read:\n')
    for book in books:
        if book['name'] == user_input:
            book['read'] = True
            _write_to_file()
            print('Book successfully marked as read')
            break
    else:
        print('No book with such name')


def delete_book():
    global books
    _read_from_file()
    user_input = input('Enter name of a book you want to delete:\n')
    len_books_old = len(books)
    books = [book for book in books if book['name'] != user_input]
    if len_books_old > len(books):
        _write_to_file()
        print('Book successfully deleted')
    else:
        print('No book with such name')


