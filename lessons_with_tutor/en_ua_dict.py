en_ua = {
    'date': ['дата', 'день'],
    'time': ['час', 'період'],
    'year': ['рік']
}

ua_en = dict()

for en_word, ua_words in en_ua.items():
    for item in ua_words:
        ua_en[item] = en_word

print(ua_en)
