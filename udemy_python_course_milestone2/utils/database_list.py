
"""Concerned with storing and retrieving books from a python list"""

# book format -> {'name': 'Harry Potter', 'author': 'Joanne Rowling', 'read': False}

books = []


def add_book():
    name = input('Enter name:\n')
    author = input('Enter author:\n')
    books.append({'name': name, 'author': author, 'read': False})
    print('Book successfully added')


def list_books():
    for book in books:
        print(book)


def read_book():
        user_input = input('Enter name of a book you want to mark as read:\n')
        for book in books:
            if book['name'] == user_input:
                book['read'] = True
                print('Book successfully marked as read')
                break
        else:
            print('No book with such name')


def delete_book():
    global books
    user_input = input('Enter name of a book you want to delete:\n')
    len_books_old = len(books)
    books = [book for book in books if book['name'] != user_input]
    if len_books_old > len(books):
        print('Book successfully deleted')
    else:
        print('No book with such name')













