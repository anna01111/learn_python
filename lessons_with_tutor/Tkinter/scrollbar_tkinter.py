from tkinter import *
root = Tk()
root.geometry("500x500")

tx = Text(root,width=40,height=3,font='14', bg="red")
scr = Scrollbar(root,command=tx.xview)
tx.configure(yscrollcommand=scr.set)

tx.grid(row=0,column=0)
scr.grid(row=0,column=1)
root.mainloop()