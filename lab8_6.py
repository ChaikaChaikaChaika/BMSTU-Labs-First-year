# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №8
# Выполнить транспонирование квадратной матрицы.

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

for i in range(0, n):
    for j in range(i+1, n):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print("Результат:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("{0:^7s}".format( str(arr[i][j])), end=' ')
    print()