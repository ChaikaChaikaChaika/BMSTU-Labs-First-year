# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №10
# Вычисление приближённого значения интеграла
import math

import numpy as numpy


def f(x: float) -> float:
    """
    :param x: function argument
    :return: function value
    """
    try:
        y = 8
    except:
        return None
    else:
        return 8


def F(x: float) -> float:
    """
    :param x: argument
    :return: the value of the primitive from the argument without const
    """
    return 8*x


def right_rectangle_method(a: float, b: float, N: int) -> float:
    """
    :param a: the start of the integration segment
    :param b: the end of the integration segment
    :param N: number of partitioning sections
    :return: value of the integral calculated by right rectangle method
    """
    sum = 0
    h = (b - a) / N
    for i in range(1, N + 1):
        if f(a + i * h) is None:
            return None
        sum += (h * f(a + i * h))
    return sum


def trapeze_method(a: float, b: float, N: int) -> float:
    """
    :param a: the start of the integration segment
    :param b: the end of the integration segment
    :param N: number of partitioning sections
    :return: value of the integral calculated by trapeze method
    """
    sum = 0
    h = (b - a) / N
    for i in range(1, N + 1):
        if f(a + (i - 1) * h) is None or f(a + i * h) is None:
            return None
        sum += (h * (f(a + (i - 1) * h) + f(a + i * h)) * 0.5)
    return sum


def display(N1: int, N2: int, rm1: float, rm2: float, tm1: float, tm2: float) -> None:
    """
    is being used for table output
    :param N1: first number of partitioning sections
    :param N2: second number of partitioning sections
    :param rm1: value for right rectangle method with use of N1
    :param rm2: value for right rectangle method with use of N2
    :param tm1: value for trapeze method with use of N1
    :param tm2: value for trapeze method with use of N2
    :return: None
    """
    print('-' * 90)
    print("{0:29s}|{1:^29s}|{2:^30s}".format(' ', 'N1 = {}'.format(N1), 'N2 = {}'.format(N2)))
    print('-' * 90)
    print("{0:29s}|{1:^29s}|{2:^30s}".format('Метод правых прямоугольников', \
                                             '{:.7}'.format(rm1), '{:.7}'.format(rm2)))
    print('-' * 90)
    print("{0:29s}|{1:^29s}|{2:^30s}".format('Метод трапеций', '{:.7}'.format(tm1), '{:.7}'.format(tm2)))
    print('-' * 90)

