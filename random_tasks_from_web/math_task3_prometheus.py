import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])


base_line = 'Everybody sing a song:'

kuplet = ''

for j in range(y):
    kuplet += ' '
    for i in range(x):
        kuplet += 'la-'
    kuplet = kuplet[:-1]

if z == 1:
    kuplet += '!'
elif z == 0:
    kuplet += '.'

song = 'Everybody sing a song:' + kuplet

print(song)
