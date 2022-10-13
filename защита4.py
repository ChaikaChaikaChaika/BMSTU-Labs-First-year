# y = 2*(x**3) + 3*(x**2)- 6*x +1.5
print("x0 = ", end='')
s_x0 = input()
print("h = ", end='')
s_h = input()
print("xn = ", end='')
s_xn = input()
n_x0, n_h, n_xn = 0, 0, 0
if len(s_x0.split('.')) != 1:
    n_x0 = len(s_x0.split('.')[1])
if len(s_h.split('.')) != 1:
    n_h = len(s_h.split('.')[1])
if len(s_xn.split('.')) != 1:
    n_xn = len(s_xn.split('.')[1])
k = max(n_x0, n_h, n_xn)
x0, h, xn = float(s_x0), float(s_h), float(s_xn)
max_y, min_y = -999999999999999999 * (10 ** 40), 999999999999999999 * (10 ** 40)
for i in range(int(x0 * (10 ** k)), int(xn * (10 ** k)) + int(h * (10 ** k)), int(h * (10 ** k))):
    if i <= int(xn * (10 ** k)):
        x = i / (10 ** k)
        y = 2 * (x ** 3) + 3 * (x ** 2) - 6 * x + 1.5
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

s_max_y = str("{0:.5}".format(float(max_y)))
s_min_y = str("{0:.5}".format(float(min_y)))
char_size = (max_y - min_y) / 150
print((12 - len(s_min_y) // 2) * " " + s_min_y, end='')
if 0 > x0 and 0 < xn:
    spaces_from_min_to_0 = int(round(abs(0 - min_y) / char_size))
    print((spaces_from_min_to_0 - len(s_min_y) // 2 - 1) * ' ' + '0', end='')
    spaces_from_0_to_max = int(round(abs(max_y - 0) / char_size))
    print((spaces_from_0_to_max - len(s_max_y) // 2) * ' ' + s_max_y)
else:
    spaces_from_min_to_max = int(round(abs(max_y - min_y) / char_size))
    print((spaces_from_min_to_max - (len(s_min_y) // 2) - (len(s_max_y) // 2)) * ' ' + s_max_y)

for i in range(int(x0 * (10 ** k)), int(xn * (10 ** k)) + int(h * (10 ** k)), int(h * (10 ** k))):
    if i <= int(xn * (10 ** k)):
        x = i / (10 ** k)
        y = 2 * (x ** 3) + 3 * (x ** 2) - 6 * x + 1.5
        s_x = str("{0:.5}".format(x))
        spaces = int(round(abs(y - min_y) / char_size))
        print('{0:10s} |'.format(s_x), end='')
        print(' ' * spaces + '*')
