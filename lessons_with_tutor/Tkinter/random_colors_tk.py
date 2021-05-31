from tkinter import *
import random


def random_color():
    return random.randint(0, 0x1000000)


tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

for x in range(0, 40):

    color = '{:06x}'.format(random_color())
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    x2 = random.randint(0, 400)
    y2 = random.randint(0, 400)
    x3 = random.randint(0, 400)
    y3 = random.randint(0, 400)
    my_triangle = canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=('#'+color), outline="red")

    print('{:x}'.format(0x10))
tk.mainloop()

