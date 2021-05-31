"""
Вхідні дані: 2 невід'ємних дійсних числа a та b -- аргументи командного рядка. b не дорівнює 0.

Вихідні дані: дійсне число -- результат обчислення формули

https://courses.prometheus.org.ua/courses/KPI/Programming101/2015_T1/courseware/e44225a068e34fc2bef68a58bf1a122b/a5463773a30745a3a29ba4d78b6d4538/

Приклад
Вхідні дані: 0 1
Приклад виклику: python test.py 0 1
Результат: 0.0
Вхідні дані: 0.5 10
Приклад виклику: python test.py 0.5 10
Результат: 0.688209837593

"""

import sys
import math
a = float(sys.argv[1])
b = float(sys.argv[2])

x_one = math.sqrt(a*b)
x_two = math.e ** a * b
x_three = a * math.e ** (2 * a / b)


x = x_one/x_two + x_three

print(x)

