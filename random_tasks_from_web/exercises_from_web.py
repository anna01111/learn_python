import random
import string
import requests
from bs4 import BeautifulSoup
import itertools
from more_itertools import locate
import json
from collections import Counter
import calendar
from bokeh.plotting import figure, show, output_file


"""
num = int(input("Enter a number: "))

print([el for el in range(1, num + 1) if num % el == 0])
"""


"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [random.randint(1, 101) for el in range(10)]
d = [random.randint(1, 101) for el in range(10)]
print(c)
print(d)
print(set(c) & set(d))
"""


"""
word = input("Enter a word: ")

if word == word[::-1]:
    print("wow it's a palindrome")
else:
    print("well, forget it")
"""


"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [el for el in a if el % 2 == 0]

print(b)
"""


"""
while True:
    print("\nHello, this is a Rock Paper Well game.\n1 - Rock\n2 - Paper\n3 - Well\nPlease enter numbers from 1 to 3.")
    user1 = int(input("user1: "))
    print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
    user2 = int(input("user2: "))

    if user1 == user2:
        print("It's a draw.")
    elif user1 == 1 and user2 == 3 or user1 == 3 and user2 == 1:
        print("user1 is a winner.")
    elif user1 == 1 and user2 == 2 or user1 == 2 and user2 == 1:
        print("user2 is a winner.")
    elif user1 == 3 and user2 == 2 or user1 == 2 and user2 == 3:
        print("user1 is a winner.")
    command = input("Enter exit_ to leave or anything else to continue: ")
    if command == "exit_":
        break
"""


"""
guesses = 0
random_num = random.randint(1, 9)
while True:
    if guesses == 0:
        print("\nEnter a number from 1 to 9 inclusive: ")
    else:
        print("Try again: ")
    user_input = int(input())
    guesses += 1
    if user_input > random_num:
        print("You guessed too high.")
    elif user_input < random_num:
        print("You guessed too low.")
    elif user_input == random_num:
        print("You've guessed it! It took you {} tries.".format(guesses))
        break
    continue
"""


"""
def beg_end(some_list):
    res = [some_list[0], some_list[-1]]
    return res


a = [4, 5, 10, 15, 20, 25]
print(beg_end(a))
"""


"""
def fib(n):
    some_list = []
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
        some_list.append(a)
    return some_list


print(fib(20))
"""


"""
a = [random.randint(1, 10) for i in range(0, 20)]


def rem_dupl_using_sets(my_list):
    return list(set(my_list))


def rem_dupl_using_lists(my_list):
    my_list1 = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list1:
            my_list1.append(my_list[i])
    return my_list1


print(a)
print(rem_dupl_using_sets(a))

print(a)
print(rem_dupl_using_lists(a))

"""


"""
a = random.sample(range(40), 10)
b = random.sample(range(40), 20)


def list_and_list_using_sets(list1, list2):
    res = list(set(list1) & set(list2))
    return res


def list_and_list(list1, list2):
    list3 = []
    for i in range(len(list1)):
        if list1[i] in list2 and list1[i] not in list3:
            list3.append(list1[i])
    for i in range(len(list2)):
        if list2[i] in list1 and list2[i] not in list3:
            list3.append(list2[i])
    return list3


print(a)
print(b)
print(list_and_list_using_sets(a, b))
print(list_and_list(a, b))

"""


"""

def reverse_string():
    inp = input("Enter a sentence: ")
    list1 = inp.split()[::-1]
    res = " ".join(list1)
    return res


print(reverse_string())

"""


# password generator

"""

def make_password():
    password = ""
    strength = int(input("For strong password, enter 1\nFor weak password, enter 2\n"))
    if strength == 1:
        password = "".join(random.choices(string.ascii_letters*2 + string.digits*3 + string.punctuation, k=8))
    elif strength == 2:
        password = "".join(random.choices(string.ascii_letters, k=8))
    return password


print(make_password())

"""


"""
url = 'https://www.nytimes.com/'

r = requests.get(url)
r_html = r.text

print(r_html)

soup = BeautifulSoup(r_html, features="html.parser")
title = soup.find('span', 'articletitle')
print(title)
"""

