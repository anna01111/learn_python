for i in range(256):
    print(i, chr(i))

a = 'a'
print(a, ord(a))

'''
s = 'Process 0!'

letters = 0
digits = 0
other = 0
for symbol in s:
    if 'a' <= symbol <= 'z' or 'A' <= symbol <= 'Z':
        letters += 1
    elif '0' <= symbol <= '9':
        digits += 1
    else:
        other += 1
print(letters)
print(digits)
print(other)


for i in range(ord('A'), ord('Z') + 1):
    print(chr(i))
'''

s = "for i in range)(ord('A')(, ord('Z') + 1):"

'''
open_ = 0
close_ = 0
correct = True
for symbol in s:
    if symbol == '(':
        open_ += 1
    elif symbol == ')':
        close_ += 1
    if open_ < close_:
        correct = False
        break


equal = open_ == close_
print(equal)
print(correct)
if equal and correct:
    print('Good phrase')
else:
    print('Bad phrase')
'''

'''
counter = 0
for symbol in s:
    if symbol == '(':
        counter += 1
    elif symbol == ')':
        counter -= 1
    if counter < 0:
        break
if counter == 0:
    print('Good phrase')
else:
    print('Bad phrase')
'''


s3 = ''
s2 = '1+2*b/c-56'
lst = ['+', '-', '/', '*']
for el in s2:
    if el not in lst:
        print(el, end='')
        s3 += el
print()
print(s3)



