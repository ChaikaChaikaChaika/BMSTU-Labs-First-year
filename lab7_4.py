# Федченко Анастасия ИУ7-15Б
# Замена всех цифр на пробелы
arr = []
n = int(input("Введите количество элементов в массиве: "))
if n<= 0:
    print("Количество элементов в списке должно быть > 0.")
    print("Перезапустите программу и попробуйте ещё раз.")
else:
    for i in range(n):
        arr.append(input())
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].isdigit():
                arr[i] = arr[i].replace(arr[i][j], ' ')
    for i in range(len(arr)):
            print(arr[i])
