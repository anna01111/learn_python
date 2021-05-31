from tkinter import *

root = Tk()
fra1 = Frame(root,width=500,height=500,bg="lightgreen")
fra3 = Frame(root,width=250,height=150,bg="darkgreen")

fra1.pack()
fra3.pack()


ent1 = Entry(fra3,width=20)
ent1.pack()

sca1 = Scale(fra1,orient=HORIZONTAL,length=300, from_=0,to=100,tickinterval=10,resolution=5)
sca1.pack()


root.mainloop()