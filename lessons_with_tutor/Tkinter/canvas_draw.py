from tkinter import *

width = 400
height = 250

root = Tk()
root.geometry(f"{width}x{height + 50}+250+250")


def show_x_and_y(event):
    step2 = cell_height * 1.5
    for i in range(num_of_rows - 1):
        canv.create_text(cell_width * 2.5, step2, text=col3[i], font="Verdana 20", fill="black")
        step2 += cell_height


def show_x_or_y(event):
    step2 = cell_height * 1.5
    for i in range(num_of_rows - 1):
        canv.create_text(cell_width * 3.5, step2, text=col4[i], font="Verdana 20", fill="black")
        step2 += cell_height


but1 = Button(text='X and Y')
but1.pack()
but2 = Button(text='X or Y')
but2.pack()

but1.bind("<Button-1>", show_x_and_y)  # ліва кнопка
but2.bind("<Button-1>", show_x_or_y)  # ліва кнопка

canv = Canvas(root, width=width, height=height, bg="white", cursor="pencil")
canv.pack()

num_of_columns = 4
num_of_rows = 5

cell_width = width / num_of_columns
cell_height = height / num_of_rows

for i in range(num_of_columns - 1):
    canv.create_line(cell_width*(i+1), 0, cell_width*(i+1), height, width=2, fill="black")

for i in range(num_of_rows - 1):
    canv.create_line(0, cell_height*(i+1), width, cell_height*(i+1), width=2, fill="black")

LABELS = ['X', 'Y', 'X and Y', 'X or Y']

step = cell_width/2
for i in range(num_of_columns):

    canv.create_text(step, cell_height/2, text=LABELS[i], font="Verdana 20", fill="black")
    step += cell_width

col1 = [0, 0, 1, 1]
step2 = cell_height*1.5
for i in range(num_of_rows - 1):

    canv.create_text(cell_width/2, step2, text=col1[i], font="Verdana 20", fill="black")
    step2 += cell_height

col2 = [0, 1, 0, 1]
step2 = cell_height*1.5
for i in range(num_of_rows - 1):

    canv.create_text(cell_width*1.5, step2, text=col2[i], font="Verdana 20", fill="black")
    step2 += cell_height


col3 = []
col4 = []
for i in range(num_of_rows - 1):
    col3.append(col1[i] & col2[i])
    col4.append(col1[i] | col2[i])


print(col3)
print(col4)

# step2 = cell_height*1.5
# for i in range(num_of_rows - 1):
#
#     canv.create_text(cell_width*2.5, step2, text=col3[i], font="Verdana 20", fill="black")
#     step2 += cell_height
#
# step2 = cell_height*1.5
# for i in range(num_of_rows - 1):
#
#     canv.create_text(cell_width*3.5, step2, text=col4[i], font="Verdana 20", fill="black")
#     step2 += cell_height


root.mainloop()
