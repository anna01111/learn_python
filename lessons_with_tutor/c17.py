# Стековый калькулятор

# input_s = '123*+4-'
input_s = [10, 2, 3, '-', '+', 4, '*']
res = 0
stack_s = []


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplying(a, b):
    return a*b


def division(a, b):
    return a/b


signs = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}

for i in range(len(input_s)):

    print('input ', input_s)
    print(stack_s)
    print()
    if type(input_s[i]) == int:
        stack_s.append(input_s[i])
    if input_s[i] in signs:
        op2 = stack_s.pop()
        op1 = stack_s.pop()
        if input_s[i] == '+':
            res = addition(op1, op2)
        elif input_s[i] == '-':
            res = subtraction(op1, op2)
        elif input_s[i] == '*':
            res = multiplying(op1, op2)
        elif input_s[i] == '/':
            res = division(op1, op2)
        stack_s.append(res)

print('input ', input_s)
print('res ', res)
print(stack_s)
print()

