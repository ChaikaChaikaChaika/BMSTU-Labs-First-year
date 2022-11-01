# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №8
# найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2

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
max_2 = 0
max_2_j = None
cur_2 = 0
for j in range(m):
    for i in range(n):
        x = abs(arr[i][j])
        flag = True
        if x == 0: # проверка на ноль (тк ед. не проходит через цикл и не является степенью двойки)
            flag = False
        while x > 1: # последовательно делим на 2 и смотрим на остаток
            if arr[i][j] % 2 != 0:
                flag = False
                break
            else:
                x //= 2
        if flag:
            cur_2 += 1
    #print(j, cur_2)
    if cur_2 > max_2:
       max_2 = cur_2
       max_2_j = j
    cur_2 = 0
if max_2 == 0:
    print("Таких столбцов в матрице нет.")
else:
    print("Результат:")
    for i in range(n):
        print(arr[i][max_2_j])