# Федченко Анастасия ИУ7-15Б
# Удалить элемент с заданным индексом алгоритмически.

print("Введите элементы изначального списка через пробел:")
arr = list(map(int, input().split(' ')))
print("Введите индекс места в списке, откуда нужно удалить элемент:")
n = int(input()) - 1
if n < 0:
    print("Индекс места в списке должен быть > 0")
    print("Перезапуcтите программу и попробуйте снова.")
elif n > (len(arr) + 1):
    print("Индекс места в списке должен быть <= длинны списка")
    print("Перезапуcтите программу и попробуйте снова.")
else:
    for i in range(n, len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    if len(arr) == 0:
        print("Список пуст")
    else:
        for i in range(len(arr)):
            print(arr[i], end=' ')
