
def saddle_point(matrix):

    min_in_row = []
    for i in range(len(matrix)):
        min_el_in_row = min(matrix[i])
        if matrix[i].count(min_el_in_row) == 1:
            min_in_row.append((i, matrix[i].index(min_el_in_row)))

    max_in_col = []
    for j in range(len(matrix[0])):
        column = []
        for el in matrix:
            column.append(el[j])
        max_el_in_col = max(column)
        if column.count(max_el_in_col) == 1:
            max_in_col.append((column.index(max_el_in_col), j))

    res = set(min_in_row) & set(max_in_col)
    if res:
        res_saddle_point = next(iter(res))
    else:
        res_saddle_point = False

    return res_saddle_point


print(saddle_point([[1, 2, 3], [0, 2, 1]]))




