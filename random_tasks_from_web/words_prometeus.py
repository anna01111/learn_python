def find_most_frequent(text):

    signs = ',.:;!?-'
    text = text.lower()

    text_no_signs = ''
    for el in text:
        if el not in signs:
            text_no_signs += el
        else:
            text_no_signs += ' '

    text_list = list(text_no_signs.split(' '))

    final_text = []
    for el in text_list:
        if el != '' or ' ' not in el:
            final_text.append(el)

    res_dict = dict((x, final_text.count(x)) for x in set(final_text))
    occurrences = []
    for value in res_dict.values():
        occurrences.append(value)

    max_num = max(occurrences)
    res_list = []
    for key, value in res_dict.items():
        if value == max_num:
            res_list.append(key)
    return res_list


print(find_most_frequent('Mom! Mom!         Are-you sleeping?!!!'))



