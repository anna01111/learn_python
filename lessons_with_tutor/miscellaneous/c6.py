# В квадратном массиве выделим четыре четверти, ограниченные главной и побочной диагоналями
# (без учета элементов, расположенных на диагоналях): верхнюю, нижнюю, левую и правую.
# Найти сумму элементов:
# - верхней четверти;
# - нижней четверти;
# - правой четверти;
# - левой четверти.


# sets size of a matrix
n = 9  # verticals - number of inner lists
m = 9  # horizontals - number of elements in each inner list


# initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


# makes a main diagonal
for i in range(n):
    l[i][i] = 1


# makes a supplementary diagonal
for i in range(n):
    l[i][m - i - 1] = 1


# prints matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()


# defines upper quarter
for i in range(n):
    for j in range(m):
        if j > i and (j < m - i - 1):
            l[i][j] = -1


# prints matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()


# defines lower quarter
for i in range(n):
    for j in range(m):
        if j < i and (j > m - i - 1):
            l[i][j] = 5


# prints matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()


# defines left quarter
for i in range(n):
    for j in range(m):
        if i > j and (i < m - j - 1):
            l[i][j] = 7


# prints matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()


# defines right quarter
for i in range(n):
    for j in range(m):
        if i < j and (i > m - j - 1):
            l[i][j] = 2


# prints matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()


# defines right quarter + sum it up
sum = 0
for i in range(n):
    for j in range(m):
        if i < j and (i > m - j - 1):
            l[i][j] = 2
            sum += l[i][j]


# prints matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()
print(sum)