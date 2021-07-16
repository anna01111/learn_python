import random

"""Задано список (г). Написати програму, яка змінить місцями перший стовпчик і стовпчик,
 який містить мінімальний за абсолютною величиною елемент матриці."""

n = 4

# приклад як може виглядати 'special' матриця
# r0 = [[1, 34, 567],
#       [7, -54, 890],
#       [-4, 43, 673]]


def special_matrix(n):
    # згенерити матрицю n х n з додатковою умовою
    r = []
    for i in range(n):
        r.append([])
        for j in range(n):

            if j == 0:
                x = random.randrange(-9, 10)
            else:
                a = int((j + 1) * '9') * -1
                b = int(j * '9') * -1
                c = 10 ** j
                d = 10 ** (j + 1)
                x = random.choice([random.randrange(a, b), random.randrange(c, d)])

            r[i].append(x)

    for item in r:
        print(item)
    print()

    return r


def usual_matrix(n):
    # згенерити матрицю n х n
    r = []
    for i in range(n):
        r.append([])
        for j in range(n):
            x = random.randrange(-100, 100)
            r[i].append(x)

    for item in r:
        print(item)
    print()

    return r


def get_col(r):
    # визначити колонку яка містить мінімальний за абсолютною величиною елемент матриці
    r_temp = []
    for i in range(len(r)):
        for j in range(len(r)):
            r_temp.append(abs(r[i][j]))
    print(r_temp)

    min_el = min(r_temp)
    print(f'minimal elem: {min_el}')

    ind = r_temp.index(min_el)

    col = ind % len(r)
    print(f"col: {col}")

    return col


def change_places(r, col):
    # поміняти стовпчики місцями
    zero_col = []
    x_col = []

    for i in range(len(r)):
        zero_col.append(r[i][0])
        x_col.append(r[i][col])

    i_zero_col = iter(zero_col)
    i_x_col = iter(x_col)

    for i in range(len(r)):
        r[i][0] = next(i_x_col)
        r[i][col] = next(i_zero_col)

    print()
    for item in r:
        print(item)
    print()


matrix = usual_matrix(n)
min_col = get_col(matrix)
change_places(matrix, min_col)







