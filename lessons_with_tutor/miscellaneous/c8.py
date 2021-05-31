# Заполнить двумерный массив (n×n)
# Определить, является ли матрица магическим квадратом (сумма чисел в каждой строке и столбце одинаковая).

import random

# sets size of a matrix
n = 3  # verticals - number of inner lists
m = 3  # horizontals - number of elements in each inner list


# re-initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


# puts random numbers in matrix
for i in range(n):
    for j in range(m):
        l[i][j] = random.randint(1, 1)


# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()

print()


# puts sums of each row to a list
sum_list = []
sum = 0
for i in range(n):
    for j in range(m):
        sum += l[i][j]
    print(sum)
    sum_list.append(sum)
    sum = 0

print()


# puts sums of each column to a list
for j in range(n):
    for i in range(m):
        sum += l[i][j]
    print(sum)
    sum_list.append(sum)
    sum = 0


print()
print(sum_list)


# check if all elements in a list are equal
is_equal = True
for i in range(len(sum_list) - 1):
    if sum_list[i] != sum_list[i + 1]:
        is_equal = False
        break
print('is equal - {}'.format(is_equal))

