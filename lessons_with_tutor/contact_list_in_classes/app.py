from classes import Person, ContactList


p = Person('anna', 'loz', '0930000000', 28)
contact_list = ContactList()



def menu():
    print('Welcome to contact list')
    action = ''
    while action != 'q':
        action = input('Please enter s to show contacts, a to add a contact, sr to sort, r to remove, e to edit, q to exit: ')
        if action == 's':
            contact_list.show_contacts()
        if action == 'a':
            contact_list.add_contact()
        if action == 'sr':
            contact_list.sort_by_name()
        if action == 'r':
            contact_list.remove_contact()
        if action == 'e':
            contact_list.edit_contact()
        if action == 'q':
            #save_to_a_file()
            print('Bye')


menu()