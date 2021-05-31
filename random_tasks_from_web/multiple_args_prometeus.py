import sys

lst = []
for arg in sys.argv[1:]:
    lst.append(arg)

lst = lst[::-1]


res = ''

for i in range(len(lst) - 1):
    res += lst[i]
    res += ' '

res += lst[-1]

print(res)



