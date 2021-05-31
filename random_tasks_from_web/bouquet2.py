"""Практичне завдання 8.3"""

import itertools


def bouquets(narcissus_price, tulip_price, rose_price, summ):
    flowers = [narcissus_price, tulip_price, rose_price]
    min_price = min(flowers)

    # щоб дізнатись найбільшу кількість квітів в букеті слід поділити суму грошей на ціну найдешевшої квітки
    max_n = summ // min_price
    pool = [0 for i in range(max_n)] + [1 for i in range(max_n)] + [2 for i in range(max_n)]
    #print(pool)

    # потім перебрати всі варіанти букетів обмежені такою кількістю квітів
    res = []
    counter = 0
    for i in range(1, max_n + 1, 2):
        res = list(itertools.combinations(pool, i))
        set_res = set(res)

        for el in set_res:
            print(el)

        for item in set_res:
            price = 0
            for el in item:
                price += flowers[el]
            if price <= summ:
                counter += 1


    # # потім позбутись однакових букетів
    # set_res = set(res)
    # #print(set_res)
    # #print(len(set_res))
    #
    # lst_res = list(set_res)
    # s_res = sorted(lst_res, key=len)
    # #print(s_res)
    #
    # # потім перевірити шоб ми не вилізли за суму
    # counter = 0
    # for item in lst_res:
    #     price = 0
    #     for el in item:
    #         price += flowers[el]
    #     if price <= summ:
    #         counter += 1

    print('counter: ', counter)


bouquets(1, 1, 1, 5)