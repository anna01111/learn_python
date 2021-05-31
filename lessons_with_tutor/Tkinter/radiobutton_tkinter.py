from tkinter import *

root = Tk()

var = IntVar()
var.set(1)

rad0 = Radiobutton(root,text="Первая",variable=var,value=0)
rad1 = Radiobutton(root,text="Вторая",variable=var,value=1)
rad2 = Radiobutton(root,text="Третья",variable=var,value=2)
rad0.pack()
rad1.pack()
rad2.pack()


def display(event):
    v = var.get()
    if v == 0:
        print("Включена первая кнопка")
    elif v == 1:
        print("Включена вторая кнопка")
    elif v == 2:
        print("Включена третья кнопка")


but = Button(root, text="Получить значение")
but.bind('<Button-1>', display)
but.pack()


root.mainloop()
