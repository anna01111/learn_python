from tkinter import *

width = 600
height = 600
canvas_height = 460


counter_ball = width - 20
counter_ball_1 = 2
r = -1


def move_ball(event):
    global r
    global counter_ball
    global counter_ball_1
    c.move(ball, r, 0)
    c.move(ball_1, -r, 0)
    counter_ball -= 1
    counter_ball_1 += 1

    update_time = entry.get()

    if abs(counter_ball - counter_ball_1) >= 4:
        c.after(update_time, move_ball, counter_ball)
    else:
        counter_ball = width - 20
        counter_ball_1 = 2
        r = r * -1
        c.after(update_time, move_ball, counter_ball)


root = Tk()
root.geometry(f"{width}x{height}+250+250")


c = Canvas(width=600, height=canvas_height, bg='grey80')
c.grid(row=0, column=0, columnspan=3)


lab = Label(text='enter speed for GREEN ball (must be a number)')
lab.grid(row=1, column=0)
entry = Entry()
entry.insert(0, '1')
entry.grid(row=1, column=1)


lab2 = Label(text='enter speed for YELLOW ball (must be a number)')
lab2.grid(row=4, column=0)
entry2 = Entry()
entry2.insert(0, '1')
entry2.grid(row=4, column=1)

but = Button(text='start moving')
but.grid(row=5, column=0)
but.bind('<Button-1>', move_ball)   # ліва кнопка


ball = c.create_oval(600, 240, 590, 250, fill="green")
ball_1 = c.create_oval(2, 240, 12, 250, fill="yellow")

print(10/4**3.0)


mainloop()
