import json

"""Concerned with storing and retrieving books from a json file"""

# book format -> {'name': 'Harry Potter', 'author': 'Joanne Rowling', 'read': False}

books = []


def _read_from_file():
    global books
    try:
        with open('books.json', 'r') as f:
            books = list(json.load(f))
    except FileNotFoundError:
        pass


def _write_to_file():
    global books
    with open('books.json', 'w') as f:
        json.dump(books, f)


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


