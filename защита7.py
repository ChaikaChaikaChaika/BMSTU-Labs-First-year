# Федченко Анастасия ИУ7-15Б
# защита Седьмой лабораторной
# в массиве после каждого эл нужно добавить ср геом включая этот эл
# 1 2 3 4
# 1 1 2 1,41 3 1,817 4 2,21
# 24 7 23 47 32
#24 24 7 12,96 23 15,69 47 20,64 32 22,5

arr = list(map(int, input().split(' ')))
arr = [0]*len(arr) + arr
res_i = 0 # результирующий индекс
k = 1 # коэфициент для вычисления нужной степени
composition = 1 # произведение предыдущих элементов исходного массива
for i in range(len(arr)//2, len(arr)):
    arr[res_i] = float(arr[i])
    composition*=arr[i]
    res_i += 1
    arr[res_i] = composition**(1/k)
    k+=1
    res_i+=1
for i in range(len(arr)):
    print("{0:.5}".format(arr[i]), end=' ')