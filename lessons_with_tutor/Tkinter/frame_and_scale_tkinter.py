
from tkinter import *


def color(event):
    c = sca.get()
    fra.configure(bg=f"#{c}")


root = Tk()

sca = Scale(root, orient=HORIZONTAL, length=300, from_=100, to=999, tickinterval=100, resolution=1)
sca.pack()

sca.set(10)
print(sca.get())

fra = Frame(root, width=500, height=100, bg="#009")
fra.pack()

but = Button(text="set color")
but.bind('<Button-1>', color)
but.pack()

root.mainloop()

# ми закінчили на    Урок 10

