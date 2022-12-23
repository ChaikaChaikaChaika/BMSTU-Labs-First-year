# Федченко Анастасия ИУ7-15б
# защита 14
import struct

format = '20si'
step = struct.calcsize(format)
print("Введите путь до файла (он должен заканчиваться на [название].bin): ", end="")
path = input()
file = open(path, 'wb')
print("Введите количество записей в базе (целое число): ", end="")
n = int(input())
for i in range(n):
    print("№{0}".format(i+1))
    surname = input("Введите фамилию: ")
    surname = surname + " "*(20 - len(surname))
    score = int(input("Введите оценку: "))
    file.write(struct.pack(format, bytes(surname, encoding='utf-8'), score))
file.close()
file = open(path, 'rb+')
r = 0
w = 0
count = 0
x = file.read(step)
while x != b'':
    a = list(struct.unpack(format, x))
    if a[1] != 2:
        #print("переписываю ", a)
        count += 1
        file.seek(step*w, 0)
        file.write(x)
        w += 1
    r += 1
    file.seek(step*r, 0)
    x = file.read(step)

file.truncate(step*count)
print("Результат: ")
file.seek(0, 0)
x = file.read(step)
c = 0
while x != b'':
    a = list(struct.unpack(format, x))
    if c == 0:
        print("{0:^20s} | {1:^8s}".format("Фамилия", "Оценка"))
        print("-"*31)
    print("{0:^20s} | {1:^8s}".format(a[0].decode('utf-8').rstrip(" "), str(a[1])))
    c+=1
    x = file.read(step)
file.close()