"""
Составить программу расчета гипотенузы прямоугольного треугольника.
Длина катетов запрашивается у пользователя.
"""
import math


try:
    c1 = int(input('Please enter length of the first cathetus\n'))
    c2 = int(input('Please enter length of the second cathetus\n'))
except ValueError:
    print('Incorrect input. The end')
else:
    hypotenuse = math.sqrt(c1**2 + c2**2)
    print(f'The length of hypotenuse is {hypotenuse}')
