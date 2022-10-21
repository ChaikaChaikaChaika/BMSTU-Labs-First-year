# Федченко Анастасия ИУ7-15Б
# Найти значение K-го экстремума в списке.

print("Введите элементы изначального списка через пробел:")
arr = list(map(int, input().split(' ')))
print("Введите каким по счёту должен быть экстремум:")
k = int(input())

count = 0
flag = False
for i in range(1, len(arr) - 1):
    if ((arr[i] < arr[i-1]) and (arr[i] < arr[i+1])) or ((arr[i] > arr[i-1]) and (arr[i] > arr[i+1])):
        count +=1
    if count == k and not flag:
        flag = True
        print("{0}-ый экстремум равен {1}".format(k, arr[i]))
        break

if flag == False:
    print("Экстремума с таким номером в списке нет.")
