# Федченко Анастасия ИУ7-15б
# защита пятой лабораторной
# даны x и accuracy
# надо вывести сумму ряда

print("x = ", end='')
x = float(input())
print("accuracy = ", end='')
accuracy = float(input())

n = 0
fact = 1
sum = 0
flag = False
y = (x-1)**0.5
while not flag:
    n+=1
    y /= n
    print(n, fact, y)
    if abs(y)>accuracy:
        sum+=y
    else:
        flag = True
print('{0:.7}'.format(sum))

