num = input("Please enter a number: ")

numbers_dict = {
    0: 'нуль',
    1: 'одна',
    2: 'два',
    3: 'три',
    4: 'чотири',
    5: 'п\'ять',
    6: 'шість',
    7: 'сім',
    8: 'вісім',
    9: 'дев\'ять',
    10: 'десять',
    20: 'двадцять',
    30: 'тридцять',
    40: 'сорок',
    50: 'п\'ятдесят',
    60: 'шістдесят',
    70: 'сімдесят',
    80: 'вісімдесят',
    90: 'дев\'яносто',
}

print(num)

num1 = int(num[0] + '0')


def currency_name(number):
    currency = ''
    if number == 1:
        currency = 'гривня'
    if 2 <= number <= 4:
        currency = 'гривні'
    if 5 <= number <= 9 or num == 0:
        currency = 'гривень'
    return currency


if len(num) > 1:
    num2 = int(num[1])
    if num2 == 0:
        print(numbers_dict[num1] + ' ' + currency_name(num2))
    else:
        print(numbers_dict[num1] + ' ' + numbers_dict[num2] + ' ' + currency_name(num2))
else:
    num = int(num)
    print(numbers_dict[num] + ' ' + currency_name(num))









