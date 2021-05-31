import sys

x = str(sys.argv[1])

counter = 0

for i in range(len(x)):
    if x[i] == '(':
        counter += 1
    elif x[i] == ')':
        counter -= 1
    if counter < 0:
        print('NO')
        break
else:
    if counter == 0:
        print('YES')
    else:
        print('NO')
