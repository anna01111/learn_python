"""
x = 'y'
while x == 'y':
    t = int(input('Please enter time: '))
    while t < 0 or t > 23:
        print("Invalid time")
        t = int(input('Please enter time: '))

    if t < 0 or t > 23:
        print("Invalid time")
    if 0 <= t < 6:
        print("Good night")
    elif 6 <= t < 13:
        print("Good morning")
    elif 13 <= t < 19:
        print("Good afternoon")
    elif 19 <= t < 24:
        print("Good eve")
    x = input('Do you want to continue? y/n: ')
    """

"""student_marks = input('Please enter your marks separated by space: ').split(' ')
print(student_marks)
sum_of_marks = 0
for el in student_marks:
    sum_of_marks += int(el)

average = sum_of_marks / len(student_marks)
print(sum_of_marks)
print(average)

if 0 <= average <= 59:
    print('two')
if 60 <= average <= 74:
    print('three')
if 75 <= average <= 89:
    print('four')
if 90 <= average <= 100:
    print('five')
    """

"""
s = 100
p = 1
r = 200
months = 0
while s < r:
    s += s / 100 * p
    months += 1
    print(months, s)
"""




