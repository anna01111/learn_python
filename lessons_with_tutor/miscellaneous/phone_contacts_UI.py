from phone_contacts import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

print(contacts)
contact = []

changes_tracker = False

# создание нового окна
def ui_show_contacts(event):
    contacts_listbox.delete(0, END)
    for contact in contacts:
        contacts_listbox.insert(END, contact)


def ui_add_contact(event):
    global contact

    def add_contact_to_list(event):
        global contacts
        global changes_tracker
        try:
            contact = [tex.get(1.0, END).strip(), tex1.get(1.0, END).strip(), int(tex2.get(1.0, END)), tex3.get(1.0, END).strip()]
            print(contact)
            contacts.append(contact)
            print(contacts)
            top_l1.destroy()

            ui_show_contacts(event)
            changes_tracker = True

        except ValueError:
            showinfo("Notification",
                     "Please note:\nAll the fields must be filled \nand the 'Age' field must be a whole number")

    def enter_leave(event):
        template = "+38 063 0000000"
        x = tex3.get(1.0, END).strip()
        if str(event.type) == 'Enter' and x == template:
                tex3.delete(1.0, END)
        elif str(event.type) == 'Leave':
            x = tex3.get(1.0, END).strip()
            if not len(x):
                tex3.insert(1.0, template)

    top_l1 = Toplevel(root)
    top_l1.title("Add contact")
    top_l1.transient(root)  # – делаем его зависимым от главного окна
    top_l1.geometry("450x150")

    lab = Label(top_l1, text="Name", bg="beige")
    tex = Text(top_l1, width=30, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")

    lab1 = Label(top_l1, text="Surname", bg="beige")
    tex1 = Text(top_l1, width=30, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")

    lab2 = Label(top_l1, text="Age", bg="beige")
    tex2 = Text(top_l1, width=3, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")

    lab3 = Label(top_l1, text="Phone number", bg="beige")
    tex3 = Text(top_l1, width=15, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid", fg="gray")
    tex3.insert(1.0, "+38 063 0000000")

    but2 = Button(top_l1, text="ADD", bg="beige", padx=10, pady=10)  # ЗРОБИТИ КНОПКУ ЧЕРВОНОЮ
    but2.grid(row=0, column=2, rowspan=4, padx=15, pady=20)
    but2.bind("<Button-1>", add_contact_to_list)  # ліва кнопка

    lab.grid(row=0, column=0)
    tex.grid(row=0, column=1)

    lab1.grid(row=1, column=0)
    tex1.grid(row=1, column=1)

    lab2.grid(row=2, column=0)
    tex2.grid(row=2, column=1)

    lab3.grid(row=3, column=0)
    tex3.grid(row=3, column=1)

    tex3.bind('<Enter>', enter_leave)
    tex3.bind('<Leave>', enter_leave)


def ui_remove_contact(event):
    global contacts_listbox
    global contacts
    global changes_tracker
    selection = contacts_listbox.curselection()

    if selection:
        # мы можем получить удаляемый элемент по индексу
        selected_contact = contacts_listbox.get(selection[0])
        if askyesno(f"Remove {selected_contact}", "Удалять или нет?"):
            contacts_listbox.delete(selection[0])
    contacts = []
    for i in range(contacts_listbox.size()):
        contacts.append(list(contacts_listbox.get(i)))

    changes_tracker = True


def ui_sort(event):
    global changes_tracker
    print(contacts)
    sort_by_name()
    ui_show_contacts(event)

    changes_tracker = True


def ui_edit(event):
    global contacts_listbox
    global contacts
    global changes_tracker
    selection = contacts_listbox.curselection()

    if selection:
        selected_contact = list(contacts_listbox.get(selection[0]))

        def ui_edit_contact(event):
            global contacts

            print(selection[0])
            print(contacts_listbox.get(selection[0]))

            edited_contact = [tex.get(1.0, END).strip(), tex1.get(1.0, END).strip(), int(tex2.get(1.0, END)), tex3.get(1.0, END).strip()]
            contacts[selection[0]] = edited_contact

            top_l1.destroy()

            ui_show_contacts(event)

        top_l1 = Toplevel(root)
        top_l1.title("Edit contact")
        top_l1.transient(root)  # – делаем его зависимым от главного окна
        top_l1.geometry("450x150")

        lab = Label(top_l1, text="Name", bg="beige")
        tex = Text(top_l1, width=30, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")
        tex.insert(1.0, f"{selected_contact[0]}")

        lab1 = Label(top_l1, text="Surname", bg="beige")
        tex1 = Text(top_l1, width=30, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")
        tex1.insert(1.0, f"{selected_contact[1]}")

        lab2 = Label(top_l1, text="Age", bg="beige")
        tex2 = Text(top_l1, width=3, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")
        tex2.insert(1.0, f"{selected_contact[2]}")

        lab3 = Label(top_l1, text="Phone number", bg="beige")
        tex3 = Text(top_l1, width=15, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")
        tex3.insert(1.0, f"{selected_contact[3]}")

        but2 = Button(top_l1, text="SAVE", bg="beige", padx=10, pady=10)  # ЗРОБИТИ КНОПКУ ЧЕРВОНОЮ
        but2.grid(row=0, column=2, rowspan=4, padx=15, pady=20)
        but2.bind("<Button-1>", ui_edit_contact)  # ліва кнопка

        lab.grid(row=0, column=0)
        tex.grid(row=0, column=1)

        lab1.grid(row=1, column=0)
        tex1.grid(row=1, column=1)

        lab2.grid(row=2, column=0)
        tex2.grid(row=2, column=1)

        lab3.grid(row=3, column=0)
        tex3.grid(row=3, column=1)

    changes_tracker = True


def ui_save():
    with open(FILENAME, 'wb') as file:
        pickle.dump(contacts, file)
    showinfo("information", 'The changes have been saved')
    print(contacts)


def ui_save_as():
    sa = asksaveasfilename()
    try:
        with open(sa, 'wb') as file:
            pickle.dump(contacts, file)
    except FileNotFoundError:
        pass


def ui_load():
    global contacts
    contacts = load_from_file()


def ui_load_from_file():
    global contacts
    op = askopenfilename()
    try:
        with open(op, 'rb') as file:
            contacts = pickle.load(file)
    except FileNotFoundError:
        pass


def ui_exit():
    if askyesno("exit", "Do you really want to exit"):
        if changes_tracker:
            if askyesno("exit", "Do you want to save changes?"):
                ui_save()
        root.destroy()


root = Tk()
root.geometry("500x500")


but = Button(text="Show contacts")
but.grid(row=0, column=0)
but.bind("<Button-1>", ui_show_contacts)  # ліва кнопка

but1 = Button(text="Add contact")
but1.grid(row=0, column=1)
but1.bind("<Button-1>", ui_add_contact)  # ліва кнопка

but_remove = Button(text="Remove contact")
but_remove.grid(row=0, column=2)
but_remove.bind("<Button-1>", ui_remove_contact)  # ліва кнопка

but_sort = Button(text="Sort contacts")
but_sort.grid(row=3, column=0)
but_sort.bind("<Button-1>", ui_sort)  # ліва кнопка

but_edit = Button(text="Edit contact")
but_edit.grid(row=3, column=1)
but_edit.bind("<Button-1>", ui_edit)  # ліва кнопка


# создаем список
contacts_listbox = Listbox()
contacts_listbox.configure(width=30, height=20)
contacts_listbox.grid(row=1, column=1)


main_menu = Menu(root)

file_menu = Menu()

file_menu.add_command(label="Save", command=ui_save)
file_menu.add_command(label="Save As ...", command=ui_save_as)
file_menu.add_command(label="Load", command=ui_load)
file_menu.add_command(label="Load From File ...", command=ui_load_from_file)
file_menu.add_command(label="Exit", command=ui_exit)

main_menu.add_cascade(label="File", menu=file_menu)

root.config(menu=main_menu)


root.mainloop()



# поломався load from file - погуглити помилку

