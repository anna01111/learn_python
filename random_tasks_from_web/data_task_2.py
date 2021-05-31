"""Практичне завдання 7.4"""

import datetime


def create_calendar_page(month=None, year=None):

    header1 = '-' * 19 + '-'
    header2 = 'MO TU WE TH FR SA SU'
    header = header1 + '\n' + header2 + '\n' + header1 + '\n'

    num_of_days = None

    if not month and not year:

        today = datetime.datetime.today()

        month = today.timetuple()[1]
        year = today.timetuple()[0]

        first_day = today.replace(day=1)
        start_day = first_day.weekday()
    elif month and not year:
        today = datetime.datetime.today()


        year = today.timetuple()[0]


        first_day = today.replace(month=month, day=1)
        start_day = first_day.weekday()



    else:
        first_day = datetime.datetime(year, month, 1)
        start_day = first_day.weekday()


    d_31 = [1, 3, 5, 7, 8, 10, 12]
    d_30 = [4, 6, 9, 11]

    if month in d_31:
        num_of_days = 31
    elif month in d_30:
        num_of_days = 30
    elif month == 2:

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


    days = list(range(1, num_of_days + 1))

    for i in range(len(days)):
        if len(str(days[i])) == 1:
            days[i] = '0' + str(days[i])


    spaces = '  '
    for i in range(start_day):
        days.insert(0, spaces)


    temp_days = []
    for i in range(len(days)):
        if i % 7 == 0 and i != 0:
            temp_days.append('\n')
        elif i != 0:
            temp_days.append(' ')
        temp_days.append(str(days[i]))


    temp_days.insert(0, header)
    result = ''.join(temp_days)
    return result


print(create_calendar_page(2, 2016))


