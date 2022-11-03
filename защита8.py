# Федченко Анастасия ИУ7-15Б
# защита 8
# на главной диавгонале разместить количество нечётных чисел в строке

n = int(input("Введите количество строк в матрице: "))
m = int(input("Введите количество столбцов в матрице: "))
arr = []
print("Введите матрицу: ")
for i in range(n):
    a = list(map(int, input().split(' ')))
    if len(a) != m:
        print("Количество элементов в строке не соответствует "
              "введённому ранее количеству столбцов в матрице.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break
    else:
        arr.append(a)

print("Изначальная матрица:")
for i in range(n):
    for j in range(m):
        print("{0:^7s}".format(str(arr[i][j])), end=' ')
    print()

if n == m:  # проверка на то, является ли матрица квадратной
    for i in range(n):
        count_1 = 0  # количество нечётных чисел в строке
        for j in range(m):
            if arr[i][j] % 2 == 1:
                count_1 += 1
        arr[i][i] = count_1
    print("Изменённая матрица:")
    for i in range(n):
        for j in range(m):
            print("{0:^7s}".format(str(arr[i][j])), end=' ')
        print()
else:
    print("Дальнейшие действия выполнить не получится тк матрица не квадратная.")
