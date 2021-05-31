import copy
# Дано натуральне тризначне число, у якому всі цифри різні.
# Знайти всі числа, утворені при перестановці цифр заданого числа.


n = ['1', '2', '3']
l = []

for i in range(3):
    l.append(n)
    n = copy.deepcopy(n)

    # swaps the last two elements
    temp_var = n[2]
    n[2] = n[1]
    n[1] = temp_var

    l.append(n)
    n = copy.deepcopy(n)

    # swaps the last two elements
    temp_var = n[2]
    n[2] = n[1]
    n[1] = temp_var

    # moves the last elements in the beginning
    temp_var = n.pop(2)
    n.insert(0, temp_var)
    
print(l)






