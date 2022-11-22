import random
import time


def gnome_sort(arr):
    """
    :param arr: исходный массив
    :return: [время сортировки, количество перестановок]
    """
    start_time = time.time()
    count = 0
    i = 1
    while i < len(arr):
        if i == 0:
            i = 1
        if arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            count += 1
            i -= 1
    finish_time = time.time()
    return [finish_time - start_time, count]


def calculations_for_table(N):
    """
    :param N: количество элементов тестовых массивов
    :return: [[время сортировки упорядоченного, количество перестановок в упорядоченном],
    [для рандомного], [для массива в обратном порядке]]
    """
    arr1 = [a for a in range(N)]
    arr2 = [a for a in range(N)]
    random.shuffle(arr2)
    arr3 = arr1[::-1]
    return [gnome_sort(arr1), gnome_sort(arr2), gnome_sort(arr3)]


# ввод с проверками
while ValueError:
    try:
        print("Введите массив, который надо отсортировать (в одну строку через пробел):")
        arr = list(map(int, input().split()))
    except ValueError:
        print("Массив должен состоять из целых чисел.")
        print("ППопробуйте ещё раз.")
    else:
        break
while ValueError or AssertionError:
    try:
        N1 = int(input("Введите первую размерность тестового массива: "))
        assert N1 > 0
    except ValueError:
        print("Размерность массива должна быть равна целому числу.")
        print("Попробуйте ещё раз.")
    except AssertionError:
        print("Размерность массива должна быть больше нуля.")
        print("Попробуйте ещё раз.")
    else:
        break
while ValueError or AssertionError:
    try:
        N2 = int(input("Введите вторую размерность тестового массива: "))
        assert N2 > 0
    except ValueError:
        print("Размерность массива должна быть равна целому числу.")
        print("Попробуйте ещё раз.")
    except AssertionError:
        print("Размерность массива должна быть больше нуля.")
        print("Попробуйте ещё раз.")
    else:
        break
while ValueError or AssertionError:
    try:
        N3 = int(input("Введите третью размерность тестового массива: "))
        assert N3 > 0
    except ValueError:
        print("Размерность массива должна быть равна целому числу.")
        print("Попробуйте ещё раз.")
    except AssertionError:
        print("Размерность массива должна быть больше нуля.")
        print("Попробуйте ещё раз.")
    else:
        break

gnome_sort(arr)  # сортировка массива
print(*arr)  # вывод отсортированного массива
# вычисление значений нужных для таблицы для каждого из N
res1 = calculations_for_table(N1)
res2 = calculations_for_table(N2)
res3 = calculations_for_table(N3)

# вывод таблицы
print('-' * 120)
print(
    "{0:29s}|{1:^29s}|{2:^29s}|{3:^30s}".format(' ', 'N1 = {}'.format(N1), 'N2 = {}'.format(N2), 'N3 = {}'.format(N3)))
print('-' * 120)
print("{0:29s}|{1:^14s}|{2:^14s}|{3:^14s}|{4:^14s}|{5:^14s}|{6:^14s}".format(' ', 'время', 'перестановки', 'время',
                                                                             'перестановки', 'время', 'перестановки'))
print('-' * 120)

print("{0:29s}|{1:^14s}|{2:^14s}|{3:^14s}|{4:^14s}|{5:^14s}|{6:^14s}".format('Упорядоченный список',
                                                                             '{0:.5}'.format(res1[0][0]),
                                                                             '{0}'.format(res1[0][1]),
                                                                             '{0:.5}'.format(res2[0][0]),
                                                                             '{0}'.format(res2[0][1]),
                                                                             '{0:.5}'.format(res3[0][0]),
                                                                             '{0}'.format(res3[0][1])))
print('-' * 120)
print("{0:29s}|{1:^14s}|{2:^14s}|{3:^14s}|{4:^14s}|{5:^14s}|{6:^14s}".format('Случайный список',
                                                                             '{0:.5}'.format(res1[1][0]),
                                                                             '{0}'.format(res1[1][1]),
                                                                             '{0:.5}'.format(res2[1][0]),
                                                                             '{0}'.format(res2[1][1]),
                                                                             '{0:.5}'.format(res3[1][0]),
                                                                             '{0}'.format(res3[1][1])))
print('-' * 120)
print("{0:29s}|{1:^14s}|{2:^14s}|{3:^14s}|{4:^14s}|{5:^14s}|{6:^14s}".format('В обратном порядке',
                                                                             '{0:.5}'.format(res1[2][0]),
                                                                             '{0}'.format(res1[2][1]),
                                                                             '{0:.5}'.format(res2[2][0]),
                                                                             '{0}'.format(res2[2][1]),
                                                                             '{0:.5}'.format(res3[2][0]),
                                                                             '{0}'.format(res3[2][1])))
print('-' * 120)
