
from tkinter import *

li = ["red","green"]
si = ["200x200", "400x400"]
si_fr = [100, 200]


def color(event):
    fra.configure(bg=li[0])
    li[0], li[1] = li[1], li[0]


def outgo(event):
    root.destroy()


def size(event):
    root.geometry(si[0])
    si[0], si[1] = si[1], si[0]


def frame_size_height(event):
    fra.configure(height=200)


def frame_size_width(event):
    fra.configure(width=200)


def frame_size_all(event):
    fra.configure(height=si_fr[0], width=si_fr[0])
    si_fr[0], si_fr[1] = si_fr[1], si_fr[0]


root = Tk()


fra = Frame(root,width=100,height=100)
but = Button(root,text="Выход")

but2 = Button(root,text="Управление фреймом")

fra.pack()
but.pack()
but2.pack()

root.bind("<Return>",color)
but.bind("<Button-1>",outgo)

root.bind("<space>", size)

but2.bind("<Button-1>", frame_size_height)  # ліва кнопка
but2.bind("<Button-2>", frame_size_width)  # права кнопка
but2.bind("<Button-3>", frame_size_all)  # середня кнопка


root.mainloop()
