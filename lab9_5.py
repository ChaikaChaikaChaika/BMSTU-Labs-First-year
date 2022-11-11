# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №9
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.

n = int(input("Введите количество строк в матрице: "))
m = int(input("Введите количество столбцов в матрице: "))
print("Введите матрицу: ")
arr = []
for i in range(n):
    a = list(input().split(' '))
    if any(len(x) != 1 for x in a):
        print("Один из элементов в строке не является символом.")
        print("Перезапустите программу и попробуйте ещё раз.")
    elif len(a) == m:
        arr.append(a)
    else:
        print("Количество элементов в строке не соответствуем заявленному количеству.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break
print("Изначальная матрица:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("{0:^7s}".format(str(arr[i][j])), end=' ')
    print()

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] in vowels:
            arr[i][j] = '.'
print("Изменённая матрица:")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("{0:^7s}".format(str(arr[i][j])), end=' ')
    print()