s = "Ukraine is a large country in Eastern Europe known for its Orthodox churches, Black Sea coastline and forested mountains. Its capital, Kiev, features the gold-domed St. Sophia's Cathedral, with 11th-century mosaics and frescoes. Overlooking the Dnieper River is the Kiev Pechersk Lavra monastery complex, a Christian pilgrimage site housing Scythian tomb relics and catacombs containing mummified Orthodox monks."

print(len(s))

width = 100
for i in range(0, len(s), width):
    print(s[i:i + width])


s2 = s.split(' ')
print(len(s2))
s2.sort()
print(s2)
print(type(s2))


for i in range(len(s2)):
    if '.' in s2[i] or ',' in s2[i]:
        s2[i] = s2[i][:-1]

for el in s2:
    print(el)

set_2 = set(s2)
print(len(set_2))

for el in set_2:
    num = s2.count(el)
    print(el + ' ' + str(num))
