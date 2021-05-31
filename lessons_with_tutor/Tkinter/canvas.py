from tkinter import *

root = Tk( )

root.title("Виджет Canvas, рисование ")
root.geometry("800x800+250+250")

can = Canvas(root)
can.pack(expand = YES, fill = BOTH)

can.create_line(20, 100, 200, 60, fill = 'red', width = 3)
can.create_arc(30,150,300,310, fill = 'blue')
can.create_rectangle(300,10, 350,40, width = 2, fill = 'green')
can.create_rectangle(10,10, 150,40, width = 3, outline = 'black')
can.create_polygon(50,200,10,300,70,255,fill = 'magenta')

can.create_line(0,0,100,100,width=2,arrow=LAST)

x=75
y=110
can.create_rectangle(x,y,x+80,y+50,fill="yellow",outline="blue")

can.create_polygon([250,100],[200,150],[300,150],fill="yellow")

can.create_oval([20,200],[150,300],fill="gray50")


can.create_arc([160,230],[230,330],start=0,extent=270,fill="lightgreen")
can.create_arc([250,230],[320,330],start=0,extent=140,style=CHORD,fill="green")
can.create_arc([340,230],[410,330],start=0,extent=140,style=ARC,outline="darkgreen",width=2)

can.create_text(20,330,text="Опыты с графическими примитивами\nна холсте",font="Verdana 12",
                anchor="w",justify=CENTER,fill="red")

x=10
while x < 450:
    can.create_rectangle(x,400,x+50,450)
    x = x + 60

root.mainloop( )