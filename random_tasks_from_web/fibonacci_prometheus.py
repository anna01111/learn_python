import sys

n = int(sys.argv[1])

n1 = 0
n2 = 1

n3 = 0
if n == 1:
    n3 = 1
else:
    for i in range(1, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

print(n3)
