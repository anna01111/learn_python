from tkinter import *

width = 400
height = 250

root = Tk()
root.geometry(f"{width}x{height}+250+250")

canv = Canvas(root, width=width, height=height, bg="white", cursor="pencil", highlightthickness=5, highlightbackground="blue")
canv.pack()

# rectangles
canv.create_rectangle(120, 30, 135, 85, fill="lightgreen", outline="black")

n = 0
for i in range(11):
    canv.create_rectangle(190, 30+n, 205, 45+n, fill="yellow", outline="black")
    n += 15

canv.create_rectangle(260, 30, 275, 115, fill="lightblue", outline="black")

# texts
canv.create_text(129, 20, text='F1', font="Verdana 15", fill="black")
canv.create_text(199, 20, text='P', font="Verdana 15", fill="black")
canv.create_text(269, 20, text='F2', font="Verdana 15", fill="black")

# side texts
canv.create_text(300, 175, text='P - main program', font="Verdana 15", fill="black")
canv.create_text(300, 195, text='F1 - function 1', font="Verdana 15", fill="black")
canv.create_text(300, 215, text='F2 - function 2', font="Verdana 15", fill="black")

# lines
canv.create_line(205, 85, 240, 85, width=2, fill="black")
canv.create_line(240, 85, 240, 40, width=2, fill="black")
canv.create_line(240, 40, 260, 40, width=2, fill="black", arrow=LAST)

canv.create_line(190, 160, 60, 160, width=2, fill="black")
canv.create_line(60, 160, 60, 40, width=2, fill="black")
canv.create_line(60, 40, 120, 40, width=2, fill="black", arrow=LAST)

canv.create_line(190, 55, 160, 55, width=2, fill="black")
canv.create_line(160, 55, 160, 40, width=2, fill="black")
canv.create_line(160, 40, 135, 40, width=2, fill="black", arrow=LAST)

root.mainloop()

