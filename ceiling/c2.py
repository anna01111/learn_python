from textwrap import wrap

# Задано тризначне натуральне число. Записати його словами, вважаючи, що це число означає деяку суму грошей
# (у гривнях або іншій валюті). Наприклад, для числа 256 треба записати "двісті п’ятдесят шість гривень".

num_dict = {
    '0': '',
    '1': 'одна ',
    '2': 'дві ',
    '3': 'три ',
    '4': 'чотири ',
    '5': 'п\'ять ',
    '6': 'шість ',
    '7': 'сім ',
    '8': 'вісім ',
    '9': 'дев\'ять ',
    '10': 'десять ',
    '11': 'одинадцять ',
    '12': 'дванадцять ',
    '13': 'тринадцять ',
    '14': 'чотирнадцять ',
    '15': 'п\'ятнадцять ',
    '16': 'шістнадцять ',
    '17': 'сімнадцять ',
    '18': 'вісімнадцять ',
    '19': 'дев\'ятнадцять ',
    '20': 'двадцять ',
    '30': 'тридцять ',
    '40': 'сорок ',
    '50': 'п\'ятдесят ',
    '60': 'шістдесят ',
    '70': 'сімдесят ',
    '80': 'вісімдесят ',
    '90': 'дев\'яносто ',
    '100': 'сто ',
    '200': 'двісті ',
    '300': 'триста ',
    '400': 'чотириста ',
    '500': 'п\'ятсот ',
    '600': 'шістсот ',
    '700': 'сімсот ',
    '800': 'вісімсот ',
    '900': 'дев\'ятсот ',
}


def currency(num):
    """Transforms word 'гривня' into grammatically correct form

    Parameters
    ----------
    num : str
        3-char-length string, consisting of numbers

    Returns
    -------
    str
        Word 'гривня' in grammatically correct form
    """

    if len(num) >= 2 and num[-2] == '1':  # handles '11' till '19'
            currency_name = 'гривень '
    elif num[-1] == '1':
        currency_name = 'гривня '
    elif '2' <= num[-1] <= '4':
        currency_name = 'гривні '
    else:
        currency_name = 'гривень '
    return currency_name


def thousand(num):
    """Transforms word 'тисяча' into grammatically correct form

    Parameters
    ----------
    num : str
        3-char-length string, consisting of numbers

    Returns
    -------
    str
        Word 'тисяча' in grammatically correct form
    """

    if len(num) >= 2 and num[-2] == '1':  # handles '11' till '19'
            thousand_name = 'тисяч '
    elif num[-1] == '1':
        thousand_name = 'тисяча '
    elif '2' <= num[-1] <= '4':
        thousand_name = 'тисячі '
    else:
        thousand_name = 'тисяч '
    return thousand_name  # returns word 'тисяча' in grammatically correct form


def make_phrase(num):
    """Transforms numbers into their word representation

    Parameters
    ----------
    num : str
        3-char-length string, consisting of numbers

    Returns
    -------
    str
        A word representation of a number
    """

    phrase = ''

    if len(num) == 1:
        if num == '0':
            phrase = 'нуль '  # handles '0'
        else:
            phrase = num_dict[num]

    elif len(num) == 2:
        num0 = num[0] + '0'
        num1 = num[1]
        if num[0] == '1':  # handles '11' till '19'
            phrase = num_dict[num]
        elif num1 == '0':  # handles '20', '30' etc
            phrase = num_dict[num0]
        else:
            phrase = num_dict[num0] + num_dict[num1]

    elif len(num) == 3:
        num0 = num[0] + '00'
        num1 = num[1] + '0'
        num2 = num[2]
        if num == '000':  # handles '000' in e.g. '1000'
            phrase = ' '
        elif num[0] + num[1] == '00':  # handles '001' in e.g. '1001'
            phrase = num_dict[num2]
        elif num[1] == '1':  # handles '11' till '19'
            phrase = num_dict[num0] + num_dict[str(int(num1) + int(num2))]
        elif num[1] == '0':  # handles '101'
            phrase = num_dict[num0] + num_dict[num2]
        elif num2 == '0':  # handles '20', '30' etc
            phrase = num_dict[num0] + num_dict[num1]
        else:
            phrase = num_dict[num0] + num_dict[num1] + num_dict[num2]
    return phrase


user_num = input("Please enter a natural number , smaller than 1'000'000: ")

# following block of code scans a string right-to-left and splits it into 3-char-length substrings
# for example '12345' will become ['12', '345']
user_num = user_num[::-1]
num_groups = wrap(user_num, 3)
for i in range(len(num_groups)):
    num_groups[i] = num_groups[i][::-1]
num_groups = num_groups[::-1]


if len(num_groups) == 1:  # handles numbers < 1'000
    print(make_phrase(num_groups[0]) + currency(num_groups[0]))
elif len(num_groups) == 2:  # handles numbers < 1'000'000
    print(make_phrase(num_groups[0]) + thousand(num_groups[0]) + make_phrase(num_groups[1]) + currency(num_groups[1]))
print('\n')


# THIS IS THE END OF A PROGRAM
# FOLLOWING FUNCTIONS ARE HERE FOR POSSIBLE FUTURE MODIFICATIONS


def million(num):
    if len(num) >= 2 and num[-2] == '1':
            million_name = 'мільйонів '
    elif num[-1] == '1':
        million_name = 'мільйон '
    elif '2' <= num[-1] <= '4':
        million_name = 'мільйони '
    else:
        million_name = 'мільйонів '
    return million_name


def milliard(num):
    if len(num) >= 2 and num[-2] == '1':
            milliard_name = 'мільярдів '
    elif num[-1] == '1':
        milliard_name = 'мільярд '
    elif '2' <= num[-1] <= '4':
        milliard_name = 'мільярди '
    else:
        milliard_name = 'мільярдів '
    return milliard_name


