import random

# fills list with random numbers
lst = []
for i in range(10):
    lst.append(random.randint(0, 23))


print(lst)


# implements sorting from smaller to bigger
for k in range(len(lst) - 1):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            temp_var = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = temp_var


print(lst)



