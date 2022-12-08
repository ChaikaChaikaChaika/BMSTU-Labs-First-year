# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №13
# База данных в текстовом файле
import re


def is_file_ok(path):  # проверка базы данных на мсоответствие структуре
    it_is_ok = True
    file = open(path, 'r')
    for line in file:
        arr = line.rstrip('\n').split(';')
        if arr[len(arr) - 1] == '':
            arr.pop(len(arr) - 1)
        if len(arr) == 5:
            # проверка полей на соответствие структуре бд
            if (re.match('^[0-9 ]+$', arr[0]) is None) or (re.match('^[a-zA-Zа-яА-Я., ]+$', arr[2]) is None) or \
                    (re.match('^[0-9 ]+$', arr[3]) is None) or (re.match('^[0-9. ]+$', arr[4]) is None):
                it_is_ok = False
                # print(line, (re.match("^[0-9 ]+$", arr[0]) is None), (re.match("^[a-zA-Zа-яА-Я., ]+$", arr[2]) is None), \
                # (re.match("^[0-9 ]+$", arr[3]) is None), (re.match("^[0-9. ]+$", arr[4])))
        else:
            if line != '':
                it_is_ok = False
                # print(line)
    return it_is_ok


def first():  # Выбрать файл для работы
    while IOError:
        try:
            print("Введите путь до файла (должен заканчиваться на '.txt'):", end=' ')
            path = input()
            if path == "exit":
                return None
            if path[len(path) - 4: len(path)] != ".txt":
                raise IOError
            else:
                f = open(path)
        except IOError:
            path = path.rstrip(' ')
            if path[len(path) - 4: len(path)] != ".txt":
                print("Возникли проблемы с нахождением файла.")
                print("Путь до файла должен заканчиваться на '[имя файла].txt' .\n")
            else:
                print("Такого файла не существует.\n")
        else:
            f.close()
            break
    if is_file_ok(path):
        print("Файл для работы успешно выбран.")
        return path
    else:
        print("\nФайл не соответствует формату. Укажите другой.\n")
        return first()


def input_line(id):  # ввод одной строки бд
    s = str(id) + ";"
    name = None
    while name is None:
        print("Введите название фильма: ", end='')
        name = input()
        if ";" in name or '\n' in name:
            print("Поля базы данных не могу содержать ';' и знак переноса строки.")
            name = None
    s += name + ';'

    director = None
    while director is None:
        print("Введите имя режисёра: ", end='')
        director = input()
        if ";" in director or '\n' in name:
            print("Поля базы данных не могу содержать ';' и знак переноса строки.")
            director = None
        elif re.match("^[a-zA-Zа-яА-Я., ]+$", director) is None:
            print("Данное поле базы данных может содержать только буквы и '.' c ','.")
            director = None
    s += director + ";"

    year_of_release = None
    while ValueError or AssertionError:
        try:
            print("Введите год выпуска: ", end='')
            year_of_release = int(input())
            assert year_of_release > 0 and year_of_release <= 2022
        except ValueError:
            print("Данное поле базы данных может содержать только числа.")
        except AssertionError:
            print("Вводимое значение должно быть больше 0 и не превышать 2022.")
        else:
            break
    s += str(year_of_release) + ";"

    rating = None
    while ValueError or AssertionError:
        try:
            print("Введите оценку этого фильма (от 0.0 до 10.0): ", end='')
            rating = float(input().replace(',', '.'))
            assert rating >= 0.0 and rating <= 10.0
        except ValueError:
            print("Данное поле базы данных может содержать только числа.")
        except AssertionError:
            print("Вводимое значение должно быть больше или равно 0 и не превышать 10.")
        else:
            break
    s += str(rating) + ";"

    return s


def second():  # Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)
    while IOError:
        try:
            print("Введите путь до файла, в который будет записана новая база данных "
                  "(должно заканчиваться на '[имя файла].txt': ", end='')
            new_path = input()
            if new_path == "exit":
                return None
            new_path = new_path.rstrip(' ')
            a = new_path.split('.')
            if a[len(a) - 1] != "txt":
                raise IOError
            else:
                cur_path = new_path
                cur_file = open(cur_path, 'w')

        except IOError:
            if a[len(a) - 1] != "txt":
                print("Возникли проблемы при создании файла.")
                print("Путь до файла должен заканчиваться на '[имя файла].txt' .\n")
            else:
                print("Возникли проблемы при создании файла.")
                print("Попробуйте ввести другой путь.\n")
        else:
            break
    while ValueError:
        try:
            print("Введите количество записей, которое будет в новой базе (целое число): ", end='')
            n = int(input())
        except ValueError:
            print("Возникла проблема при вводе.")
            print("Количество записей должно быть выражено целым числом.")
        else:
            break

    for i in range(n):
        print("Заполнение строки №{0}:".format(i + 1))
        cur_file.write(input_line(i) + "\n")

    cur_file.close()

    return cur_path


