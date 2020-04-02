from textwrap import wrap

# Задано тризначне натуральне число. Записати його словами, вважаючи, що це число означає деяку суму грошей
# (у гривнях або іншій валюті). Наприклад, для числа 256 треба записати "двісті п’ятдесят шість гривень".

num_dict = {
    0: 'нуль ',
    1: 'одна ',
    2: 'дві ',
    3: 'три ',
    4: 'чотири ',
    5: 'п\'ять ',
    6: 'шість ',
    7: 'сім ',
    8: 'вісім ',
    9: 'дев\'ять ',
    10: 'десять ',
    11: 'одинадцять ',
    12: 'дванадцять ',
    13: 'тринадцять ',
    14: 'чотирнадцять ',
    15: 'п\'ятнадцять ',
    16: 'шістнадцять ',
    17: 'сімнадцять ',
    18: 'вісімнадцять ',
    19: 'дев\'ятнадцять ',
    20: 'двадцять ',
    30: 'тридцять ',
    40: 'сорок ',
    50: 'п\'ятдесят ',
    60: 'шістдесят ',
    70: 'сімдесят ',
    80: 'вісімдесят ',
    90: 'дев\'яносто ',
    100: 'сто ',
    200: 'двісті ',
    300: 'триста ',
    400: 'чотириста ',
    500: 'п\'ятсот ',
    600: 'шістсот ',
    700: 'сімсот ',
    800: 'вісімсот ',
    900: 'дев\'ятсот ',
}


def currency(number):
    currency_name = ''
    if number == 1:
        currency_name = 'гривня '
    if 2 <= number <= 4:
        currency_name = 'гривні '
    if number == 0 or 5 <= number <= 9 or 10 <= number <= 19:
        currency_name = 'гривень '
    return currency_name


def thousand(number):
    if number == 1:
        thousand_name = 'тисяча '
    if number == 0 or 2 <= number <= 4:
        thousand_name = 'тисячі '
    else:
        thousand_name = 'тисяч '
    return thousand_name


user_num = input("Please enter a natural number: ")


def make_words(num):
    output = ''
    if len(num) == 1:
        num = int(num)
        output = num_dict[num]  #+ currency(num)

    elif len(num) == 2:
        num1 = int(num[-2] + '0')
        num2 = int(num[-1])
        if num1 == 10:
            output = num_dict[int(num)]  #+ currency(int(num))
        elif num2 == 0:
            output = num_dict[num1]  #+ currency(num2)
        else:
            output = num_dict[num1] + num_dict[num2]  #+ currency(num2)

    elif len(num) == 3:
        num1 = int(num[-3] + '00')
        num2 = int(num[-2] + '0')
        num3 = int(num[-1])
        if num2 == 10:
            output = num_dict[num1] + num_dict[int(num2 + num3)]  #+ currency(int(num2 + num3)))
        elif num2 == 0 and num3 == 0:
            output = num_dict[num1]  #+ currency(num3))
        elif num2 == 0:
            output = num_dict[num1] + num_dict[num3]
        elif num3 == 0:
            output = num_dict[num1] + num_dict[num2]  #+ currency(num3))
        else:
            output = num_dict[num1] + num_dict[num2] + num_dict[num3]  #+ currency(num3))
    return output


user_num = user_num[::-1]
num_groups = wrap(user_num, 3)
for i in range(len(num_groups)):
    num_groups[i] = num_groups[i][::-1]
num_groups = num_groups[::-1]
print(num_groups)


if len(num_groups) == 1:
    print(make_words(num_groups[0]) + currency(int(num_groups[0][-1])))
elif len(num_groups) == 2:
    print(make_words(num_groups[0]) + thousand(int(num_groups[0][-1])) + make_words(num_groups[1])
          + currency(int(num_groups[1][-1])))
















'''

elif len(num) == 4:
    num0 = int(num[-4])
    num1 = int(num[-3] + '00')
    num2 = int(num[-2] + '0')
    num3 = int(num[-1])
    print(num_dict[num0] + thousand_name(num0) + num_dict[num1] + num_dict[num2] + num_dict[num3] + currency(num3))
    
    '''






