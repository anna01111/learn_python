from tkinter import *


width = 600
height = 600

root = Tk()
root.geometry(f"{width}x{height}+250+250")


def move_a_man(event):
    c.move('man', 10, 10)
    c.itemconfig('man', fill="red", width=3)



canvas_height = 460

c = Canvas(width=600, height=canvas_height, bg='grey80')
c.grid(row=0, column=0, columnspan=3)

but = Button(text='move a man')
but.grid(row=1, column=1)

but.bind('<Button-1>', move_a_man)   # ліва кнопка

head = c.create_oval(300, 40, 330, 70, tag="man")
body = c.create_oval(290, 70, 340, 150, tag="man")
right_arm = c.create_line(340, 85, 380, 85, tag="man")
left_arm = c.create_line(290, 85, 250, 110, tag="man")

right_leg = c.create_line(325, 150, 325, 200, tag="man")
left_leg = c.create_line(305, 150, 305, 200, tag="man")


mainloop()
