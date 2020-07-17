import random

# sets size of a matrix
n = 7  # verticals - number of inner lists
m = 7  # horizontals - number of elements in each inner list


# initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


# prints a 2-dimensional list
for el in l:
    print(el)
print()


# fills matrix with random numbers
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = random.randint(0, 100)
        print(l[i][j], end='\t')
    print()

print()


# fills matrix with numbers: 1, 2, 3, 4 and so on
step = 1
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j] = step
        step += 1
        print(l[i][j], end='\t')
    print()


# in theory makes a sound
print('\a')


# makes a snake in a matrix
step = 1
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            l[i][j] = step
        else:
            l[i][m - j - 1] = step
        step += 1


# prints a matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')  # \t makes a tabulation, well, aligns elements so they look fine
    print()
print()


# re-initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


# makes a frame inside a matrix, filling this frame with 1
l[0] = [1 for el in range(m)]
l[n - 1] = [1 for el in range(m)]
for i in range(n):
    l[i][0] = 1
    l[i][m - 1] = 1


# prints a matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()


# re-initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])


# makes a diagonal with 2
for i in range(n):
    l[i][i] = 2


# makes a supplementary diagonal with 3
for i in range(n):
    l[i][m - i - 1] = 3


# prints a matrix
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()


