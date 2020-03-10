# status - Done

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

my_list = list(map(int, input("Please enter numbers in the following format: 1 29 7 3 ").split()))
my_num = int(input("Please enter a whole number: "))


def two_sum(user_list, user_num):
    for i in user_list:
        if user_num - i in user_list:
            res = [user_list.index(i), user_list.index(user_num - i)]
            print("Here are indexes of two numbers: ")
            return res
    print("No luck. Try different numbers")


print(two_sum(my_list, my_num))










