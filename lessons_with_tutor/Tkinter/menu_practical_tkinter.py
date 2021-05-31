from tkinter import *


def red():
    fra.configure(bg="red")


def green():
    fra.configure(bg="green")


def blue():
    fra.configure(bg="blue")


def five_per_five_hundred():
    fra.configure(height=500, width=500)
    root.geometry("500x500")


def seven_per_four_hundred():
    fra.configure(height=700, width=400)
    root.geometry("400x700")


def about():
    win = Toplevel(root)
    lab = Label(win, text="Це лейбел на новому вікні")
    lab.pack()


def help_():

    lab1.configure(text="Це лейбл на руті")


def exit_():
    root.destroy()


root = Tk()

lab1 = Label(root, bg="yellow")
lab1.pack()

fra = Frame(root, width=1000, height=1000, bd=50)
fra.pack()

m = Menu(root)  # создается объект Меню на главном окне
root.config(menu=m)  # окно конфигурируется с указанием меню для него

c = Menu(m)
m.add_cascade(label="Color", menu=c)
c.add_command(label="Red", command=red)
c.add_command(label="Green", command=green)
c.add_command(label="Blue", command=blue)


s = Menu(m)
m.add_cascade(label="Size", menu=s)
s.add_command(label="500x500", command=five_per_five_hundred)
s.add_command(label="700х400", command=seven_per_four_hundred)


o = Menu(m)
m.add_cascade(label="Other", menu=o)
o.add_command(label="About", command=about)
o.add_command(label="Help", command=help_)
o.add_command(label="Exit", command=exit_)


root.mainloop()

