
def convert_n_to_m(x, n, m):

    char_set = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print(x)

    if not (isinstance(x, int) or isinstance(x, str)):
        return False

    print(x)

    if isinstance(x, str):
        x = x.upper()

    x = str(x)

    # визначити чи є лишні символи - різні знаки і букви чи цифри
    # які не влазяться згідно з зазначеної системи числення
    compare_base = char_set[:n]
    print(compare_base)
    for el in x:
        if el not in compare_base:
            return False

    # передбачити одиничну систему числення n
    if n == 1:
        x = len(x)
        n = 10

    # забрати незначущі нулі
    temp_x = x
    for el in x:
        if el == '0':
            temp_x = temp_x[1:]
        else:
            break
    x = temp_x

    # перевести з будь-якої в десяткову
    x_in_base_10 = 0
    for i in range(len(x)):
        b = char_set.index(x[- (i + 1)])
        x_in_base_10 += n ** i * b
    print('x in decimal: ', end='')
    print(x_in_base_10)

    # передбачити одиничну систему числення m
    if m == 1:
        print('OUR RES: ', end='')
        print('0' * x_in_base_10)
        return '0' * x_in_base_10

    # перевести з десяткової в будь-яку
    x_in_base_m = []
    while x_in_base_10 > 1:
        digit = x_in_base_10 % m
        x_in_base_10 = x_in_base_10 // m
        x_in_base_m.append(char_set[digit])
    x_in_base_m.append(char_set[x_in_base_10])
    x_in_base_m = x_in_base_m[::-1]
    x_in_base_m = ''.join(x_in_base_m)

    temp_x_in_base_m = x_in_base_m
    for el in x_in_base_m:
        if el == '0':
            temp_x_in_base_m = temp_x_in_base_m[1:]
        else:
            break
    x_in_base_m = temp_x_in_base_m

    print('x in base m: ', end='')
    print(x_in_base_m)
    return x_in_base_m


print(convert_n_to_m('000', 10, 2))

