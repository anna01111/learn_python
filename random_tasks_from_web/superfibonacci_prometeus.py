
# n > 0
# m <= 35


def super_fibonacci(n, m):
    f_list = []
    for i in range(m):
        f_list.append(1)

    next_el = 0
    for i in range(n - m):
        k = 1
        for j in range(m):
            next_el += f_list[-k]
            k += 1
        f_list.append(next_el)
        next_el = 0

    return f_list[n - 1]



