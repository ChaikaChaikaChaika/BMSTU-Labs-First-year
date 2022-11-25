# Федченко Анастасия ИУ7-15Б
# защита 11
# реализация быстрой сортировки

def quick_sort(l, r, arr):
    i = l
    j = r - 1
    pivot = arr[(l + r) // 2]  # средний элемент, относительно которого будем проверять
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if l <= j:  # проверяем есть ли куда двигаться влево
        quick_sort(l, j + 1, arr)
    if (r - 1) >= i:  # проверяем есть ли куда двигаться вправо
        quick_sort(i, r, arr)


print("Введите массив, который надо отсортировать:")
arr = list(map(int, input().split()))
quick_sort(0, len(arr), arr)
print("Отсортированный массив")
print(*arr)
