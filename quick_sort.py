def quick_sort(arr, l, r):
    pivot = arr[(l + r) // 2]
    i, j = l, r - 1
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if l <= j:
        quick_sort(arr, l, j + 1)
    if (r - 1) >= i:
        quick_sort(arr, i, r)


arr = [6, 5, 3, 1, 8, 7, 2, 4]
quick_sort(arr, 0, len(arr))
print(*arr)
