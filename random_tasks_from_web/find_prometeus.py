"""Практичне завдання 5.4"""


def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


my_folder = ['D:', ['recycle bin', 'anna.txt'], 'hey.py']
my_filename = 'anna.txt'


# def file_search(folder, filename):
#     path = ''
#     print('folder: ', folder)
#
#     for item in folder:
#             print('item: ', item)
#             if isinstance(item, list):
#                 if file_search(item, filename):
#                     return True
#             else:
#                 print('ITEM: ', item)
#                 print('FILENAME: ', filename)
#                 if item == filename:
#                     return True
#     else:
#         return False

path = []


def file_search(folder, filename):
    global path

    for i in range(len(folder)):
            if isinstance(folder[i], list):
                if file_search(folder[i], filename):
                    path.append(folder[0])
                    path2 = path[::-1]
                    res = '/'.join(path2)
                    return res
            else:
                if folder[i] == filename:
                    path.append(filename)
                    path.append(folder[0])
                    return True
    else:
        return False


print(file_search(my_folder, my_filename))
#print(file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder',
   #  'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))

