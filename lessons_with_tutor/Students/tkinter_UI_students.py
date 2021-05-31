from app import *
from tkinter import *
import pickle

lst = []

FILENAME = 'data_file'

# student1 = Student('anna', 'loz', date(1990, 10, 1), EducationLevel.PhD)
# student2 = Student('anna', 'kap', date(1991, 10, 1), EducationLevel.Master)
# # student3 = Student('olia', 'a', date(1980, 10, 1), EducationLevel.Master)
# lst.append(student1)
# lst.append(student2)


# удаление выделенного элемента
def delete():
    selection = languages_listbox.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    languages_listbox.delete(selection[0])
    lst.pop(selection[0])

# добавление нового элемента
def add():
    new_name = name_entry.get()
    new_surname = surname_entry.get()

    new_year = int(year_entry.get())
    new_month = int(month_entry.get())
    new_day = int(day_entry.get())

    new_ed_level = students_listbox.get(students_listbox.curselection())

    student3 = Student(new_name, new_surname, date(new_year, new_month, new_day), new_ed_level)
    languages_listbox.insert(END, student3)
    lst.append(student3)


def save():
    global lst
    with open(FILENAME, 'wb') as file:
        pickle.dump(lst, file)


def load():
    global lst
    try:
        with open(FILENAME, 'rb') as file:
            lst = pickle.load(file)
    except FileNotFoundError:
        pass
    languages_listbox.delete(0, languages_listbox.size())

    for el in lst:
        languages_listbox.insert(END, el)



root = Tk()
root.title("GUI на Python")


# НАПИСАТИ В КОЖНЕ ПОЛЕ ШО ТО МАЄ БУТИ - МІСЯЦЬ РІК ІМЯ і т д

# текстовое поле и кнопка для добавления в список
name_entry = Entry(width=10)
name_entry.grid(column=0, row=0, padx=6, pady=6)

surname_entry = Entry(width=10)
surname_entry.grid(column=1, row=0, padx=6, pady=6)

year_entry = Entry(width=4)
year_entry.grid(column=2, row=0, padx=6, pady=6)

month_entry = Entry(width=2)
month_entry.grid(column=3, row=0, padx=6, pady=6)

day_entry = Entry(width=2)
day_entry.grid(column=4, row=0, padx=6, pady=6)

add_button = Button(text="Добавить", command=add).grid(column=5, row=0, padx=6, pady=6)

# создаем список
languages_listbox = Listbox(width=40)
languages_listbox.grid(row=1, column=0, columnspan=4, sticky=W + E, padx=5, pady=5)

# добавляем в список начальные элементы
# languages_listbox.insert(END, student1)
# languages_listbox.insert(END, student2)

delete_button = Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)

save_button = Button(text="Сохранить", command=save).grid(row=2, column=2, padx=5, pady=5)

load_button = Button(text="Вигрузить", command=load).grid(row=2, column=3, padx=5, pady=5)


students_listbox = Listbox()

for ed_level in EducationLevel:
    students_listbox.insert(END, ed_level)

students_listbox.grid(row=1, column=5, padx=5, pady=5)

root.mainloop()