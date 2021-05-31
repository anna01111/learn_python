morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--.."
}


def encode_morze(text):
    text_alpha = ''
    for item in text:
        if item.isalpha() or item == ' ':
            text_alpha += item

    words = text_alpha.split(' ')
    print(words)

    enc_text = ''
    for item in words:
        for letter in item:
            x = morse_code[letter.upper()]
            y = ''
            for el in x:
                if el == '-':
                    y += '^^^'
                elif el == '.':
                    y += '^'
                y += '_'
            enc_text += y
            enc_text += '__'
        enc_text += '____'
    enc_text = enc_text[:-7]

    return enc_text




text = 'S1OS2'



our_res = encode_morze(text)
print(our_res)
answer = '^_^_^___^^^_^^^_^^^___^_^_^'

print(our_res == answer)
