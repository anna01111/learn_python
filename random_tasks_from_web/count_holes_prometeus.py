def count_holes(n):

    n = str(n)
    if '.' in n:
        return 'ERROR'

    try:
        n = int(n)
    except ValueError:
        return 'ERROR'

    holes = {
        '0': 1,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 1,
        '5': 0,
        '6': 1,
        '7': 0,
        '8': 2,
        '9': 1,
        '-': 0,
    }

    n = str(n)

    counter = 0
    for digit in n:
        counter += holes[digit]

    return counter


count_holes('123')

