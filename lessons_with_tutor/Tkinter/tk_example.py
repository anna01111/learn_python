from tkinter import *


def new_window():
    next_win = Toplevel(root)  # создание нового окна
    next_win.transient(root)  # – делаем его зависимым от главного окна

    next_win.geometry("300x340+50+430")
    next_win.config(bg="beige")

    lab2 = Label(next_win, text="Сколько штук?", font="Arial 16", bg="beige")
    lab2.pack()

    var = IntVar()
    var.set(1)
    rad0 = Radiobutton(next_win, text="0-10", variable=var, value=0, bg="beige")
    rad1 = Radiobutton(next_win, text="11-20", variable=var, value=1, bg="beige")
    rad2 = Radiobutton(next_win, text="21-30", variable=var, value=2, bg="beige")
    rad3 = Radiobutton(next_win, text="31-40", variable=var, value=3, bg="beige")

    rad0.pack()
    rad1.pack()
    rad2.pack()
    rad3.pack()

    lab3 = Label(next_win, text="Какого цвета?", font="Arial 16", bg="beige")
    lab3.pack()

    c1 = IntVar()
    c2 = IntVar()
    c3 = IntVar()
    c4 = IntVar()
    che1 = Checkbutton(next_win, text="RED", variable=c1, onvalue=1, offvalue=0, bg="red")
    che2 = Checkbutton(next_win, text="BLUE", variable=c2, onvalue=2, offvalue=0, bg="blue")
    che3 = Checkbutton(next_win, text="GREEN", variable=c3, onvalue=3, offvalue=0, bg="green")
    che4 = Checkbutton(next_win, text="YELLOW", variable=c4, onvalue=4, offvalue=0, bg="yellow")

    che1.pack()
    che2.pack()
    che3.pack()
    che4.pack()



root = Tk()
root.geometry("400x400+0+0")
root.config(bg="beige")

lab = Label(root, text="Ваш адрес:", font="Arial 18", bg="lightyellow")
lab.pack()

entry = Entry(root, width=16, font="Arial 18", bg="lightyellow", bd=3)
entry.pack()

lab1 = Label(root, text="Комментарий", font="Arial 18", bg="beige")
lab1.pack()

tex = Text(root, width=18, height=5, font="Verdana 20", wrap=WORD, bg="white", fg="black")
tex.pack()

but = Button(root, text="ОТПРАВИТЬ", padx="20", pady="8", fg="blue", bg="white", command=new_window)
but.pack()







root.mainloop()