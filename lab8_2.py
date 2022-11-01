# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №8
# Переставить местами строки с max и min количеством отрицательных элементов

n = int(input("Введите количество строк в матрице: "))
m = int(input("Введите количество столбцов в матрице: "))
print("Введите матрицу: ")
arr = []
for i in range(n):
    a = list(map(int, input().split(' ')))
    if len(a) == m:
        arr.append(a)
    else:
        print("Колличество элементов в строке не соответствуем заявленному количеству.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break

max_n = None
max_n_i = None
min_n = None
min_n_i = None
cur_n = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < 0:
            cur_n += 1
    if max_n is None or cur_n > max_n:
        max_n = cur_n
        max_n_i = i
    if min_n is None or cur_n < min_n:
        min_n = cur_n
        min_n_i = i
    #print(max_n, min_n)
    cur_n = 0
if max_n == 0 and min_n == 0:
    print("В этой матрице нет строк, содержащих отрицательные элементы.")
else:
    arr[max_n_i], arr[min_n_i] = arr[min_n_i], arr[max_n_i]
    print("Результат: ")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print("{0:^7s}".format( str(arr[i][j])), end=' ')
        print()
