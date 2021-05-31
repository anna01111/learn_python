from tkinter import *

"""
languages = ["Python", "JavaScript", "C#", "Java"]

root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

languages_listbox = Listbox()

for language in languages:
    languages_listbox.insert(END, language)

languages_listbox.pack()

root.mainloop()

"""

"""


languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]

root = Tk()
root.title("GUI на Python")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)

for language in languages:
    languages_listbox.insert(END, language)

languages_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=languages_listbox.yview)

root.mainloop()

"""


# удаление выделенного элемента
def delete():
    selection = languages_listbox.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    languages_listbox.delete(selection[0])


# добавление нового элемента
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)


root = Tk()
root.title("GUI на Python")

# текстовое поле и кнопка для добавления в список
language_entry = Entry(width=40)
language_entry.grid(column=0, row=0, padx=6, pady=6)
add_button = Button(text="Добавить", command=add).grid(column=1, row=0, padx=6, pady=6)

# создаем список
languages_listbox = Listbox()  # selectmode="multiple" to get multiple selection
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)

# добавляем в список начальные элементы
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")

delete_button = Button(text="Удалить", command=delete).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()