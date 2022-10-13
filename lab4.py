# Федченко Анастасия ИУ7-15Б
# построение таблицы значения и графика функций
# вариант 19
# y1 = 9.45*(x**4) + 5 *(x**3) - 4.37*(x**2) - 0.28*x - 0.35
# y2 = (x-1)**2 - 0.5*(e**x)
import math

# print(' '*170)

print("Введите начальное значение x0 = ", end='')
x0 = input()
print("Введите значение шага h = ", end='')
h = input()
print("Введите конечное значение xn = ", end='')
xn = input()
if float(x0) >= float(xn):
    print("Начальное значение x должно быть меньше конечного.")
    print("Перезапутите программу и попробуйте снова.")
elif float(x0) + float(h) > float(xn):
    print("Этот шаг слишком большой для данного промежутка.")
    print("Перезапутите программу и попробуйте снова.")
elif float(h) <= 0:
    print("Шаг должен быть больше нуля.")
    print("Перезапутите программу и попробуйте снова.")
else:
    x0_str, h_str, xn_str = '', '', ''  # определение у какого числа больше дробная часть
    if len(x0.split('.')) > 1:
        x0_str = x0.split('.')[1]  # смотрю у какого числа больше дробная часть
    if len(h.split('.')) > 1:
        h_str = h.split('.')[1]  # чтобы потом посмотреть на десять в какой степени нам надо будет домножить
    if len(xn.split('.')) > 1:
        xn_str = xn.split('.')[1]  # для правильной работы с range
    k = max(len(x0_str), len(h_str), len(xn_str))
    f_x0, f_h, f_xn = int(float(x0) * (10 ** k)), int(float(h) * (10 ** k)), int(float(xn) * (10 ** k))
    # print(x0, h, xn)
    print('-' * 45)
    print("| {0:12s} | {1:12s} | {2:12s} |".format('x', 'y1', 'y2'))
    print('-' * 45)

    for i in range(f_x0, f_xn + f_h, f_h):  # вывод таблицы
        if i<=f_xn:
            x = i / (10 ** k)
            y1 = 9.45 * (x ** 4) + 5 * (x ** 3) - 4.37 * (x ** 2) - 0.28 * x - 0.35
            y2 = (x - 1) ** 2 - 0.5 * (math.e ** x)
            x_str = str("{0:.5}".format(x))
            y1_str = str("{0:.5}".format(y1))
            y2_str = str("{0:.5}".format(y2))
            # print(x_str, y1_str, y2_str)
            print("| {0:12s} | {1:12s} | {2:12s} |".format(x_str, y1_str, y2_str))
            # print("%5f" % (x), "%5f" % (y1), "%5f" % (y2))
            # print("{0:5s} {1:5s} {2:5s}".format(x, y1, y2))
            # #print("{0:.4}".format(9.45*(x**4) + 5 *(x**3) - 4.37*(x**2) - 0.28*x - 0.35), end=' ')
    print('-' * 45)

    print("График первой функции y = 9.45*(x^4) + 5 *(x^3) - 4.37*(x^2) - 0.28*x - 0.35")
    print("Введите количество засечек n = ", end='')
    n = int(input()) - 2
    while (n + 2) < 4 or (n + 2) > 8:
        print("Колличество засечек должно быть 4 <= n <= 8.")
        print("Попробуйте ещё раз")
        print("Введите количество засечек n = ", end='')
        n = int(input()) - 2
    max_y = -99999999999 * (10 ** 50)
    min_y = 99999999999 * (10 ** 50)
    for i in range(f_x0, f_xn + f_h, f_h):  # нахождение максимума и минимума на заданном промежутке
        if i <= f_xn:
            x = i / (10 ** k)
            if (9.45 * (x ** 4) + 5 * (x ** 3) - 4.37 * (x ** 2) - 0.28 * x - 0.35) > max_y:
                max_y = (9.45 * (x ** 4) + 5 * (x ** 3) - 4.37 * (x ** 2) - 0.28 * x - 0.35)
            if (9.45 * (x ** 4) + 5 * (x ** 3) - 4.37 * (x ** 2) - 0.28 * x - 0.35) < min_y:
                min_y = (9.45 * (x ** 4) + 5 * (x ** 3) - 4.37 * (x ** 2) - 0.28 * x - 0.35)

    # print(min_y, max_y)
    # print(min_y, max_y)
    one_marker = (max_y - min_y) / (n + 1)  # длина одной засечки
    one_char = (max_y - min_y) / 150  # длина одного элемента
    gap = int(round(one_marker / one_char))  # какому значению равен один размер засечки
    min_y_str = str("{0:.5}".format(min_y))
    max_y_str = str("{0:.5}".format(max_y))
    print(' ' * (10 - len(min_y_str) // 2) + min_y_str, end='')
    pred = (len(min_y_str) + 1) // 2  # сколько пробелов отнимаентся из-за предыдущего
    for i in range(1, n + 1):
        y = min_y + i * one_marker
        y_str = str("{0:.5}".format(y))
        print(' ' * (gap - (len(y_str) + 1) // 2 - pred) + y_str, end='')
        pred = len(y_str) // 2
    print(' ' * (gap - (len(max_y_str) + 1) // 2 - pred) + max_y_str)
    # print(min_y)
    for i in range(f_x0, f_xn + f_h, f_h):
        if i <= f_xn:
            x = i / (10 ** k)
            x_str = str("{0:.5}".format(x))  # вывод числа x
            print("{0:8s} |".format(x_str), end='')
            y = (9.45 * (x ** 4) + 5 * (x ** 3) - 4.37 * (x ** 2) - 0.28 * x - 0.35)
            spaces = int(round(abs(y - min_y) / one_char)) - 1  # высчитывание количества пробелов для y
            spaces_for_zero = int(round(abs(0 - min_y) / one_char)) - 1  # высчитывание количества пробелов для 0
            # print(spaces, spaces_for_zero, y - max_y, y - min_y)
            if spaces < 0:
                spaces = 0
            if spaces_for_zero < 0:
                spaces_for_zero = 0
            if spaces_for_zero < spaces:
                if spaces_for_zero < 170:
                    print(' ' * spaces_for_zero + "|", end='')
                    print(' ' * (spaces - spaces_for_zero - 1) + "*")
                else:
                    print(' ' * (spaces - 1) + "*")
                # print(spaces)
            elif spaces_for_zero > spaces:
                print(' ' * spaces + "*", end='')
                if spaces_for_zero < 170:
                    print(' ' * (spaces_for_zero - spaces - 1) + "|")
                else:
                    print()
                # print(spaces)
            else:
                print(' ' * spaces + "*")

        # print(y, (y - min_y), spaces)
