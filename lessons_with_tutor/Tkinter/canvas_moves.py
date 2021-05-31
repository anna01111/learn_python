from tkinter import *

width = 600
height = 600


def move_obj(event):
    c.move(rect, 0, 150)
    c.itemconfig(trian, outline="red", width=3)
    c.coords(oval, 300, 200, 450, 450)


def mooove(event):
    c.move(rect, 0, 2)


def color(event):
    c.itemconfig('group1',fill="red",width=3)


def clean(event):
    c.delete('all')


root = Tk()
root.geometry(f"{width}x{height}+250+250")

c = Canvas(width=460,height=460,bg='grey80')
c.pack()
c.bind('<Button-1>', mooove)  # ліва кнопка
c.bind('<Button-3>', color)   # середня кнопка
c.bind('<Button-2>', clean)  # права кнопка

oval = c.create_oval(30,10,130,80)
rect = c.create_rectangle(180,10,280,80)
trian = c.create_polygon(330,80,380,10,430,80, fill='grey80', outline="black")


but = Button(text='move objects')
but.pack()
but.bind("<Button-1>", move_obj)  # ліва кнопка


oval1 = c.create_oval(30,10,130,80,tag="group1")
c.create_line(10,100,450,100,tag="group1")


root.mainloop()
