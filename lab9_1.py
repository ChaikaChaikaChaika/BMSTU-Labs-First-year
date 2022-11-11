# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №9
# Даны массивы D и F. Сформировать матрицу A по формуле
# ajk = sin(dj+fk).
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.
import math

D = list(map(int, input("Введите масссив D: ").split()))
F = list(map(int, input("Введите масссив F: ").split()))

arr = []
for j in range(len(D)):
    a = []
    for k in range(len(F)):
        a.append(math.sin(D[j] + F[k]))
    arr.append(a)

AV = []
L = []
for i in range(len(arr)):
    sum = 0
    count = 0
    for j in range(len(arr[i])):  # подсчёт суммы и количества положительных элементов в строке
        if arr[i][j] > 0:
            sum += arr[i][j]
            count += 1
    if count:  # если в строке есть положительные числа
        AV.append(sum / count)
        count = 0
        for j in range(len(arr[i])):
            if arr[i][j] < AV[i]:
                count += 1
        L.append(count)
    else:  # если в строке нет положительных чисел
        AV.append(None)
        L.append(float(0))
    arr[i].append(AV[i])
    arr[i].append(float(L[i]))
print("Результат:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] is None:
            print("    -     ", end=' ')
        else:
            print("{0:^10s}".format(str('{0:.5}'.format(arr[i][j]))), end=' ')
    print()
