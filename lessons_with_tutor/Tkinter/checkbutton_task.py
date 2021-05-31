from tkinter import *


def checkbuttons_active(event):
    tex.delete(1.0, END)

    res = ""
    if c1.get():
        res += f"Первый флажок "
    if c2.get():
        res += f"Второй флажок  "
    tex.insert(1.0, res)


def checkbuttons_passive(event):
    tex.delete(1.0, END)
    res = ""
    if not c1.get():
        res += f"Первый флажок "
    if not c2.get():
        res += f"Второй флажок "
    tex.insert(1.0, res)


root = Tk()
root.geometry("300x300")


c1 = IntVar()
c2 = IntVar()
che1 = Checkbutton(root,text="Первый флажок", variable=c1,onvalue=1,offvalue=0)
che2 = Checkbutton(root,text="Второй флажок",variable=c2,onvalue=2,offvalue=0)

che1.pack()
che2.pack()

tex = Text(root, width=40, height=3, font="Verdana 12", wrap=WORD, bg="yellow", padx=5, pady=5, bd=10, )
tex.pack()


tex.bind("<Button-1>", checkbuttons_active)  # ліва кнопка
tex.bind("<Button-2>", checkbuttons_passive)  # права кнопка


root.mainloop()
