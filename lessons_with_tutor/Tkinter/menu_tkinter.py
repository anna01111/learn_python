


from tkinter import *
from tkinter import messagebox


def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")


root = Tk()


root.title("GUI на Python")
root.geometry("300x250")

main_menu = Menu(root)

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save", command=edit_click)
file_menu.add_separator()

file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu, command=edit_click)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()




