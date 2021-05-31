# використати алгоритм Евкліда для пошуку найбільшого спільного дільника
import itertools
import operator


numbers = [1, 2, 3, 4, 5]

res = itertools.accumulate(numbers, operator.mul)

for item in res:
    print(item)




