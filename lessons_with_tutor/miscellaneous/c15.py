# Дано текст, що є правильним записам алгебраїчного виразу котрий складається з чисел,
# знаків арифметичних операцій та дужок (для зміни пріоритету арифметичних операцій),
# наприклад (2+2)*2 
# Обчислити значення цього виразу.

s = '12+20-34'


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b

signs = ['+', '-', '*', '/']

operand1 = ''
operand2 = ''
sign = ''
index = 0

for i in range(len(s)):
    if '0' <= s[i] <= '9':
        operand1 += s[i]
    else:
        index = i
        break
print(index)

if s[index] in signs:
    sign += s[index]
    index += 1


for i in range(index, len(s)):
    if '0' <= s[i] <= '9':
        operand2 += s[i]
    else:
        index = i
        break

print(operand1)
print(operand2)
print(sign)


oper1 = int(operand1)
oper2 = int(operand2)

res = 0
if sign == '+':
    res = addition(oper1, oper2)
elif sign == '-':
    res = subtraction(oper1, oper2)

print(res)
print(index)

if index == len(s):
    print(res)
else:
    operand1 = res
    s = s[index:]
    index = 0
    if s[index] in signs:
        sign += s[index]
        index += 1
    for i in range(index, len(s)):
        if '0' <= s[i] <= '9':
            operand2 += s[i]
        else:
            index = i
            break
    oper1 = int(operand1)
    oper2 = int(operand2)

    res = 0
    if sign == '+':
        res = addition(oper1, oper2)
    elif sign == '-':
        res = subtraction(oper1, oper2)
    if index == len(s):
        print(res)
print(res)


