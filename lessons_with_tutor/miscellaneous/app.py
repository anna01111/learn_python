class O:
    name = 'O'


class A:
    name = 'A'


class B(A, O):
    pass


b = B()
print(b.__class__.name)
