# coding=utf-8
# Status - Done

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:    Input: 123    Output: 321

Example 2:    Input: -123   Output: -321

Example 3:    Input: 120    Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2**31, 2**31, − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
overflows.
"""

my_list = list(input("Please enter a whole number from the range between - 2147483648, 2147483648 : "))


def reverse_digits(user_list):
    if user_list[0] == "-":
        sign = [user_list[0]]
        chars = user_list[1:][::-1]
        reversed_list = sign + chars
    else:
        reversed_list = user_list[::-1]
    reversed_num = "".join(reversed_list)
    return int(reversed_num)


print(reverse_digits(my_list))





