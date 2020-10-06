
"""
from tkinter import *
from tkinter import messagebox


def show_message():
    messagebox.showinfo("GUI Python", message.get())


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Click Me", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()
"""



"""
from tkinter import *
from tkinter import messagebox


def display_full_name():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())


root = Tk()
root.title("GUI на Python")

name = StringVar()
surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text="Click Me", command=display_full_name)
message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
"""

from tkinter import *
from tkinter import messagebox


def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)


def display():
    messagebox.showinfo("GUI Python", name_entry.get() + " " + surname_entry.get())


root = Tk()
root.title("GUI на Python")

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry()
surname_entry = Entry()

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

# вставка начальных данных
name_entry.insert(0, "Tom")
surname_entry.insert(0, "Soyer")

display_button = Button(text="Display", command=display)
clear_button = Button(text="Clear", command=clear)

display_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
