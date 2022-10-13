# Федченко Анастасия ИУ7-15Б
# определение лежит ли точка внутри треугольника
import math

print("Введите координаты 1-ой вершины треугольника: ", end=' ')
x1, y1 = map(int, input().split())
print("Введите координаты 2-ой вершины треугольника: ", end=' ')
x2, y2 = map(int, input().split())
print("Введите координаты 3-ей вершины треугольника: ", end=' ')
x3, y3 = map(int, input().split())
length12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2)  # вычисление длин сторон треугольника в квадрате
length13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2)
length23 = ((x2 - x3) ** 2 + (y2 - y3) ** 2)
if ((length12 ** 0.5 + length13 ** 0.5 - length23 ** 0.5) < 1e-6) or (
        (length12 ** 0.5 + length23 ** 0.5 - length13 ** 0.5) < 1e-6) or \
        ((length23 ** 0.5 + length13 ** 0.5 - length12 ** 0.5) < 1e-6):  # проверка не лежат ли точки на одной прямой
    print("Заданные точки лежат на одной прямой и не могут образовывать треугольник.")
    print("Перезапустите программу и введите значения снова.")
else:
    print("Стороны равны: {0:.5} {1:.5} {2:.5}".format(length12 ** 0.5, length13 ** 0.5, length23 ** 0.5))
    cos_angle123 = (length12 + length23 - length13) / (2 * length12 ** 0.5 * length23 ** 0.5)  # нахождение cos 123
    cos_angle132 = (length13 + length23 - length12) / (2 * length13 ** 0.5 * length23 ** 0.5)  # нахождение cos 132
    cos_angle213 = (length12 + length13 - length23) / (2 * length12 ** 0.5 * length13 ** 0.5)  # нахождение cos 213
    # print(cos_angle123, cos_angle132, cos_angle213)
    mediana = 0
    if cos_angle213 > cos_angle132 and cos_angle213 > cos_angle123:  # нахождение медианы если самый маленький угол 213
        x = length23 / 4
        mediana = (length12 + x - 2 * length12 ** 0.5 * x ** 0.5 * cos_angle123) ** 0.5
    if cos_angle123 > cos_angle132 and cos_angle123 > cos_angle213:  # нахождение медианы если самый маленький угол 123
        x = length13 / 4
        mediana = (length23 + x - 2 * length23 ** 0.5 * x ** 0.4 * cos_angle132) ** 0.5
    if cos_angle132 > cos_angle123 and cos_angle132 > cos_angle213:  # нахождение медианы если самый маленький угол 132
        x = length12 / 2
        mediana = (length13 + x - 2 * length13 ** 0.5 * x ** 0.5 * cos_angle213) ** 0.5
    print("Длина медианы проведённой из наименьшего угла {0:.5}".format(mediana))
    if cos_angle123 < 0 or cos_angle132 < 0 or cos_angle213 < 0:  # проверка на тупоугольность
        print("Треугольник является тупоугольным")
    else:
        print("Треугольник НЕ является тупоугольным")

    print("Введите координаты свободной точки ", end='')
    x4, y4 = map(int, input().split())
    length14 = ((x1 - x4) ** 2 + (y1 - y4) ** 2)  # вычисление расстояния от 4ой точки до вершин трегольника в кв
    length24 = ((x2 - x4) ** 2 + (y2 - y4) ** 2)
    length34 = ((x3 - x4) ** 2 + (y3 - y4) ** 2)
    sum_S = 0
    if not ((length12 ** 0.5 + length14 ** 0.5 - length24 ** 0.5) < 1e-6 or \
            (length12 ** 0.5 + length24 ** 0.5 - length14 ** 0.5) < 1e-6 or \
            (length24 ** 0.5 + length14 ** 0.5 - length12 ** 0.5) < 1e-6):  # проверка если не лежат ли на одной прямой
        p = (length12 ** 0.5 + length14 ** 0.5 + length24 ** 0.5) / 2  # полупериметр треугольника 124
        sum_S += (p * (p - length12 ** 0.5) * (p - length14 ** 0.5) * (p - length24 ** 0.5)) ** 0.5  # площадь 124
    if not ((length24 ** 0.5 + length34 ** 0.5 - length23 ** 0.5) < 1e-6 or \
            (length23 ** 0.5 + length24 ** 0.5 - length34 ** 0.5) < 1e-6 or \
            (length23 ** 0.5 + length34 ** 0.5 - length24 ** 0.5) < 1e-6):  # проверка если не лежат ли на одной прямой
        p = (length23 ** 0.5 + length24 ** 0.5 + length34 ** 0.5) / 2  # полупериметр треугольника 234
        sum_S += (p * (p - length23 ** 0.5) * (p - length24 ** 0.5) * (p - length34 ** 0.5)) ** 0.5  # площадь 234
    if not ((length14 ** 0.5 + length34 ** 0.5 - length13 ** 0.5)< 1e-6 or \
            (length14 ** 0.5 + length13 ** 0.5 - length34 ** 0.5) < 1e-6or \
            (length13 ** 0.5 + length34 ** 0.5 - length14 ** 0.5) < 1e-6):  # проверка если не лежат ли на одной прямой
        p = (length14 ** 0.5 + length34 ** 0.5 + length13 ** 0.5) / 2  # полупериметр треугольника 134
        sum_S += (p * (p - length14 ** 0.5) * (p - length34 ** 0.5) * (p - length13 ** 0.5)) ** 0.5  # площадь 134

    P = (length12 ** 0.5 + length13 ** 0.5 + length23 ** 0.5) / 2  # полупериметр исходного треугольника
    S = (P * (P - length12 ** 0.5) * (P - length13 ** 0.5) * (P - length23 ** 0.5)) ** 0.5  # площадь исходного
    # print(S, sum_S)
    if abs(sum_S - S) < 1e-6:  # если сумма площадей равна площади исходного треугольника
        print("Точка находится внутри треугольника")
        # вычисление расстояний от точки до прямых содержащих стороны треугольника и нахождение максимального
        d12 = abs((y2 - y1) * x4 - (x2 - x1) * y4 - x1 * y2 + x2 * y1) / (((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5)
        d13 = abs((y3 - y1) * x4 - (x3 - x1) * y4 - x1 * y3 + x3 * y1) / (((y3 - y1) ** 2 + (x3 - x1) ** 2) ** 0.5)
        d23 = abs((y3 - y2) * x4 - (x3 - x2) * y4 - x2 * y3 + x3 * y2) / (((y3 - y2) ** 2 + (x3 - x2) ** 2) ** 0.5)
        print("Расстояние от точки до наиболее удаленной стороны {0:.5}".format(max(d12, d13, d23)))
    else:
        print("Точка НЕ находится внутри треугольника")
