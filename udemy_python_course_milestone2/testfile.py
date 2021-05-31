import itertools

with open('1.txt', 'r') as f:
    header = itertools.islice(f, 2)

    for item in header:
        print(item)
    print(type(header))