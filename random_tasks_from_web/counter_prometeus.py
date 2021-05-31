

def counter(a, b):
    a = str(a)
    b = str(b)

    a_no_duplicates = set(a)
    b_no_duplicates = set(b)

    return len(a_no_duplicates & b_no_duplicates)


print(counter(154354, 182))


