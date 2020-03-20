
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""

my_words = input("Please enter words, separated by space(e.g. elf line wolf): ").lower().split(" ")
base_word = my_words[0]
base_combos = []
for i in range(len(base_word)):
    for j in range(len(base_word) - i):
        base_combos.append(base_word[j:j + i + 1])
base_combos = base_combos[::-1]
print(base_combos)

# I want to check for every combination(from biggest to smallest)
# if it is in every other string - then return it,
# if there is no such combo that would be in every other string - return an empty string
# I DON'T KNOW HOW TO CONTINUE

"""
for el in base_combos:
    for word in my_words[1:]:
        if el not in word:
            break
        else:
            continue
"""


















