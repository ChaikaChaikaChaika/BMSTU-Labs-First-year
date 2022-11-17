# Федченко Анастасия ИУ7-15Б
# защита 9
# в матрице найти столбец с наибольшим количеством нечётных чисел и поменять с последней строкой
N = int(input("Введите количество строк в матрице: "))
K = int(input("Введите количество столбцов в матрице: "))
print("Введите матрицу (построчно через пробел)")
arr = []
for i in range(N):
    a = list(map(int, input().split(' ')))
    if len(a) != K:
        print("Количество элементов в строке не соответствует количество столбцов.")
        print("Перезапустите программу и попробуйте ещё раз.")
        break
    else:
        arr.append(a)
print("Введённая матрица:")
for i in range(N):
    for j in range(K):
        print('{0:^8s}'.format(str(arr[i][j])), end=' ')
    print()
max_1 = None
max_1_j = None
for j in range(K):
    cur_1 = 0
    for i in range(N):
        if arr[i][j] % 2 == 1:
            cur_1 += 1
    if max_1 is None or max_1 < cur_1:
        max_1 = cur_1
        max_1_j = j

print("Номер столбца с наибольшим количеством нечётных элементов:", max_1_j + 1)
if N!= K:
    print("К сожалению, не получится поменять этот столбец с последней строкой тк нужно чтобы матрица была квадратной.")
else:
    x = 0
    y = 0
    while(x<K and y<K):
        if x == max_1_j:
            x+=1
        if x<K and y<K:
            arr[len(arr)-1][x], arr[y][max_1_j] = arr[y][max_1_j], arr[len(arr)-1][x]
        x+=1
        y+=1
    #arr[]

    for i in range(N):
        for j in range(K):
            print('{0:^8s}'.format(str(arr[i][j])), end=' ')
        print()