def main():
    try:
        a = float(input("Введите начало отрезка интегрирования: "))
        b = float(input("Введите конец отрезка интегрирования: "))
    except ValueError:
        print("Произошла проблема при вводе. Возможно, Вы ввели строку вместо числового значения.")
        print("Попробуйте ещё раз.")
        main()
    else:
        if b <= a:
            print("Конец отрезка интегрирования должен быть больше начала.")
            print("Попробуйте ещё раз.")
            main()
        else:
            try:
                N1 = int(input("Введите первое количество участков разбиения (целочисленное значение): "))
                N2 = int(input("Введите первое количество участков разбиения (целочисленное значение): "))
            except ValueError:
                print("Произошла проблема при вводе.")
                print("Возможно, Вы ввели строку вместо числового значения или вещественное значение вместо целого.")
                print("Попробуйте ещё раз.")
                main()
            else:
                rm1 = right_rectangle_method(a, b, N1)  # value of the integral by right rectangle method with the use of N1
                rm2 = right_rectangle_method(a, b, N2)  # value of the integral by right rectangle method with the use of N2
                tm1 = trapeze_method(a, b, N1)  # value of the integral by trapeze method with the use of N1
                tm2 = trapeze_method(a, b, N2)  # value of the integral by trapeze method with the use of N2

                # checking if function is defined on f given interval
                if (rm1 is None) or (rm2 is None) or (tm1 is None) or (tm2 is None) or \
                        (isinstance(rm1, complex) and (rm1.imag != 0)) or (isinstance(rm2, complex) and (rm2.imag != 0)) or \
                        (isinstance(tm1, complex) and (tm1.imag != 0)) or (isinstance(tm2, complex) and (tm2.imag != 0)):
                    print("Значение интеграла на отрезке [{0:.5}, {1:.5}] не может быть вычисленно, \n"
                          "тк на части этого отрезка функция не определена.".format(a, b))
                else:
                    absolute = F(b) - F(a)  # value of the intagral calculated with the use of primitives
                    print('\nТаблица значений интегралла, полученных с помощью разных методов.')
                    display(N1, N2, rm1, rm2, tm1, tm2)

                    print("Значение интегралла вычисленное при помощи первообразной: {0:.7}".format(absolute))
                    # calculation of absolute error
                    rm1_a = abs(absolute - rm1)
                    rm2_a = abs(absolute - rm2)
                    tm1_a = abs(absolute - tm1)
                    tm2_a = abs(absolute - tm2)
                    print('\nТаблица абсолютных погрешностей значений интегралла, полученных с помощью разных методов.')
                    display(N1, N2, rm1_a, rm2_a, tm1_a, tm2_a)

                    print('\nТаблица относительных погрешностей значений интегралла, полученных с помощью разных методов.')
                    print("Значения указаны в процентах.")
                    # output of the table with calculated relative errors
                    display(N1, N2, (abs(absolute - rm1) / absolute) * 100, (abs(absolute - rm2) / absolute) * 100, \
                            (abs(absolute - tm1) / absolute) * 100, (abs(absolute - tm2) / absolute) * 100)
                    E = input("Введите погрешность (она должна быть числовым значением): ")
                    while E is str:
                        E = input("Введите погрешность ещё раз (она должна быть числовым значением): ")
                    e = float(E)
                    # finding which method is more accurate
                    if min(rm1_a, rm2_a, tm1_a, tm2_a) == rm1 or min(rm1_a, rm2_a, tm1_a, tm2_a) == rm2:
                        print("Метод правых прямоугольников даёт более точный результат.")
                        # finding out how big N should be for this |I(N) - I(N*2)| < E to be true on less accurate method
                        cur_N = 1
                        integral1 = trapeze_method(a, b, cur_N)
                        integral2 = trapeze_method(a, b, 2 * cur_N)
                        while abs(integral2 - integral1) >= e:
                            '''print(cur_N, abs(trapeze_method(a, b, cur_N) - trapeze_method(a, b, cur_N * 2)),
                                  abs(trapeze_method(a, b, cur_N) - trapeze_method(a, b, cur_N * 2)) >= 1e-4)'''
                            cur_N *= 2
                            integral1 = integral2
                            integral2 = trapeze_method(a, b, 2 * cur_N)



                        print("Для соблюдения данного неравенства |I(N) - I(N*2)| < Ɛ \n"
                              "при использовании метода трапеций N должно быть равно {0}".format(cur_N))
                        # print(cur_N, trapeze_method(a, b, cur_N), trapeze_method(a, b, cur_N * 2), \
                        # abs(trapeze_method(a, b, cur_N) - trapeze_method(a, b, cur_N * 2)))
                    else:
                        print("Метод трапеций даёт более точный результат.")
                        # finding out how big N should be for this |I(N) - I(N*2)| < E to be true on less accurate method
                        cur_N = 1
                        integral1 = right_rectangle_method(a, b, cur_N)
                        integral2 = right_rectangle_method(a, b, 2 * cur_N)
                        while abs(integral2 - integral1) >= e:
                            '''print(cur_N, right_rectangle_method(a, b, 2 * cur_N), right_rectangle_method(a, b, cur_N), \
                                  abs(right_rectangle_method(a, b, 2 * cur_N) - right_rectangle_method(a, b, cur_N)))'''
                            cur_N *= 2
                            integral1 = integral2
                            integral2 = right_rectangle_method(a, b, 2 * cur_N)

                        print("Для соблюдения данного неравенства |I(N) - I(N*2)| < Ɛ \n"
                              "при использовании метода правых прямоугольников N должно быть равно {0}".format(cur_N))
                        # print(cur_N, right_rectangle_method(a, b, 2 * cur_N), right_rectangle_method(a, b, cur_N), \
                        # abs(right_rectangle_method(a, b, 2 * cur_N) - right_rectangle_method(a, b, cur_N)))
main()