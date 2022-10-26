# Федченко Анастасия ИУ7-15Б
# Защита шестой лабораторной
# найти последнюю наименее длинную непрерывную последовательность убывающих по модулю чисел
# 5 4 3 2 5
# 5 4 3 2 3 4 3

arr = list(map(int, input().split(' ')))
s_res, f_res, s_cur, f_cur = 0, 0, -1, -1
flag = False
for i in range(0, len(arr)):
    #print('i = ', i)
    if s_cur == -1 and f_cur == -1:
        s_cur = i
        f_cur = i
        #print("cur", s_cur, f_cur)
    elif abs(arr[i]) < abs(arr[i - 1]):
        f_cur = i
        #print("cur", s_cur, f_cur)
    elif (not flag) or ((f_res - s_res) >= (f_cur - s_cur)):
        s_res = s_cur
        f_res = f_cur
        #print("res", s_res, f_res)
        flag = True
        s_cur, f_cur = i, i
        #print("cur", s_cur, f_cur)
if (not flag) or ((f_res - s_res) >= (f_cur - s_cur)):
    s_res = s_cur
    f_res = f_cur
    #print("res", s_res, f_res)

for i in range(s_res, f_res + 1):
    print(arr[i], end=' ')
