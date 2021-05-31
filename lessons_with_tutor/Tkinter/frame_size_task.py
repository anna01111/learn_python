from tkinter import *


def size(event):
    try:
        fra.configure(height=height.get(), width=width.get())
    except TclError:
        pass


root = Tk()
root.geometry("300x300")

height = Entry()
width = Entry()

height.pack()
width.pack()


fra = Frame(root, width=300, height=300, bg="green", bd=50)
fra.pack()


root.bind("<space>", size)

root.mainloop()


