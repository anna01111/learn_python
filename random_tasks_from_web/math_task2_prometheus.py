import sys
import math

x = float(sys.argv[1])
m = float(sys.argv[2])
q = float(sys.argv[3])


x_one = q * math.sqrt(2 * math.pi)
x_two = (x - m) ** 2
x_three = 2 * q ** 2


res = (1 / x_one) * math.exp(- x_two / x_three)
print(res)

