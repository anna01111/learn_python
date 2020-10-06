import sqlite3
import os

"""Concerned with storing and retrieving books from a sqlite db
Names of the books must be unique, as they are used as a table's primary key"""

# book format -> {'name': 'Harry Potter', 'author': 'Joanne Rowling', 'read': False}


def create_file_if_not_exists() -> None:
    if not os.path.exists('/data.db'):
        with sqlite3.connect('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
            connection.commit()


def add_book() -> None:
    name = input('Enter name:\n')
    author = input('Enter author:\n')
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        try:
            # '?' syntax protects against sql injection
            cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
            connection.commit()
        except sqlite3.IntegrityError:
            print('Book with the given name already exists')


def list_books() -> None:
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()  # -> [(name, author, read), (name, author, read) etc]
        books = [{'name': book[0], 'author': book[1], 'read': book[2]} for book in books]
        for book in books:
            print(book)


def read_book() -> None:
    user_input = input('Enter name of a book you want to mark as read:\n')
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE books SET read=1 WHERE name=?', (user_input,))
        connection.commit()


def delete_book() -> None:
    user_input = input('Enter name of a book you want to remove:\n')
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        # notice how we use a comma to write a tuple of one element
        cursor.execute(f'DELETE FROM books WHERE name=?', (user_input,))


# initializing db
create_file_if_not_exists()


