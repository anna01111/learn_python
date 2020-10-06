from classes import Person, ContactList

USER_INPUT = """\nPlease enter\n
- 'l' to list contacts,
- 'a' to add a contact,
- 's' to sort,
- 'r' to remove,
- 'e' to edit,
- 'q' to exit\n
"""


p = Person('anna', 'loz', '0930000000', 28)

# initializing contact list
contact_list = ContactList()


def menu():
    print('Welcome to contact list')
    action = ''
    while action != 'q':

        contact_list.load_from_file()

        action = input(USER_INPUT)
        if action == 'l':
            contact_list.list_contacts()
        elif action == 'a':
            contact_list.add_contact()
        elif action == 's':
            contact_list.sort()
        elif action == 'r':
            contact_list.remove_contact()
        elif action == 'e':
            contact_list.edit_contact()
        elif action == 'q':
            print('Bye')
        else:
            print('Invalid input')

        contact_list.save_to_a_file()


menu()


