
# f = open('test.txt', 'r')
# print(f.name)
# f.close()


# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

    # size_to_read = 10
    # fc = f.read(size_to_read)
    # while len(fc) > 0:
    #     print(fc)
    #     fc = f.read(size_to_read)


s = 'anna is amazing '
print(s.count('a'))
print()
ind = 0
lst = []
while True:

    ind = s.find('a', ind)
    if ind == -1:
        break
    lst.append(s.find('a', ind))
    ind += 1


print(lst)

letter = input('Please enter a letter: ')
d = s.replace('a', letter)

print(d)


