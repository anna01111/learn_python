# Створити консольний додаток, що моделює спрощену гру «Еволюція».
# На ігровому полі випадковим чином розмістити клітини. Розмір поля та кількість клітин задається користувачем.
# Після натискання на клавішу «Пробіл» провести такі операції:
# • якщо чарунка ігрового поля порожня і в сусідніх чарунках є 2 або більше клітин,
#   то в даній чарунці з'являється клітина;
# • якщо в чарунці знаходиться клітина і по сусідству немає жодної вільної чарунки, то клітина вмирає.


import random

# sets size of a matrix
n = 7  # verticals - number of inner lists
m = 7  # horizontals - number of elements in each inner list


# initializes a matrix
l = []
for i in range(n):
    l.append([0 for el in range(m)])



num_of_cells = 10

k = 0
while k < num_of_cells:
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    if l[x][y] == 0:
        l[x][y] = 1
        k += 1

# prints a matrix
print()
for i in range(n):
    for j in range(m):
        print(l[i][j], end='\t')
    print()
print()


for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
