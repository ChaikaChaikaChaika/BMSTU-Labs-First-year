# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №8
# найти строку, имеющую наибольшее количество нулевых элементов

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

max_0 = None
max_0_i = None
cur_0 = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            cur_0+=1
    if max_0 is None or cur_0 > max_0:
        max_0 = cur_0
        max_0_i = i
    cur_0 = 0

if max_0 is None or max_0 == 0:
    print("В матрице нет строк с нулевыми элементами.")
else:
    print("Строка с наибольшим количеством нулей: ")
    print(*arr[max_0_i])