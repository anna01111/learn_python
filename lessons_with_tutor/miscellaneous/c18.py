# створення польського запису + дужки

input_s = '(10+(2-3))*4'
output_s = []
stack_s = []

nums = []
counter = 1
print('start')

i = 0  # to use in input_s
j = 0  # to use in nums
while i < len(input_s):
    print('i = ', i)
    if '0' <= input_s[i] <= '9':
        print(input_s[i])
        nums.append(input_s[i])
        if i + counter < len(input_s):
            while '0' <= input_s[i + counter] <= '9':
                nums[j] += input_s[i + counter]
                counter += 1
        nums[j] = int(nums[j])
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
    if type(nums[i]) == int:
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

