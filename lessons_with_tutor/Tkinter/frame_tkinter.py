from tkinter import *

TEXT= "Ukraine (Ukrainian: Україна, romanized: Ukrayina, pronounced [ʊkrɐˈjinɐ] (About this soundlisten); Russian: Украина, tr. Ukraina, IPA: [ʊkrɐˈinə]) is a country in Eastern Europe. It is bordered by Russia to the east and north-east; Belarus to the north; Poland, Slovakia and Hungary to the west; and Romania, Moldova"
root = Tk()

fra2 = Frame(root,width=300,height=200,bg="green",bd=50)
fra3 = Frame(root,width=500,height=350,bg="darkblue",bd=20)
fra4 = Frame(root,width=500,height=1,bg="white",bd=20)

fra2.grid(row=0, column=0)
fra3.grid(row=1, column=0)
fra4.grid(row=2, column=0)

ent1 = Entry(fra3,width=20)
ent1.pack()

sca1 = Scale(fra2,orient=HORIZONTAL,length=300, from_=0,to=100,tickinterval=10,resolution=5)
sca1.pack()

tex = Text(fra4, width=40, height=3, font="Verdana 12", wrap=WORD, bg="lightyellow", padx=5, pady=5, bd=10, )
tex.insert(1.0, TEXT)
tex.grid(row=2, column=0)

scroll = Scrollbar(command=tex.yview)
scroll.grid(row=2, column=1)

tex.config(yscrollcommand=scroll.set)

root.mainloop()
