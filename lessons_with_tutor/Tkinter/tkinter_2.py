from tkinter import *
"""
clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.place(x=30, y=125, anchor="c", height=100, width=100, bordermode=OUTSIDE)

root.mainloop()
"""


"""

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn1 = Button(text="x=10, y=20", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
btn1.place(x=10, y=20)

btn2 = Button(text="x=50, y=100", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
btn2.place(x=50, y=100)

btn3 = Button(text="x=140, y=160", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
btn3.place(x=140, y=160)

root.mainloop()

"""

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

for r in range(3):
    for c in range(3):
        btn = Button(text="{}-{}".format(r, c))
        btn.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)

root.mainloop()