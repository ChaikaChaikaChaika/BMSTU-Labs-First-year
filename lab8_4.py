# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №8
# Переставить местами столбцы с максимальной и минимальной суммой
# элементов.

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

min_sum = None
min_sum_j = None
max_sum = None
max_sum_j = None
cur_sum = 0
for j in range(m):
    for i in range(n):
        cur_sum += arr[i][j]
    if max_sum is None or max_sum < cur_sum:
        max_sum = cur_sum
        max_sum_j = j
    if min_sum is None or min_sum > cur_sum:
       min_sum = cur_sum
       min_sum_j = j
    cur_sum = 0
for i in range(n):
    arr[i][min_sum_j], arr[i][max_sum_j] = arr[i][max_sum_j], arr[i][min_sum_j]

print("Результат:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("{0:^7s}".format(str(arr[i][j])), end=' ')
    print()