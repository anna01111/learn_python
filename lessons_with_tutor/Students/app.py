from datetime import date
from enum import Enum
from statistics import mean
from operator import attrgetter


class Person:
    def __init__(self, name, surname, birth_date):
        self.__name = name
        self.__surname = surname
        self.__birth_date = birth_date

    def __repr__(self):
        return f'{self.__name} {self.__surname} {self.__birth_date}'

    name = property()

    @name.setter
    def name(self, value):
        for el in value:
            if el.isdigit():
                self.__name = 'no_name'
                break
        else:
            self.__name = value

    @name.getter
    def name(self):
        return self.__name

    surname = property()

    @surname.setter
    def surname(self, value):
        for el in value:
            if el.isdigit():
                self.__surname = 'no_surname'
                break
        else:
            self.__surname = value

    @surname.getter
    def surname(self):
        return self.__surname

    birth_date = property()

    @birth_date.setter
    def birth_date(self, value):

        current_year = date.today().year
        print('CURRENT  year: ', current_year)
        print('value year: ', value.year)
        if current_year - value.year < 150:
            self.__birth_date = value
        else:
            self.__birth_date = date(1, 1, 1)
            print('Incorrect birth date')

    @birth_date.getter
    def birth_date(self):
        return self.__birth_date


class Exam:
    def __init__(self, name, mark, exam_date):
        self.__name = name
        self.mark = mark
        self.__exam_date = exam_date

    def __repr__(self):
        return f'{self.__name} {self.mark} {self.__exam_date}'


# education_level = ['Bachelor', 'Master', 'PhD']


class EducationLevel(Enum):
    Bachelor = 1
    Master = 2
    PhD = 3


class Student(Person):
    def __init__(self, name, surname, birth_date, education):
        Person.__init__(self, name, surname, birth_date)
        self.__passed_exams = []
        self.__education = education
        self.__average_mark = 0

    def __repr__(self):
        info = Person.__repr__(self) + f' {self.__education}'

        for exam in self.__passed_exams:
            info += '\n' + exam.__repr__()  # print info about each exam in a separate line

        if self.__passed_exams:
            info += '\n' + str(self.__average_mark)

        return info

    def __gt__(self, other):
        return self.__average_mark > other.__average_mark

    def __lt__(self, other):
        return self.__average_mark < other.__average_mark

    def count_average_mark(self):
        self.__average_mark = mean([exam.mark for exam in self.__passed_exams])

    def pass_exam(self, exam):
        self.__passed_exams.append(exam)
        self.count_average_mark()


student1 = Student('anna', 'loz', date(1990, 10, 1), EducationLevel.PhD)

student1.birth_date = date(1800, 10, 1)

exam1 = Exam('programming', 100, date.today())
exam2 = Exam('language', 90, date.today())
student1.pass_exam(exam1)
student1.pass_exam(exam2)
print(student1)


student2 = Student('anna', 'kap', date(1991, 10, 1), EducationLevel.Master)

exam3 = Exam('programming', 70, date.today())
exam4 = Exam('language', 60, date.today())
student2.pass_exam(exam3)
student2.pass_exam(exam4)
print(student2)


student3 = Student('olia', 'a', date(1980, 10, 1), EducationLevel.Master)

exam5 = Exam('programming', 80, date.today())
exam6 = Exam('language', 60, date.today())
student3.pass_exam(exam5)
student3.pass_exam(exam6)
print(student3)


group = [student1, student2, student3]
print(group)
print()


# ПОСОРТУВАТИ І ВИДРУКУВАТИ ЗАДОМ НАПЕРЕД - ВІД БІЛЬШОГО ДО МЕНШОГО
# for el in sorted(group):
#     print(el)
# print()
# for el in reversed(sorted(group)):
#     print(el)


def sort_by_surname(group):
    sorted_group = sorted(group, key=lambda student: student.surname)
    return sorted_group


def sort_by_name(group):
    sorted_group = sorted(group, key=lambda student: student.name)
    return sorted_group


def sort_by_name_then_surname(group):
    sorted_group = sorted(group, key=attrgetter('name', 'surname'))
    return sorted_group


def sort_by_birth_date(group):
    sorted_group = sorted(group, key=attrgetter('birth_date'))
    return sorted_group


print('SORTED BY SURNAME')
srt_gr = sort_by_surname(group)
for student in srt_gr:
    print(student)
print()


print('SORTED BY NAME')
srt_gr = sort_by_name(group)
for student in srt_gr:
    print(student)
print()


print('SORTED BY NAME THEN SURNAME')
srt_gr = sort_by_name_then_surname(group)
for student in srt_gr:
    print(student)
print()


print('SORTED BY BIRTH DATE')
srt_gr = sort_by_birth_date(group)
for student in srt_gr:
    print(student)
print()
