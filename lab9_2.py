# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №9
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.

n = int(input("Введите количество строк и столбцов в матрице: "))
print("Введите матрицу: ")
arr = []
for i in range(n):
    a = list(map(int, input().split(' ')))
    if len(a) == n:
        arr.append(a)
    else:
        print("Колличество элементов в строке не соответствуем заявленному количеству.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break
# поворот на 90 по часовой
# контуров будет n//2
for t in range(n // 2):
    for r in range(t, n - 1 - t):
        '''print(t,r)
        print(r, n-t-1)
        print(n-t-1, n-r-1)
        print(n-r-1, t)
        print()'''
        arr[t][r], arr[r][n-t-1], arr[n-t-1][n-r-1], arr[n-r-1][t] = arr[n-r-1][t], arr[t][r], arr[r][n-t-1], arr[n-t-1][n-r-1]

print("Промежуточный результат:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("{0:^7s}".format(str(arr[i][j])), end=' ')
    print()

# поворот на 90 против часовой
for t in range(n // 2):
    for r in range(t, n - 1 - t):
        arr[t][r], arr[r][n-t-1], arr[n-t-1][n-r-1], arr[n-r-1][t] = arr[r][n-t-1], arr[n-t-1][n-r-1], arr[n-r-1][t], arr[t][r]


print("Результат:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("{0:^7s}".format(str(arr[i][j])), end=' ')
    print()
