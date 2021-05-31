"""Завдання 8.2"""


def find_fraction(summ):
    half = summ // 2

    for i in range(half):
        if summ % 2 == 0:
            up = half - 1 - i
        else:
            up = half - i
        down = summ - up

        up1 = up
        down1 = down
        while up1 != 0 and down1 != 0:
            if up1 > down1:
                up1 = up1 % down1
            else:
                down1 = down1 % up1

        if not(up1 > 1 or down1 > 1):
            return up, down
    return False


num = 150000001

print(find_fraction(num))
