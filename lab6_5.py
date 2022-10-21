# Федченко Анастасия ИУ7-15Б
# Поменять местами элементы с характеристиками
# Последний чётный и минимальный положительный

print("Введите элементы изначального списка через пробел:")
arr = list(map(int, input().split(' ')))

last_even = 0
last_even_i = -1
min_positive = -1
print(min_positive)
min_positive_i = -1

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        last_even = arr[i]
        last_even_i = i
    if arr[i] > 0 and (arr[i] < min_positive or min_positive == -1):
        min_positive = arr[i]
        min_positive_i = i

if last_even_i == -1:
    print("В списке нет чётных элеентов")
elif min_positive_i == -1:
    print("В списке нет положительных элементов")
elif last_even_i == min_positive_i:
    print("Нужные элементы совпадают")
else:
    temp = arr[last_even_i]
    arr[last_even_i] = arr[min_positive_i]
    arr[min_positive_i] = temp
    print("Результат:")
    for i in range(len(arr)):
        print(arr[i], end=' ')
