import random

# implement algorithm to sort time


# sorts numbers in a list from smallest to largest + swaps rows in a matrix
def my_sort(my_list):
    for k in range(len(my_list) - 1):
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                temp_var = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp_var
                m.insert(i + 2, m[i])
                m.pop(i)
    return my_list


n = 4
m = []

# randomly create n_raw points of time
for i in range(n):
    m.append([])
    m[i].append(random.randint(0, 23))
    m[i].append(random.randint(0, 59))
    m[i].append(random.randint(0, 59))

for i in range(n):
    print(m[i])

# put hours in a separate list for further sorting
hours = []
for i in range(n):
    hours.append(m[i][0])

print()
print(hours)
print()
print(my_sort(hours))
print()

for i in range(n):
    print(m[i])
