# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №9
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G.

n_d = int(input("Введите количество строк в матрице D: "))
m_d = int(input("Введите количество столбцов в матрице D: "))
print("Введите матрицу D: ")
D = []
for i in range(n_d):
    a = list(map(int, input().split(' ')))
    if len(a) == m_d:
        D.append(a)
    else:
        print("Колличество элементов в строке не соответствуем заявленному количеству.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break

n_z = int(input("Введите количество строк в матрице Z: "))
m_z = int(input("Введите количество столбцов в матрице Z: "))
print("Введите матрицу Z: ")
Z = []
for i in range(n_z):
    a = list(map(int, input().split(' ')))
    if len(a) == m_z:
        Z.append(a)
    else:
        print("Колличество элементов в строке не соответствуем заявленному количеству.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break

if len(D) != len(Z):
    print("Задача не может быть выполнена тк в матрицах разное количество строк")
else:
    print("--------------------Результат--------------------")
    print("Исходная матрица D:")
    for i in range(len(D)):
        for j in range(len(D[i])):
            print("{0:^7s}".format(str(D[i][j])), end=' ')
        print()

    print("Исходная матрица Z:")
    for i in range(len(Z)):
        for j in range(len(Z[i])):
            print("{0:^7s}".format(str(Z[i][j])), end=' ')
        print()

    G = []
    for i in range(len(D)):
        g = 0
        sum_x_i = sum(Z[i])
        for j in range(len(D[i])):
            if D[i][j] > sum_x_i:
                g+=1
        G.append(g)

    print("Массив G:")
    for i in range(len(G)):
        print("{0:^7s}".format(str(G[i])), end=' ')
    print()

    Max_G = max(G)
    for i in range(len(D)):
        for j in range(len(D[i])):
            D[i][j] = D[i][j]*Max_G

    print("Изменённая матрица D:")
    for i in range(len(D)):
        for j in range(len(D[i])):
            print("{0:^7s}".format(str(D[i][j])), end=' ')
        print()


