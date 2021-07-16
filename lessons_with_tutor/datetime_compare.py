from datetime import date, datetime, timedelta
import random


# згенерити 10 дат
dates = []
today = datetime.today()
current_year = today.timetuple()[0]


for i in range(10):
    rnd_year = random.randrange(1931, current_year)
    rnd_month = random.randrange(1, 13)
    rnd_day = random.randrange(1, 29)
    dates.append(datetime(rnd_year, rnd_month, rnd_day, 0, 0, 0))

for item in dates:
    print(item)


# вибрати з них дві для порівняння
n1 = None
n2 = None
different = False
while not different:
    n1 = random.randrange(0, len(dates))
    n2 = random.randrange(0, len(dates))
    if n1 != n2:
        different = True

date1 = dates[n1]
date2 = dates[n2]

print()
print(date1)
print(date2)


# порівняти і повернути ту що відбулася пізніше
coef = date1 - date2
coef_int = coef.days

print()
print(coef)


if coef_int < 0:
    res = date2
elif coef_int > 0:
    res = date1
else:
    res = None

print('RESULT')
print(res)
