# Створити консольний додаток, що моделює таку гру. На ігровому полі захований скарб.
# Розмір ігрового поля задається користувачем. Місце розташування кладу визначається випадковим чином.
# На початку гри гравець розташовується в лівому нижньому кутку поля.
# На кожному етапі можна переміщатися на одну позицію по горизонталі або по вертикалі.
# Гравцеві після кожного кроку надається підказка – відстань до скарбу.

import random

# sets size of a matrix
n = 7  # verticals - number of inner lists
m = 7  # horizontals - number of elements in each inner list


# initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


x_tr = random.randint(0, n - 1)
y_tr = random.randint(0, n - 1)
l[x_tr][y_tr] = 1


x_pl = n - 1
y_pl = 0
l[x_pl][y_pl] = 2


# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()

dist_x = abs(x_tr - x_pl)
dist_y = abs(y_tr - y_pl)

dist = (dist_x ** 2 + dist_y ** 2) ** 0.5

print(dist_x)
print(dist_y)
print(dist)

repeat = True


x_old = n - 1
y_old = 0

while dist > 0:
    repeat = True
    while repeat:
        direct = input("Please enter a direction: u for up, d for down, l for left, r for right: ").lower()
        if direct == 'u':
            if x_pl > 0:
                x_old = x_pl
                x_pl -= 1
                repeat = False
        if direct == 'd':
            if x_pl < n - 1:
                x_old = x_pl
                x_pl += 1
                repeat = False
        if direct == 'l':
            if y_pl > 0:
                y_old = y_pl
                y_pl -= 1
                repeat = False
        if direct == 'r':
            if y_pl < n - 1:
                y_old = y_pl
                y_pl += 1
                repeat = False
        if repeat:
            print("INCORRECT DIRECTION. TRY AGAIN")
    print(x_old, y_old)
    l[x_old][y_old] = 0
    l[x_pl][y_pl] = 2

    # prints a matrix
    print()
    for i in range(n):
        for j in range(m):
            print(l[i][j], end='\t')
        print()
    print()

    dist_x = abs(x_tr - x_pl)
    dist_y = abs(y_tr - y_pl)

    dist = (dist_x ** 2 + dist_y ** 2) ** 0.5

    print(dist_x)
    print(dist_y)
    print(dist)



