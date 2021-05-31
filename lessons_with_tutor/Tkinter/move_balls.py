from tkinter import *

width = 600
height = 600
canvas_height = 460


counter = width - 20
r = -1


def initialize_move(event):
    global r
    global counter
    c.move(ball, r, 0)
    counter -= 1

    if counter >= 0:
        c.after(entry.get(), initialize_move, counter)
    else:
        counter = width - 20
        r = r * -1
        c.after(10, initialize_move, counter)


koef = width / canvas_height

x = 1 * koef
y = - 1

counter2 = canvas_height # по ігреку


def initialize_move_diagonal(event):
    global koef
    global counter2
    global x
    global y
    c.move(ball2, x, y)
    counter2 -= 1

    if counter2 >= 0:
        c.after(entry.get(), initialize_move_diagonal, counter2)
    else:
        counter2 = canvas_height
        x = x * -1
        y = y * -1

        c.after(entry.get(), initialize_move_diagonal, counter2)





def stop(event):
    pass


root = Tk()
root.geometry(f"{width}x{height}+250+250")


c = Canvas(width=600, height=canvas_height, bg='grey80')
c.grid(row=0, column=0, columnspan=3)

but = Button(text='move green ball (enter time in miliseconds)')
but.grid(row=1, column=1)
but.bind('<Button-1>', initialize_move)   # ліва кнопка

entry = Entry()
entry.insert(0, '1')
entry.grid(row=1, column=2)

but0 = Button(text='stop a ball')
but0.grid(row=2, column=1)
but0.bind('<Button-1>', stop)   # ліва кнопка

ball = c.create_oval(600, 240, 590, 250, fill="green")


# second ball

ball2 = c.create_oval(2, 440, 22, 460, fill="yellow")

but2 = Button(text='move yellow ball (enter time in miliseconds)')
but2.grid(row=4, column=1)
but2.bind('<Button-1>', initialize_move_diagonal)   # ліва кнопка

entry2 = Entry()
entry2.insert(0, '1')
entry2.grid(row=4, column=2)




mainloop()


