# Реалізовуємо форматування тексту, у якому ми
#
# - розтягуємо текст
# - прижимаєм текст до правого краю
# - центруємо текст


my_s = '''The territory of modern Ukraine has been inhabited since 32,000 BC. During the Middle Ages, the area was a key centre of East Slavic culture, with the powerful state of Kievan Rus' forming the basis of Ukrainian identity. Following its fragmentation in the 13th century, the territory was contested, ruled and divided by a variety of powers, including the Polish–Lithuanian Commonwealth, Austria-Hungary, the Ottoman Empire and Russia. A Cossack republic emerged and prospered during the 17th and 18th centuries, but its territory was eventually split between Poland and the Russian Empire. After World War II the Western part of Ukraine merged into the Ukrainian Soviet Socialist Republic, and the whole country became a part of the Soviet Union as a single state entity. Ukraine gained its independence in 1991, following the dissolution of the Soviet Union at the end of the Cold War. '''
my_length = 102


def format_string(s, length):

    # розриваємо по заданій довжині, не розриваючи слова
    lst = []
    st = 0
    en = length
    while True:
        # print('st - ', st, ', en - ', en)
        if s[en] != ' ':
            while s[en] != ' ':
                en -= 1
        lst.append(s[st:en])
        st = en + 1
        en += length
        if en > len(s):
            break
    lst.append(s[st:len(s) - 1])

    for el in lst:
        print(el)
    return lst


def stretchen(lst, length):

    lst2 = []
    for el in lst:
        space = length - len(el)
        place = el.count(' ')
        d = ' '
        if place == 0:
            el = el + d * space
        else:
            while space > 0:
                if place < space:
                    el = el.replace(d, d + ' ', place)
                    space -= place

                else:
                    el = el.replace(d, d + ' ', space)
                    space = 0
                d = d + ' '

        lst2.append(el)
    return lst2


# my_lst2 = stretchen(format_string(my_s, my_length), my_length)
#
# print('\nStretchened\n')
# for el in my_lst2:
#     print(el)


def put_right(lst, length):

    lst2 = []
    for el in lst:
        space = length - len(el)
        d = ' '
        el = d * space + el

        lst2.append(el)
    return lst2


# my_lst2 = put_right(format_string(my_s, my_length), my_length)
#
# print('\nPut right\n')
# for el in my_lst2:
#     print(el)


def put_center(lst, length):

    lst2 = []
    for el in lst:
        space = length - len(el)
        d = ' '
        space1 = space // 2
        space2 = space - space // 2
        el = d * space1 + el + d * space2

        lst2.append(el)
    return lst2


# my_lst2 = put_center(format_string(my_s, my_length), my_length)
#
# print('\nPut center\n')
# for el in my_lst2:
#     print(el)

