# Федченко Анастасия ИУ7-15Б
# вычисление суммы ряда (по варианту) с точностью до члена ряда ε
# вариант 27

# print("Введите значение аргумента x = ", end='')
# x = float(input())
print("Введите точность accuracy = ", end='')
accuracy = float(input())
print("Введите шаг печати print_step = ", end='')
print_step = float(input())
print("Введите максимальное количество итераций iterations = ", end='')
iterations = float(input())
if abs(int(iterations) - iterations) > 1e-6:
    print("Значение итераций должно быть целочисленным.")
    print("Перезапутите программу и попробуйте снова.")
if accuracy <= 0:
    print("Значение точности должно быть положительным.")
    print("Перезапутите программу и попробуйте снова.")
if print_step <= 0:
    print("Количество шагов печати должно быть положительным.")
    print("Перезапутите программу и попробуйте снова.")

print("| {0:^12} | {1:^12} | {2:^12} |".format("№ итерации", 't', 's'))
print('-'*46)
i = 0
sum = 0
next_step = 0
flag = False
while iterations > 0:
    y = 1 / ((2 * i + 1) ** 2)
    sum += y
    s_y = str("{0:.5}".format(y))
    s_sum = str("{0:.5}".format(sum))
    if i == next_step:
        print("| {0:^12} | {1:^12} | {2:^12} |".format(str(i + 1), s_y, s_sum))
        next_step += print_step
    if 1 / ((2 * (i + 1) + 1) ** 2) <= accuracy:
        print()
        print("Сумма бесконечного ряда = {0}, вычислена за {1} итераций.".format(s_sum, i + 1))
        flag = True
        break
    iterations -= 1
    i += 1
if not(flag):
    print("За указанное число итераций необходимой точности достичь не удалось.")
