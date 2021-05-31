"""This module converts numbers base 10 into numbers with user-requested base"""

import string

characters_set = list(string.digits) + list(string.ascii_letters)

num_to_convert = int(input("Enter a whole positive number with base 10 to convert: "))
base_num = int(input("Enter a base number: "))

result_num = []
while num_to_convert > 1:
    digit = num_to_convert % base_num
    num_to_convert = num_to_convert // base_num
    result_num.append(characters_set[digit])
result_num.append(characters_set[num_to_convert])
result_num = result_num[::-1]
print(result_num)

print(string.digits)
print(string.ascii_uppercase)