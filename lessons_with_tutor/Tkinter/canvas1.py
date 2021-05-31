from tkinter import *
import random


def random_color():
    return random.randint(0, 0x1000000)


def draw_squares(event):

    n = int(ent.get())
    print(n)
    size_of_square = (width - 3)/n

    # up left to bottom right
    x = 3
    while x < width:
        color = '{:06x}'.format(random_color())
        canv2.create_rectangle(x, x, x + size_of_square, x + size_of_square, fill=('#'+color))
        x = x + size_of_square


def clear_squares(event):
    canv2.delete('all')


root = Tk()
root.geometry("600x1200+250+250")

width = 502
height = 502

canv2 = Canvas(root, width=width, height=height, bg="lightblue", cursor="pencil")
canv2.pack()

ent = Entry()
ent.pack()

but = Button(root, text="enter number")
but.pack()
but.bind("<Button-1>", draw_squares)  # ліва кнопка

but2 = Button(root, text="clear canvas")
but2.pack()
but2.bind("<Button-1>", clear_squares)  # ліва кнопка

canv = Canvas(root, width=width, height=height, bg="lightblue", cursor="pencil")
canv.pack()

# up left to bottom right
x = 3
while x < width:
    canv.create_rectangle(x, x, x+100, x+100, fill='red')
    x = x + 100

# up left to bottom right
x = width - 3
while x > 3:
    canv.create_rectangle(x, x, x - 100, x - 100, fill='green')
    x = x - 100

# bottom right to up left
y = width
x = 3
while x < width:
    canv.create_rectangle(x, y, x+100, y - 100, fill='yellow')
    x = x + 100
    y = y - 100







root.mainloop()

# зробити на другій канві можливість намалювати нну кількість квадрітів, чисто н вводить користувач