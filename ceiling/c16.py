# створення польського запису

input_s = '123+21*3333333-4'
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
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1
}

for i in range(len(nums)):
    if type(nums[i]) == int:
        output_s.append(nums[i])
        print('input ', nums)
        print('output ', output_s)
        print(stack_s)
        print()
    if nums[i] in signs:
        if len(stack_s) == 0:
            stack_s.append(nums[i])
            print('input ', nums)
            print('output ', output_s)
            print(stack_s)
            print()
        else:
            prior_input = signs[nums[i]]
            print(prior_input, nums[i])
            prior_stack = signs[stack_s[-1]]
            print(prior_stack, stack_s[-1])
            while prior_input <= prior_stack:
                if len(stack_s) == 0:
                    break
                else:
                    output_s += stack_s.pop()
                    print('input ', nums)
                    print('output ', output_s)
                    print(stack_s)
                    print()
            stack_s.append(nums[i])
while len(stack_s) != 0:
    output_s += stack_s.pop()

print('input ', nums)
print('output ', output_s)
print(stack_s)
print()


