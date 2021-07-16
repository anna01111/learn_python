"""
Л_р_python_КПИ_17.pdf
Сторінка 78

Варіанти
Завдання 1. Одновимірні масиви (вектори)
"""

import random
import math
n = 10

a = [random.random() for i in range(n)]
b = [random.randint(-10, 11) for j in range(n)]
c = [random.randint(0, 51) for k in range(n)]

# print(a)
print(b)
# print(c)


# d = list(range(n, 0, -1))
# print(d)


def f_1(lst):
    negatives = [item for item in lst if item < 0]
    try:
        max_neg = max(negatives)
        max_neg_ind = lst.index(max_neg)
        for i in range(max_neg_ind):
            lst[i] = lst[i] ** 2
    except ValueError:
        print('there are no negative values')

    print(f'function_1: {lst}')


def f_2(lst):
    not_sequence = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            not_sequence = True
            break

    if not_sequence:
        for i in range(len(lst)):
            if lst[i] < 0:
                lst[i] = 1
    else:
        print('there will be no change')

    print(f'function_2: {lst}')


def f_3(lst):
    lst_pos = [item for item in lst if item >= 0]
    lst_neg = [item for item in lst if item < 0]

    res = lst_pos + lst_neg

    print(f"function_3:\n{res}")


example = [1, 6, 5, 0, 2]


def f_4(lst):
    res = []
    n = int(len(lst) / 2)
    for i in range(n):
        res.append(lst[i])
        res.append(lst[n + i])

    print(f"function_4:\n{res}")


def f_5(lst):
    up = False
    # якшо збільшується
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            break
    else:
        up = True
        print('The numbers go up')

    # якшо зменшується
    down = False
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            break
    else:
        down = True
        print('The numbers go down')

    if not up and not down:
        print('No order')


def f_7(lst):
    l_p_el = None
    for i in range(len(lst)):

        x = -(i + 1)
        print(f'x: {x}')
        print(f'lst[x] - {lst[x]}')
        if lst[x] > 0:
            l_p_el = lst[x]
            ind = len(lst) + x
            break
    res = 0
    if l_p_el:
        print(l_p_el, type(l_p_el))
        new_list = lst[:ind + 1]
        print(new_list)
        res = sum(new_list)

    print(res)


def f_7a(lst):
    # написати таку ж функцію але всюди використовувати звичайні індекси а не зворотні
    l_p_el = None
    ind = None
    for i in range(len(lst) - 1, 0, -1):

        print(f'i: {i}')
        print(f'lst[i] - {lst[i]}')
        if lst[i] > 0:
            l_p_el = lst[i]
            ind = i
            break
    res = 0
    if l_p_el:
        for i in range(ind + 1):
            res += lst[i]
    print(res)


def f_8(lst):
    res = sum([item for item in lst if item % 2 != 0])

    print(res)


def f_9(lst):

    abs_lst = [abs(item) for item in lst]
    max_el = max(abs_lst)
    min_el = min(abs_lst)
    print(f'max_el: {max_el}')
    print(f'min_el: {min_el}\n')

    max_ind = abs_lst.index(max_el)
    min_ind = abs_lst.index(min_el)
    print(f'max_ind: {max_ind}')
    print(f'min_ind: {min_ind}\n')

    ind_sorted = sorted([max_ind, min_ind])

    res = 1
    for i in range(ind_sorted[0] + 1, ind_sorted[1]):
        res *= lst[i]

    print(res)


def f_10(lst):
    new_lst = [item for item in lst if item != 0]
    count = lst.count(0)
    new_lst.extend([0 for item in range(count)])

    print(new_lst)


def f_10a(lst):
    new_lst = [item for item in lst if item != 0] + [0 for item in range(lst.count(0))]

    print(new_lst)


def f_11(lst):
    try:
        zero_ind = lst.index(0)
    except ValueError:
        print('There is no zero in the list')
    else:
        lst2 = [abs(item) for item in lst[zero_ind:]]
        res = sum(lst2)
        print(res)


def f_11a(lst):
    try:
        zero_ind = lst.index(0)
    except ValueError:
        print('There is no zero in the list')
    else:
        res = sum([abs(item) for item in lst[zero_ind:]])
        print(res)


def f_12(lst):
    neg_nums_ind = []
    i_lst = iter(lst)
    for i in range(2):
        for item in i_lst:
            print(f'item: {item}')
            if item < 0:
                neg_nums_ind.append(lst.index(item))
                break

    print(f'neg_nums_ind: {neg_nums_ind}')
    if neg_nums_ind:
        n1 = neg_nums_ind[0]
        n2 = neg_nums_ind[1] if len(neg_nums_ind) == 2 else -1
        res = sum(lst[n1 + 1: n2])

        print(res)
    else:
        print('There are no negative numbers in here')


def f_13(lst, x, y, z):
    """
    x must be smaller then y
    if the interval is empty or invalid, the function returns the initial list unchanged
    """
    new_lst = lst
    flag = False

    for item in lst:
        if item in range(x, y + 1):
            flag = True
            break

    if flag:
        new_lst = []

        for item in lst:
            if item in range(x, y + 1):
                new_lst.append(item)
            else:
                new_lst.append(z)

    print(new_lst)
    return new_lst


f_13([1.2, 5.1, 7.3], 0, 5, None)


