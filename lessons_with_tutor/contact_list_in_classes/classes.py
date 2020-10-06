import pickle
from operator import itemgetter, attrgetter, methodcaller

FILENAME = 'contacts.dat'


class Person:
    def __init__(self, name: str, surname: str, number: str, age: str):
        self.name = name
        self.surname = surname
        self.number = number
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.surname}, number: {self.number}, age: {self.age}.'

    def __gt__(self, other):
        return self.name > other

    def __lt__(self, other):
        return self.name < other

    def edit_contact(self, new_name: str, new_surname: str, new_number: str, new_age: str):

        # if the value we get from user is empty = we don't change the field and leave it as it was
        if new_name:
            self.name = new_name
        if new_surname:
            self.surname = new_surname
        if new_number:
            self.number = new_number
        if new_age:
            self.age = new_age


class ContactList:
    def __init__(self):
        self.l = []

    def __repr__(self):
        return 'This is a contacts list'

    @property
    def contact_list_is_empty(self):
        return len(self.l) == 0

    def list_contacts(self):
        if self.contact_list_is_empty:
            print('Contact list is empty')
        else:
            for index, person in enumerate(self.l):
                print(f'id: {index + 1}, {person}')  # adding 1 to make the list start from 1 and be more user-readable

    @staticmethod
    def get_user_input() -> list:
        name = input("Please enter name: ")
        surname = input("Please enter surname: ")
        phone_number = input("Please enter phone number: ")
        age = input("Please enter age: ")
        return [name, surname, phone_number, age]

    def add_contact(self):
        person = Person(*self.get_user_input())
        self.l.append(person)

    def edit_contact(self):
        try:
            # handling situation when contact list is empty
            if self.contact_list_is_empty:
                raise Warning

            # showing contact list
            self.list_contacts()

            # taking user input
            user_input = int(input('Please enter id of a contact you want to edit: '))
            print("If you don't want to change some field - leave it empty")

            # handling situation when we get index -1 or -2 etc and thus unwillingly delete element from a list
            if user_input < 1:
                raise ValueError

            # editing an element
            # subtracting 1 as we've added it before in list_contacts() for user convenience's sake
            self.l[user_input - 1].edit_contact(*self.get_user_input())

        except (IndexError, ValueError):
            print("You've entered incorrect id")
        except Warning:
            print('Contact list is empty')
        else:
            print('Edited successfully')

    def remove_contact(self):
        try:
            # handling situation when contact list is empty
            if self.contact_list_is_empty:
                raise Warning

            # showing contact list
            self.list_contacts()

            # taking user input
            user_input = int(input('Please enter id of a contact you want to remove: '))

            # handling situation when we get index -1 or -2 etc and thus unwillingly delete element from a list
            if user_input < 1:
                raise ValueError

            # deleting the element
            self.l.pop(user_input - 1)  # subtracting 1 as we've added it before in list_contacts() for user convenience

        except (IndexError, ValueError):
            print("You've entered incorrect id")
        except Warning:
            print('Contact list is empty')
        else:
            print('Removed successfully')

    def sort_by_name(self):
        self.l = sorted(self.l, key=lambda person: person.name)

    def sort_by_surname(self):
        self.l = sorted(self.l, key=lambda person: person.surname)

    def sort_by_number(self):
        self.l = sorted(self.l, key=lambda person: person.number)

    def sort_by_age(self):
        self.l = sorted(self.l, key=lambda person: person.age)

    def sort(self):
        line = """
        Enter number representing by which filed you want to sort:
        1 - name,
        2 - surname,
        3 - number,
        4 - age
        """
        action = input(line)
        if action == '1':
            self.sort_by_name()
        elif action == '2':
            self.sort_by_surname()
        elif action == '3':
            self.sort_by_number()
        elif action == '4':
            self.sort_by_age()

    def save_to_a_file(self):
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.l, file)

    def load_from_file(self):
        try:
            with open(FILENAME, 'rb') as file:
                self.l = pickle.load(file)
        except FileNotFoundError:
            pass

