

class Person:
    def __init__(self, name: str, surname: str, number: str, age: int):
        self.name = name
        self.surname = surname
        self.number = number
        self.age = age

    def __str__(self):
        return f'{self.name} {self.surname}, number: {self.number}, age: {self.age}'

    def edit_contact(self):
        pass


class ContactList:
    def __init__(self):
        self.l = [Person('ania', 'loz', '0000000', 25), Person('olia', 'loz', '111111', 20)]

    def __str__(self):
        return 'This is a contacts list'

    @property
    def contact_list_is_empty(self):
        return len(self.l) == 0

    def show_contacts(self):
        if self.contact_list_is_empty:
            print('Contact list is empty')
        else:
            for index, person in enumerate(self.l):
                print(f'id: {index + 1}, {person}')  # adding 1 to make the list start from 1 and be more user-readable

    def add_contact(self):
        name = input("Please enter name: ")
        surname = input("Please enter surname: ")
        while True:
            try:
                age = int(input("Please enter age: "))
                break  # we get out of a loop once we get no error in the line above
            except ValueError:
                print("Error - input must be a whole number. Please try again: ")
        phone_number = input("Please enter phone number: ")

        person = Person(name, surname, phone_number, age)
        self.l.append(person)

    def remove_contact(self):
        try:
            # handling situation when contact list is empty
            if self.contact_list_is_empty:
                raise Warning

            # showing contact list
            self.show_contacts()

            # taking user input
            user_input = int(input('Please enter id of a contact you want to remove: '))

            # handling situation when we get index -1 or -2 etc and thus unwillingly delete element from a list
            if user_input < 1:
                raise ValueError

            # deleting the element
            self.l.pop(user_input - 1)  # subtracting 1 as we've added it before in show_contacts() for user convenience

        except (IndexError, ValueError):
            print("You've entered incorrect id")
        except Warning:
            print('Contact list is empty')
        else:
            print('Deleted successfully')

    def sort_by_name(self):
        pass