# cows and bulls game
"""

def c_and_b_game():
    rand_list = [str(random.randrange(10)) for i in range(4)]
    print(rand_list)
    while True:
        cows = 0
        bulls = 0
        inp_list = list(input("Enter a four-digit number: "))
        print(inp_list)
        rand_list_copy = rand_list.copy()
        inp_list_copy = inp_list.copy()
        subject_of_removal_cows = []
        subject_of_removal_bulls = []
        for i in range(len(rand_list)):
            if inp_list_copy[i] == rand_list[i]:
                cows += 1
                subject_of_removal_cows.append(inp_list_copy[i])
        for i in range(len(subject_of_removal_cows)):
            inp_list_copy.remove(subject_of_removal_cows[i])
            rand_list_copy.remove(subject_of_removal_cows[i])
        for i in range(len(inp_list_copy)):
            if inp_list_copy[i] in rand_list_copy:
                bulls += 1
                subject_of_removal_bulls.append(inp_list_copy[i])
        for i in range(len(subject_of_removal_bulls)):
            inp_list_copy.remove(subject_of_removal_bulls[i])
            rand_list_copy.remove(subject_of_removal_bulls[i])
        print("{} cows, {} bulls".format(cows, bulls))
        if inp_list == rand_list:
            print("You've got it..")
            break


c_and_b_game()
"""


"""
with open('primes.txt', 'r') as f:
    primes = set(f.read().split(", "))


with open('happies.txt', 'r') as f:
    happies = set(f.read().split(", "))


overlaps = list(primes & happies)
overlaps = [int(el) for el in overlaps]
overlaps.sort()
print(overlaps)

"""


"""
my_list = []
for combination in itertools.product(range(10), repeat=4):
    my_list.append("%s" % " ".join(map(str, combination)))

print(my_list)

guesses = 0
while True:
    middle_index = int(len(my_list) // 2)
    print(my_list[middle_index])
    print("If i've guessed, enter g\n"
          "If your number is lower than mine, enter l\n"
          "If your number is higher than mine, enter h")
    user_input = input(": ")
    if user_input == "g":
        print("wow, i have guessed after {} tries ^ ^".format(guesses))

        break
    if user_input == "l":
        my_list = my_list[:middle_index]
    elif user_input == "h":
        my_list = my_list[middle_index + 1:]
    guesses += 1
    print(my_list)

"""


"""
def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(max_number(7, 2, 3))
"""


"""
with open('sowpods.txt', 'r') as f:
    line = f.read().split("\n")

random_word = line[random.choice(range(len(line)))]

letters_to_show = ["_" for el in range(len(random_word))]
already_used_letters = []
letter = ""
while True:
    if letter not in already_used_letters:
        already_used_letters.append(letter)
    if "_" not in letters_to_show:
        print("Congrats.")
        break
    letter = input("Guess your letter: ").upper()
    indexes_of_letter = list(locate(random_word, lambda x: x == letter))
    for el in indexes_of_letter:
        letters_to_show[el] = letter
    string_to_show = " ".join(letters_to_show)
    if letter in already_used_letters:
        print("You've already used that letter. Try another one.")
        continue
    elif letter in random_word:
        print(string_to_show)
    elif letter not in random_word:
        print("Incorrect.")
        print(string_to_show)
        continue
"""

"""
def lookup_name():
    print("Who's birthday do you want to look up?")
    user_key = input(": ").lower().capitalize()
    user_value = Birthdays.get(user_key, "no data")
    if user_key in Birthdays:
        print(user_key + "'s birthday is " + user_value + ".")
    else:
        print("Sadly, we don't have a data for this name.")


def add_name():
    print("Would you like to add another name to this list?"
          "\nIf yes, enter yes"
          "\nIf no, enter anything else")
    command_ = input(": ").lower()
    if command_ == "yes":
        new_name = input("Enter a name (please write it in lowercase with only first letter capitalized): ")
        new_date = input("Enter a date: ")
        Birthdays[new_name] = new_date
        with open("info.json", "w") as f:
            json.dump(Birthdays, f)
        print("Your data has been added, bye.")
    else:
        print("All right, bye.")


with open("info.json", "r") as f:
    Birthdays = json.load(f)

print("\nWelcome to the birthday dictionary. We know the birthdays of:")
for key in Birthdays:
    print(key)

lookup_name()
add_name()
"""


"""
def extract_months(file):
    with open("info.json", "r") as f:
        birthdays = json.load(f)

    dates = [birthdays[key] for key in birthdays]
    months = [int(el[3:5]) for el in dates]

    months_by_name = []
    for el in months:
        months_by_name.append(calendar.month_name[el])

    c = Counter(months_by_name)
    #for key in c:
        #print(key + ": " + str(c[key]))
    return c


c = extract_months("info.json")

output_file("plot.html")
x_categories = [key for key in c]
x = [key for key in c]
y = [c[key] for key in c]

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)
"""











































































































