def third(path):  # вывод бд
    was_anything_shown = False
    f = open(path, 'r')
    # print(s)
    for line in f:
        a = line.split(';')
        # print(a)
        if line != '':
            if not was_anything_shown:
                was_anything_shown = True
                print('-' * 80)
                print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format('id', 'Название', 'Режисёр',
                                                                          'Год выпуска', 'Оценка'))
            print('-' * 80)
            print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format(a[0], a[1], a[2], a[3], a[4]))
    f.close()
    if not was_anything_shown:
        print("Файл пуст или содержит невалидные данные.")


def fifth(path):  # поиск по оценке
    while ValueError or AssertionError:
        try:
            print("Введите минимальную подходящую оцеку (вещественное число): ", end='')
            rate = float(input())
            assert (10 - rate) > 1e-6 and (rate - 0) > 1e-6
        except ValueError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входными данными является одно вещественное число.")
        except AssertionError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входные данные больше нуля и меньше единицы.")
        else:
            break

    was_anything_shown = False
    f = open(path, 'r+')

    for line in f:
        a = line.split(';')
        # print(a)
        if line != '':
            if (float(a[4]) - rate) >= 0:
                if not was_anything_shown:
                    was_anything_shown = True
                    print('-' * 80)
                    print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format('id', 'Название', 'Режисёр',
                                                                              'Год выпуска', 'Оценка'))
                print('-' * 80)
                print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format(a[0], a[1], a[2], a[3], a[4]))
    f.close()
    if not was_anything_shown:
        print("\nВ базе данных нет подходящих элементов.\n")


def sixth(path):  # поиск по году и оценке
    while ValueError or AssertionError:
        try:
            print("Введите минимальную подходящую оцеку (вещественное число): ", end='')
            rate = float(input())
            assert (10 - rate) > 1e-6 and (rate - 0) > 1e-6
        except ValueError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входными данными является одно вещественное число.")
        except AssertionError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входные данные больше нуля и меньше единицы.")
        else:
            break
    while ValueError or AssertionError:
        try:
            print("Введите минимальный подходящий год выпуска (целое число): ", end='')
            year = float(input())
            assert year > 0 and year <= 2022
        except ValueError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входными данными является одно целое число.")
        except AssertionError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входные данные больше нуля и меньше 2022.")
        else:
            break

    was_anything_shown = False
    f = open(path, 'r')

    for line in f:
        a = line.split(';')
        # print(a)
        if line != '':
            if (float(a[4]) - rate) >= 0 and year <= int(a[3]):
                if not was_anything_shown:
                    was_anything_shown = True
                    print('-' * 80)
                    print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format('id', 'Название', 'Режисёр',
                                                                              'Год выпуска', 'Оценка'))
                print('-' * 80)
                print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format(a[0], a[1], a[2], a[3], a[4]))
    f.close()
    if not was_anything_shown:
        print("\nВ базе данных нет подходящих элементов.\n")


# print(re.match("^[0-9а-яА-Я. ]+$", "Д.Кэмерон") is not None)
cur_path = None
cur_file = None
working = True
while working:
    while ValueError or AssertionError:
        try:
            print("Список команд:")

            print("1. Выбрать файл для работы.\n"
                  "2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями).\n"
                  "3. Вывести содержимое базы данных.\n"
                  "4. Добавить запись в конец базы данных.\n"
                  "5. Поиск по оценке.\n"
                  "6. Поиск по году выпуска и оценке.\n"
                  "7. Завершение работы программы.\n")
            print("Выберите номер команды для выполнения (ввыести целое число):", end=' ')
            N = int(input())
            assert N > 0 and N <= 7
        except ValueError:
            print("Возникла проблема при вводе номера команды.")
            print("Убедитесь, что входными данными является одно целое число.")
        except AssertionError:
            print("Возникла проблема при вводе номера команды.")
            print("Убедитесь, что вводится номер одной из существующих команд в промсежутке от 1 до 7.")
        else:
            break
    if N == 1:  # выбор файла для работы
        cur_path = first()
    elif N == 2:  # инициализация бд
        cur_path = second()
    elif N == 3:  # вывод содержимого бд
        if cur_path is None:
            cur_path = first()
        third(cur_path)
    elif N == 4:  # добавить запись в конец бд
        if cur_path is None:
            cur_path = first()
        if cur_path is  not None:
            cur_file = open(cur_path, 'r')
            res = None
            for line in cur_file:
                if line != '':
                    a = line.split(';')
                    if re.match('^[0-9]+$', a[0]):
                        res = int(a[0])
                        res += 1

            '''arr = cur_file.readlines()
            t = len(arr) - 1
            
            while t != 0:
                i = arr[t].split(';')
                if re.match("^[0-9]+$", i[0]):
                    res = int(i[0])
                    res += 1
                    break
                t -= 1'''
            if res is None:
                res = 0
            cur_file.close()
            cur_file = open(cur_path, 'a')
            #cur_file.seek(0, 2)
            cur_file.write(input_line(res) + '\n')
            cur_file.close()
    elif N == 5:  # поиск по оценке
        if cur_path is None:
            cur_path = first()
        fifth(cur_path)
    elif N == 6:  # поиск по оценке и году выпуска
        if cur_path is None:
            cur_path = first()
        sixth(cur_path)
    elif N == 7:  # завершение работы
        working = False
        if cur_file != None:
            cur_file.close()

print("Работа завершена.")
