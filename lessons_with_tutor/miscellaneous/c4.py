# Дано натуральне тризначне число.
# Знайти:


# число одиниць, десятків і сотень цього числа;
n_raw = 619
n = list(str(n_raw))

num_of_ones = int(n[-1])
num_of_tenths = int(n[-2])
num_of_hundreds = int(n[-3])

print('ones - {}'.format(num_of_ones))
print('tenths - {}'.format(num_of_tenths))
print('hundreds - {}'.format(num_of_hundreds))


# суму цифер цього числа
n_sum = 0
for i in range(len(n)):
    n[i] = int(n[i])
    n_sum += n[i]

print('sum - {}'.format(n_sum))


# check if all elements in a list are equal
is_equal = True
for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        is_equal = False
        break
print('is equal - {}'.format(is_equal))

# check if all elements in a list are different
is_different = True
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        is_different = False
        break
print('is_different - {}'.format(is_different))


# pop can be used to delete element from a list and simultaneously assign that element to a variable
'''
print(l)
n1 = l.pop(0)
print(n1)
'''


