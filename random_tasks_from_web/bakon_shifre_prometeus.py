import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

m = str(sys.argv[1])

m = [el for el in m if el != ' ']
x = len(m) % 5
m = m[:-x]


temp_m = []
for i in range(0, len(m), 5):
    temp_m.append(''.join(m[i:i + 5]))
m = temp_m


temp_m = []
for word in m:
    temp_word = ''
    for letter in word:
        if letter.islower():
            temp_word += 'a'
        elif letter.isupper():
            temp_word += 'b'
    temp_m.append(temp_word)
m = temp_m


result = []
for el in m:
    index = key.find(el)
    letter = alphabet[index]
    result.append(letter)

result = ''.join(result)

print(result)

