n = 4  # must be positive integer or 0
f = 1  # initializing variable where we gonna save factorial number

if n < 0 or not isinstance(n, int):
    print('incorrect input. exiting the program')
else:
    for i in range(n):
        f *= i + 1

print(f)


x = list(range(1, n + 1))
print(x)
