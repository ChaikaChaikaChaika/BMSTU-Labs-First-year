# Федченко Анастасия ИУ7-15Б
# Найти наиболее длинную непрерывную последовательность
# Возрастающая последовательность отрицательных чисел, модуль которых
# является простым числом.

print("Введите элементы изначального списка через пробел:")
arr = list(map(int, input().split(' ')))
current, result = [], []

if arr[0] < 0:
    current.append(arr[0])
i = 1
while i < len(arr):
    # print(i)
    x = abs(arr[i])
    is_prime = True  # проверка на простоту
    if x == 1:
        is_prime = False
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            is_prime = False
    # проверка на условие задачи
    if (arr[i] < 0) and ((arr[i] > arr[i - 1]) or (len(current) == 0)) and is_prime:
        current.append(arr[i])
    else:
        if len(current) > len(result):  # замена результата, если нынешнее больше
            result = current.copy()
            i -= 1
        current.clear()

    i += 1
    # print(current)
if len(current) > len(result):
    result = current.copy()
if len(result) == 0:
    print("Последовательности обладающей такими характеристиками в этом списке нет")
else:
    print("Возрастающая последовательность отрицательных чисел, модуль которых является простым числом.")
for i in range(len(result)):
    print(result[i], end=' ')
