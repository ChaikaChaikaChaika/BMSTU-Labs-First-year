# Федченко Анастасия ИУ7-15Б
# Поиск элемента в списке строк по варианту.
# Поиск наиболее короткого элемента, не содержащего пробелов

arr = []
n = int(input("Введите количество элементов в массиве: "))
if n<= 0:
    print("Количество элементов в списке должно быть > 0.")
    print("Перезапустите программу и попробуйте ещё раз.")
else:
    for i in range(n):
        arr.append(input())
    min_l = None
    min_l_i = None
    for i in range(len(arr)):
        if arr[i].count(' ') == 0:
            if min_l is None or len(arr[i])<min_l:
                min_l_i = i
                min_l = len(arr[i])
    if min_l is None:
        print("Такого элемента в списке нет.")
    else:
        print(arr[min_l_i])
