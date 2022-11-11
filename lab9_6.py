# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №9
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.

n = int(input("Введите количество строк в матрицах A и B: "))
m = int(input("Введите количество столбцов в матрицах A и B: "))
print("Введите матрицу A: ")
A = []
for i in range(n):
    a = list(map(float, input().split(' ')))
    if len(a) == m:
        A.append(a)
    else:
        print("Колличество элементов в строке не соответствуем заявленному количеству.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break

print("Введите матрицу B: ")
B = []
for i in range(n):
    a = list(map(float, input().split(' ')))
    if len(a) == m:
        B.append(a)
    else:
        print("Колличество элементов в строке не соответствуем заявленному количеству.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break

C = []
for i in range(n):
    c = []
    for j in range(m):
        c.append(A[i][j]*B[i][j])
    C.append(c)

V = []
for j in range(m):
    v = 0
    for i in range(n):
        v+=C[i][j]
    V.append(v)

print("Матрица A:")
for i in range(len(A)):
    for j in range(len(A[i])):
        print("{0:^7s}".format(str(str('{0:.5}'.format(A[i][j])))), end=' ')
    print()
print("Матрица B:")
for i in range(len(B)):
    for j in range(len(B[i])):
        print("{0:^7s}".format(str(str('{0:.5}'.format(B[i][j])))), end=' ')
    print()
print("Матрица C:")
for i in range(len(C)):
    for j in range(len(C[i])):
        print("{0:^7s}".format(str('{0:.5}'.format(C[i][j]))), end=' ')
    print()
print("Массив V:")
for i in range(len(V)):
    print("{0:^7s}".format(str('{0:.5}'.format(V[i]))), end=' ')
print()