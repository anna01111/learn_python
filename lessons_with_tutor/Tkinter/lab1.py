from tkinter import *
from tkinter.messagebox import *


def help_func(event):
    sample_text = """
    Имя = Ваше имя
    Адрес - Ваш адрес
    Программист = Отметьте 'Программист' если ви
    являетесь программистом
    Пол = Вибирете ваш пол
    Возраст = Ваш возраст
    """
    lab6.configure(text=sample_text, justify=LEFT)


def ok_func(event):
    user_text = ""
    user_text += f"Имя: {tex1.get(1.0, END)}"
    user_text += f"Адрес: {tex2.get(1.0, END)}"
    if var1.get():
        profession = "Программист"
    else:
        profession = "Не Программист"
    user_text += f"Профессия: {profession}\n"
    sex = "Мужской" if var2.get() else "Женский"
    user_text += f"Пол: {sex}\n"
    user_text += f"Возраст: {tex3.get(1.0, END)}\n"

    if tex1.get(1.0, END) and tex2.get(1.0, END) and tex3.get(1.0, END):
        but1.configure(state="active")

    try:
        x = int(tex3.get(1.0, END))
        if x > 0:
            lab6.configure(text=user_text, justify=LEFT)
        else:
            showinfo("Ошибка!", "Возраст должен бить целим положительним числом")
    except ValueError:
        showinfo("Ошибка!", "Возраст должен бить целим положительним числом")


root = Tk()
root.configure(bg="beige")

lab1 = Label(text="Имя", bg="beige")
lab2 = Label(text="Адрес", bg="beige")

tex1 = Text(root, width=30, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")
tex2 = Text(root, width=30, height=5, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")

but1 = Button(text="OK", state="disabled")
but2 = Button(text="Help")

var1 = IntVar()
ch1 = Checkbutton(root, text="Программист", variable=var1, onvalue=1, offvalue=0, bg="beige")


fra1 = Frame(root, bg="red", borderwidth=1, relief="solid")
fra1.configure(width=400, height=50)


lab3 = Label(text="Пол", bg="beige")

var2 = IntVar()
rad1 = Radiobutton(fra1, text="Женский", variable=var2, value=0, bg="beige")
rad2 = Radiobutton(fra1, text="Мужской", variable=var2, value=1, bg="beige")

rad1.pack()
rad2.pack()

fra1.configure(width=400, height=50)

lab4 = Label(text="Возраст", bg="beige")
tex3 = Text(root, width=10, height=1, font="Verdana 12", wrap=WORD, borderwidth=1, relief="solid")

lab5 = Label(text="Результат", bg="beige")

lab6 = Label(width=40, height=8, borderwidth=1, relief="solid")

lab1.grid(row=0, column=0, padx=20, pady=20)
lab2.grid(row=1, column=0)
tex1.grid(row=0, column=1)
tex2.grid(row=1, column=1)
but1.grid(row=0, column=2)
but2.grid(row=1, column=2)
ch1.grid(row=2, column=0, padx=20, pady=20)
fra1.grid(row=3, column=0, columnspan=3)
lab4.grid(row=4, column=0)
tex3.grid(row=4, column=1, sticky="w", padx=20, pady=20)
lab5.grid(row=5, column=0)
lab6.grid(row=6, column=0, columnspan=2, pady=20)


but1.bind("<Button-1>", ok_func)  # ліва кнопка
but2.bind("<Button-1>", help_func)  # ліва кнопка


root.mainloop()




