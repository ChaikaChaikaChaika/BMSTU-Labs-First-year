# Федченко Анастасия ИУ7-15Б
# После каждого элемента целочисленного списка, имеющего свойство по варианту,
# добавить его удвоенное значение, без использования вложенных циклов.
# Отрицательные элементы

arr = list(map(int, input("Введите список: ").split(' ')))
# в этом способе я не жалею место, использую второй массив
'''res = []
for i in range(len(arr)):
    res.append(arr[i])
    if arr[i]<0:
        res.append(arr[i]*2)
    
print(*res)'''
count_negative = 0
for i in range(len(arr)):
    if arr[i] < 0:
        count_negative += 1
arr = [0] * count_negative + arr
res_i = 0
for i in range(count_negative, len(arr)):
    arr[res_i] = arr[i]
    res_i += 1
    if arr[i] < 0:
        arr[res_i] = arr[i] * 2
        res_i+=1
if len(arr) == 0:
    print("Список пуст")
else:
    print(*arr)
