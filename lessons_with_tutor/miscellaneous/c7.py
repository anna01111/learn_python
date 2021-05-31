# Заполнить двумерный массив (n×n) таким образом, что элементы,
# находящиеся на главной диагонали и выше нее – случайные положительные числа,
# а элементы, находящиеся ниже главной диагонали получить как
# зеркальное отражение относительно главной диагонали.

import random

# sets size of a matrix
n = 5  # verticals - number of inner lists
m = 5  # horizontals - number of elements in each inner list


# initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


# makes a diagonal
for i in range(n):
    l[i][i] = 1


# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()


# define upper half
for i in range(n):
    for j in range(m):
        if j > i:
            l[i][j] = random.randint(1, 100)


# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()


# define symmetrical bottom part
for i in range(n):
    for j in range(m):
        if j > i:
             l[j][i] = l[i][j]


# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
