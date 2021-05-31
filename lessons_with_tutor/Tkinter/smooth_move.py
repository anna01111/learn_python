import tkinter as tk


def smooth_motion(counter):
     canvas.move(disc, 0, dy)
     counter -= 1
     if counter >= 0:
         canvas.after(10, smooth_motion, counter)

root = tk.Tk()
canvas = tk.Canvas(root, bg='cyan')
canvas.pack()

counter = 200
disc = canvas.create_oval(200, 0, 210, 10, fill='green')
dy = (100 - 0) / counter
smooth_motion(counter)

root.mainloop()