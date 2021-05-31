from tkinter import *


def put_text(event):
    s = entry.get()
    label.configure(text=s)


root = Tk()
root.geometry("300x300")

label = Label()
label.pack()

entry = Entry(root, width=20)
entry.pack()

root.bind("<Return>", put_text)


root.mainloop()



