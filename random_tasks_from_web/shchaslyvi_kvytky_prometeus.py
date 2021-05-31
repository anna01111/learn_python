import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])


l = list(range(a1, a2 + 1))

temp_l = []
for el in l:
    temp_el = list(str(el))
    n = 6
    x = '0' * (n - len(temp_el))
    temp_el.insert(0, x)
    temp_l.append(''.join(temp_el))

l = temp_l

counter = 0
for el in l:
    x = int(el[0]) + int(el[1]) + int(el[2])
    y = int(el[3]) + int(el[4]) + int(el[5])
    if x == y:
        counter += 1


print(counter)

