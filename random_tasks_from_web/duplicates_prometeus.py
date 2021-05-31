
def clean_list(list_to_clean):

    res = []
    for i in range(len(list_to_clean)):
        if list_to_clean[i] not in res:
            res.append(list_to_clean[i])
        else:
            x = list_to_clean[i]
            index_y = res.index(list_to_clean[i])
            y = res[index_y]

            if type(x) != type(y):
                res.append(list_to_clean[i])

    return res


print(clean_list([32, 32.1, 32.0, -123]))
