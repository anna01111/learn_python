# згенерувати магічний квадрат

import random

# sets size of a matrix
n = 7  # verticals - number of inner lists
m = 7  # horizontals - number of elements in each inner list


# re-initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()

print()


# puts random numbers in matrix to make magic
sum_0 = 0
for j in range(n):
        l[0][j] = random.randint(1, 100)
        sum_0 += l[0][j]


for i in range(1, n - 1):
    sum_1 = 0
    for j in range(n - 1):
            l[i][j] = random.randint(1, 100)
            sum_1 += l[i][j]

    l[i][n - 1] = sum_0 - sum_1


for j in range(n):
        sum_1 = 0
        for i in range(n - 1):
            sum_1 += l[i][j]
        l[n - 1][j] = sum_0 - sum_1


# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()

print()

print(sum_0)


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

