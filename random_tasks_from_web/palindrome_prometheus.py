import sys

x = str(sys.argv[1])


x = x.lower()

y = [letter for letter in x if letter != ' ']


if y[::-1] == y:
    print('YES')
else:
    print('NO')





