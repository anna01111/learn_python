from tkinter import *
from tkinter.messagebox import *  # подключаем диалоговые окна
from tkinter.colorchooser import askcolor  # диалоговое окно выбор цвета

root = Tk()
root.title("Главное окно программы")


# создаем фрейм для размещения на нем других компонент:
win1 = Frame(root, bg='#555555')

# Помещаем фрейм на форму методом pack.
# Вместо параметра side (прижать к стороне) задаем параметр anchor (якорь):
# компонент будет прижат к северной (north) стороне и растянут по ширине.
win1.pack(anchor="n", expand=YES, fill=Y)

# Обработчик кнопки закрытия программы (запуск нескольких диалоговых окон):


def close_query():
    # при нажатии на кнопку уточняем у пользователя, закрывать ли программу:
    if askyesno('Выход из программы...', 'Закрыть программу? '):
        showwarning('Диалоговое окно', 'Внимание!!!')
        # Уничтожаем главное окно и поэтому закрываем программу:
        root.destroy()
    else:
        showinfo('Диалоговое окно', 'Информация')


# Создаем кнопку закрытия программы:
Button(win1, text='Выход', command=close_query).pack(side=RIGHT, padx=10, pady=5)

# Создаем обработчик кнопки выбора цвета:


def my_set_color(w):
    # Запускаем диалоговое окно выбора цвета:
    res = askcolor()
    # печатаем результат res, который вернул диалог:
    print("Диалоговое окно Цвет возвращает результат:", res)
    if res[1]:  # если цвет был выбран, то
        w.config(bg=res[1])  # меняем цвет у виджета w
        win1.config(bg=res[1])  # и меняем цвет у фрейма главного окна


def exit_(win):
    win.destroy()


big = False


def size(win):
    global big
    big = False if big else True

    if not big:
        win.geometry("600x500")
    else:
        win.geometry("300x250")


def input_(entry):
    new_name = entry.get()
    root.label1(text=new_name)


# Обработчик нажатия на кнопку "Цвет" главного окна.
# В этом обработчике создаем новое окно (виджет Toplevel)
def new_window():
    top_l1 = Toplevel(root)  # создание нового окна
    top_l1.title("Дополнительное окно программы")
    top_l1.transient(root)  # – делаем его зависимым от главного окна

    top_l1.geometry("300x250")

    # top_l1.grab_set( ) # – устанавливаем фокус ввода
    # Создаем две кнопки в этом окне:
    b1 = Button(top_l1, text='Color ', command=(lambda: my_set_color(b1)), fg='blue')
    b2 = Button(top_l1, text='Цвет ', command=(lambda: my_set_color(b2)))
    b3 = Button(top_l1, text='Виход ', command=(lambda: exit_(top_l1)))
    b4 = Button(top_l1, text='Размер ', command=(lambda: size(top_l1)))
    b5 = Button(top_l1, text='Ввод ', command=(lambda: input_(entry)))

    b1.pack()
    b2.pack()
    b3.pack()

    b4.pack()
    b5.pack()

    entry = Entry(top_l1, width=10)
    entry.pack()


# Создаем кнопку "Цвет" главного окна:
Button(win1, text='Цвет', command=new_window).pack(side=RIGHT, padx=10, pady=5)

label1 = Label(root, text="Hello Python", fg="#eee", bg="#333")
label1.pack()

root.mainloop()


