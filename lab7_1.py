# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №7
# Удалить все элементы целочисленного списка, имеющие свойство по варианту,
# за один цикл
# Отрицательные элементы

arr = list(map(int, input("Введите список: ").split(' ')))
# вариант со срезами, но я не уверена что срезы не будут внутри представлять собой вложенные циклы
i = 0
while i < len(arr):
    if arr[i] < 0:
        arr = arr[:i] + arr[(i+1): len(arr)]
    else:
        i+=1

# вариант с перестановкой согласно индексам, но здесь два цикла,
# тк надо удалить остатки, иначе массив будет непрвильный
'''res_i = 0
for now in range(len(arr)):
    if arr[now] >= 0:
        arr[res_i] = arr[now]
        res_i += 1
for i in range(0, len(arr) - res_i):
    arr.pop()'''
if len(arr) == 0:
    print("Список пуст")
else:
    print(*arr)
