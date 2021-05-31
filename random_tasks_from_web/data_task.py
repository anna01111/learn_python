"""Практичне завдання 7.4"""

import datetime


def create_calendar_page(month=None, year=None):

    header1 = '-' * 19 + '-'
    header2 = 'MO TU WE TH FR SA SU'
    header = header1 + '\n' + header2 + '\n' + header1 + '\n'

    num_of_days = None

    # якщо ф-ція без параметрів і ми використовуєм теперішній місяць
    if not month and not year:

        today = datetime.datetime.today()
        print(today.date())

        month = today.timetuple()[1]
        year = today.timetuple()[0]
        print(month)

        first_day = today.replace(day=1)
        start_day = first_day.weekday()
        print(start_day)
    # якщо переданий один параметр
    elif month and not year:
        today = datetime.datetime.today()
        print(today.date())

        year = today.timetuple()[0]
        print(month)

        first_day = today.replace(month=month, day=1)
        start_day = first_day.weekday()
        print(start_day)

    # якщо передані обидва параметри
    else:
        first_day = datetime.datetime(year, month, 1)
        #first_day = today.replace(month=month, day=1)
        start_day = first_day.weekday()
        print('month: ', month, type(month))



    d_31 = [1, 3, 5, 7, 8, 10, 12]
    d_30 = [4, 6, 9, 11]

    if month in d_31:
        num_of_days = 31
    elif month in d_30:
        num_of_days = 30
    elif month == 2:
        # if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        #     num_of_days = 29
        # else:
        #     num_of_days = 28

        if year % 4 == 0:
            if year % 100 == 0:
                num_of_days = 28
            else:
                num_of_days = 29

        if year % 100 == 0:
            if year % 400 == 0:
                num_of_days = 29
            else:
                num_of_days = 28

    print(num_of_days)

    days = list(range(1, num_of_days + 1))

    for i in range(len(days)):
        if len(str(days[i])) == 1:
            days[i] = '0' + str(days[i])

    for item in days:
        print(item)

    spaces = '  '
    for i in range(start_day):
        days.insert(0, spaces)

    print(days)

    temp_days = []
    for i in range(len(days)):
        if i % 7 == 0 and i != 0:
            temp_days.append('\n')
        elif i != 0:
            temp_days.append(' ')
        temp_days.append(str(days[i]))

    print(temp_days)

    temp_days.insert(0, header)
    result = ''.join(temp_days)
    return result


print(create_calendar_page(2, 2016))


