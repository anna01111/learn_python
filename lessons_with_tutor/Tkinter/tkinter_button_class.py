from tkinter import *


class But_print:

    def __init__(self, number):
        self.number = number
        self.but = Button(root, width=30, height=5, bg="white", fg="blue")
        self.but["text"] = f"Печать {self.number}"
        self.but.bind("<Button-1>", self.printer)
        self.but.pack()

    def printer(self,event):
        print(f"Как всегда очередной 'Hello World!' {self.number}")


root = Tk()
# root.geometry("400x400")

lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")
lab.pack()

tex = Text(root, width=10, height=5, font="Verdana 20", wrap=WORD, bg="grey", fg="white")
tex.pack()


var = IntVar()
var.set(0)
rad0 = Radiobutton(root, text="Первая", variable=var, value=0)
rad1 = Radiobutton(root, text="Вторая", variable=var, value=1)
rad2 = Radiobutton(root, text="Третья", variable=var, value=2)
rad0.pack()
rad1.pack()
rad2.pack()


c1 = IntVar()
c2 = IntVar()
che1 = Checkbutton(root, text="Первый флажок", variable=c1, onvalue=1, offvalue=0)
che2 = Checkbutton(root, text="Второй флажок", variable=c2, onvalue=2, offvalue=0)
che1.pack()
che2.pack()


r = ['Linux', 'Python', 'Tk', 'Tkinter']
lis = Listbox(root, selectmode=SINGLE, height=4)
for i in r:
    lis.insert(END, i)
lis.pack()


lst = []
for i in range(2):
    lst.append((But_print(i)))

root.mainloop()
