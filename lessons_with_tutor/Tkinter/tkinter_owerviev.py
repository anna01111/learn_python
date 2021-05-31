from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))


def click_button_new():
    global clicks
    clicks += 1
    buttonText.set("Clicks {}".format(clicks))


root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300+600+250")

btn = Button(text="Hello")
btn.pack()  # робить кнопку видимою


btn1 = Button(text="Hello1",          # текст кнопки
             background="#ccc",     # фоновый цвет кнопки
             foreground="#f0f",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="50",              # отступ от границ до содержимого по вертикали
             font="10"              # высота шрифта
             )
btn1.pack()


btn2 = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn2.pack()


buttonText = StringVar()
buttonText.set("Clicks {}".format(clicks))

btn3 = Button(textvariable=buttonText, background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button_new)
btn3.pack()


root.mainloop()

