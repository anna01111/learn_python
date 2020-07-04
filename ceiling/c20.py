# the task here is to grab all the identifiers from a big string, and put them into a list

import keyword
keywords = keyword.kwlist
print(keywords)

str2 = '''def polish_write(input_s):
    # створення польського запису + дужки

    # input_s = '(10+(2-3))*4'
    output_s = []
    stack_s = []

    nums = []
    counter = 1
    print('start')

    i = 0  # to use in input_s
    j = 0  # to use in nums
    while i < len(input_s):  # takes numbers out of string and puts them into list separately
        print('i = ', i)
        if '0' <= input_s[i] <= '9' or input_s[i] == '.':
            print(input_s[i])
            nums.append(input_s[i])
            if i + counter < len(input_s):
                while '0' <= input_s[i + counter] <= '9' or input_s[i + counter] == '.':
                    nums[j] += input_s[i + counter]
                    counter += 1
            nums[j] = float(nums[j])
            print('count = ', counter)
            i += counter
            counter = 1
            print('count = ', counter)
        else:
            nums.append(input_s[i])
            print('else', input_s[i])
            i += 1
        j += 1
        print(nums)

    print()


    signs = {
        '(': 0,
        ')': 5,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    print('input ', nums)
    for i in range(len(nums)):
        if type(nums[i]) == float:
            output_s.append(nums[i])
            print('output ', output_s)
            print('stack', stack_s)
            print()
        if nums[i] in signs:
            if nums[i] == '(':
                stack_s.append(nums[i])
                print('output ', output_s)
                print('stack', stack_s)
                print()
            elif nums[i] == ')':
                x = stack_s.pop()
                print('x ', x)
                while x != '(':
                    if len(stack_s) == 0:  # check
                        break
                    else:
                        output_s.append(x)
                        x = stack_s.pop()
                        print('x ', x)
            elif len(stack_s) == 0:
                stack_s.append(nums[i])
                print('output ', output_s)
                print('stack', stack_s)
                print()
            else:
                priority_input = signs[nums[i]]
                print(priority_input, nums[i])
                priority_stack = signs[stack_s[-1]]
                print(priority_stack, stack_s[-1])
                while priority_input <= priority_stack:
                    if len(stack_s) == 0:
                        break
                    else:
                        output_s.append(stack_s.pop())
                        print('output ', output_s)
                        print('stack', stack_s)
                        print()
                stack_s.append(nums[i])
    while len(stack_s) != 0:
        output_s.append(stack_s.pop())
    print('output ', output_s)
    print('stack', stack_s)
    print()

    return output_s


def calculate_res(input_s):
    # Стековый калькулятор

    # input_s = '123*+4-'
    # input_s = [10, 2, 3, '-', '+', 4, '*']
    res = 0
    stack_s = []

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplying(a, b):
        return a * b

    def division(a, b):
        return a / b

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
        if type(input_s[i]) == float:
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

    return res


ariphmetic_task = '(5+(2-3))*4'

print(calculate_res(polish_write(ariphmetic_task)))

'''

#print(stroka)


counter = 1
i = 0
j = 0
words = []

while i < len(str2):
    if 'a' <= str2[i] <= 'z' or str2[i] == '_':
        #print(str2[i])
        words.append(str2[i])
        while 'a' <= str2[i + counter] <= 'z' or str2[i + counter] == '_' or '0' <= str2[i + counter] <= '9':
            words[j] += str2[i + counter]
            counter += 1
        i += counter
        counter = 1
        j += 1
    else:
        i += 1
print(words)


keyword_set = set(keywords)
words_set = set(words)


our_keywords = words_set & keyword_set
words_set_res = words_set - our_keywords
print(words_set)


def print_list(lst):
    k = 0
    for el in lst:
        if k == 10:
            print()
            k = 0
        else:
            k += 1
            print(el, end=' ')
    print()
    print()


print('WORDS')
print_list(words_set)
print('OUR KEY WORDS')
print_list(our_keywords)
print('RESULT')
print_list(words_set_res)


variables = {}
for el in words_set_res:
    variables[el] = []
print(variables)


l = str2.split('\n')
for i in range(len(l)):
    print(i, l[i])

for word in words_set_res:
    for i in range(len(l)):
        if word in l[i]:
            inx_before = l[i].index(word) - 1
            inx_after = l[i].index(word) + len(word)
            if word == 'a':
                print(i, inx_before, l[i][inx_before], inx_after, l[i][inx_after])
            if not l[i][inx_before].isalpha():
                if inx_after < len(l[i]):
                    if not l[i][inx_after].isalpha():
                        coordinates = [i, l[i].index(word)]
                        variables[word].append(coordinates)




print(variables)

for key in variables:
    print(key, variables[key])



