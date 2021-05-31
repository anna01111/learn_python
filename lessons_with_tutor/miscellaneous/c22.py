words_set_res = ('a')

print(f'words_set_res = {words_set_res}')

str2 = '''def addition(a, b):
    for word in words_set_res:
    for i in range(len(l)):'''

l = str2.split('\n')
for i in range(len(l)):
    print(i, l[i])

variables = {}
for el in words_set_res:
    variables[el] = []
print(variables)

# ПРОГРАМА ШУКАЄ СЛОВО В СТРОЦІ ЛИШЕ ОДИН РАЗ, А ПОТРІБНО ЗРОБИТИ ЩОБ ШУКАЛО БАГАТО РАЗ
for word in words_set_res:
    for i in range(len(l)):
        if word in l[i]:

            m = -1
            for j in range(2):

                m = l[i].index(word, m + 1)
                print('i', i, 'm ', m, 'word ', word)

            # inx_before = l[i].index(word) - 1
            # inx_after = l[i].index(word) + len(word)
            # if word == 'a':
            #     print(i, inx_before, l[i][inx_before], inx_after, l[i][inx_after])
            # if not l[i][inx_before].isalpha():
            #     if not l[i][inx_after].isalpha():
            #         coordinates = [i, l[i].index(word)]
            #         variables[word].append(coordinates)


for key in variables:
    print(key, variables[key])

