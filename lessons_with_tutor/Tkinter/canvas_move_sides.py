from tkinter import *

zero_count = 5
x = zero_count
y = zero_count

step = 10


def move_up(event):
    global y
    if y > zero_count:
        c.move(oval, 0, -step)
        y -= step
    print(y)


def move_down(event):
    global y
    if y < canvas_height - oval_size - zero_count:
        c.move(oval, 0, step)
        y += step
    print(y)


def move_left(event):
    global x
    if x > zero_count:
        c.move(oval, - step, 0)
        x -= step


def move_right(event):
    global x
    if x < width - oval_size - zero_count:
        c.move(oval, step, 0)
        x += step
    print(x)

width = 600
height = 600

root = Tk()
root.geometry(f"{width}x{height}+250+250")

canvas_height = 460

c = Canvas(width=600, height=canvas_height, bg='grey80')
c.grid(row=0, column=0, columnspan=3)

oval_size = 150

oval = c.create_oval(x, y, x + oval_size, y + oval_size)

oval2 = c.create_oval(x, y, x + 2, y + 2)

but_up = Button(text='^')
but_up.bind('<Button-1>', move_up)  # ліва кнопка

but_down = Button(text='|')
but_down.bind('<Button-1>', move_down)  # ліва кнопка

but_left = Button(text='<-')
but_left.bind('<Button-1>', move_left)  # ліва кнопка

but_right = Button(text='->')
but_right.bind('<Button-1>', move_right)  # ліва кнопка

but_left.grid(row=2, column=0)

but_up.grid(row=1, column=1)

but_down.grid(row=3, column=1)

but_right.grid(row=2, column=2)



mainloop()



