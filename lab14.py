# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №14
# База данных в бинарном файле
import os.path
import re
import struct

format = 'i60s40sii'
step = struct.calcsize(format)


def is_file_ok(path):  # проверка файла на соответствие формату
    f = open(path, 'rb')
    it_is_ok = True
    try:
        x = f.read(step)
        while x != b'':
            struct.error(list(struct.unpack(format, x)))
            a = list(struct.unpack(format, x))

            # проверка полей на соответствие структуре бд
            if (re.match('^[0-9 ]+$', str(a[0])) is None) or \
                    (re.match('^[a-zA-Zа-яА-Я., ]+$', a[2].decode('utf-8')) is None) or \
                    (re.match('^[0-9 ]+$', str(a[3])) is None) or \
                    (re.match('^[0-9. ]+$', str(a[4])) is None) or (a[3]<0 or a[3]>2022) or \
                    (a[4]<0 or a[4]>10):
                #print(str(a[0]), a[2].decode('utf-8'), a[2].decode('utf-8'), str(a[4]))
                '''print((re.match('^[0-9 ]+$', str(a[0])) is None),
                      (re.match('^[a-zA-Zа-яА-Я., ]+$', a[2].decode('utf-8')) is None),
                      (re.match('^[0-9 ]+$', str(a[3])) is None), (re.match('^[0-9 ]+$', str(a[4])) is None))'''
                it_is_ok = False
            x = f.read(step)
            # print(line, (re.match("^[0-9 ]+$", arr[0]) is None), (re.match("^[a-zA-Zа-яА-Я., ]+$", arr[2]) is None), \
            # (re.match("^[0-9 ]+$", arr[3]) is None), (re.match("^[0-9. ]+$", arr[4])))
    except:
        return False
    else:
        return it_is_ok


def first():  # Выбрать файл для работы
    while IOError:
        try:
            print("Введите путь до файла (должен заканчиваться на '.bin') или 'menu' для возвращения к меню:", end=' ')
            path = input()
            if path == "menu":
                return None
            if path[len(path) - 4: len(path)] != ".bin":
                raise IOError
            else:
                f = open(path)
        except IOError:
            path = path.rstrip(' ')
            if path[len(path) - 4: len(path)] != ".bin":
                print("Возникли проблемы с нахождением файла.")
                print("Путь до файла должен заканчиваться на '[имя файла].bin' .\n")
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
    name = None
    while name is None:
        print("Введите название фильма: ", end='')
        name = input()
        if ";" in name or '\n' in name:
            print("Поля базы данных не могу содержать ';' и знак переноса строки.")
            name = None
        elif len(name) > 30:
            print("Это поле базы данных не должно содержать больше 30-ти элементов")
            name = None
    if len(name) < 30:
        name = name + (60 - len(name)) * ' '
    b_name = bytes(name, encoding='utf-8')

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
        elif len(director) > 20:
            print("Это поле базы данных не должно содержать больше 20-ти элементов")
            director = None

    if len(director) < 20:
        director = director + (40 - len(director)) * ' '
    b_director = bytes(director, encoding='utf-8')

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

    rating = None
    while ValueError or AssertionError:
        try:
            print("Введите оценку этого фильма (от 0 до 10): ", end='')
            rating = int(input())
            assert rating >= 0 and rating <= 10
        except ValueError:
            print("Данное поле базы данных может содержать только числа.")
        except AssertionError:
            print("Вводимое значение должно быть больше или равно 0 и не превышать 10.")
        else:
            break
    # упаковка и возврат
    return struct.pack(format, id, b_name, b_director, year_of_release, rating)


def second():  # Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями)
    while IOError:
        try:
            print("Введите путь до файла, в который будет записана новая база данных "
                  "(должно заканчиваться на '[имя файла].bin' или 'menu' для возвращения к меню: ", end='')
            new_path = input()
            if new_path == "menu":
                return None
            new_path = new_path.rstrip(' ')
            a = new_path.split('.')
            if a[len(a) - 1] != "bin":
                raise IOError
            else:
                cur_path = new_path
                cur_file = open(cur_path, 'wb')

        except IOError:
            if a[len(a) - 1] != "bin":
                print("Возникли проблемы при создании файла.")
                print("Путь до файла должен заканчиваться на '[имя файла].bin' .\n")
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
        cur_file.write(input_line(i))

    cur_file.close()

    return cur_path


def third(path):  # вывод бд
    was_anything_shown = False
    f = open(path, 'rb')
    # print(s)
    i = 0
    x = f.read(step)
    while x != b'':
        '''print('i', struct.unpack('i', f.read(4)))
        for i in range(60):
            a = struct.unpack('1s', f.read(1))
            print('1s', a[0])
        print(struct.unpack('i', f.read(4)))
        print(struct.unpack('f', f.read(4)))
        #print(len(line), line)'''
        a = list(struct.unpack(format, x))
        # print(a)
        # a = line.split(';')
        # print(a)
        if x != '':
            if not was_anything_shown:
                was_anything_shown = True
                print('-' * 86)
                print("{5:^5s}|{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format('id', 'Название', 'Режисёр',
                                                                                  'Год выпуска', 'Оценка', '№'))
            print('-' * 86)
            id = str(a[0])
            name = a[1].decode('utf-8')
            name = name.rstrip(' ')
            director = a[2].decode('utf-8')
            director = director.rstrip(' ')
            year_of_release = str(a[3])
            rating = str(a[4])
            print(
                "{5:^5s}|{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format(id, name, director, year_of_release, rating,
                                                                            str(i)))
            i += 1
        x = f.read(step)
    f.close()
    if not was_anything_shown:
        print("\nФайл пуст или содержит невалидные данные.\n")


def max_id(path):  # находждение максимального id в базе, чтобы не было повторов
    res = None
    f = open(path, 'rb')
    x = f.read(step)
    while x != b'':
        a = list(struct.unpack(format, x))
        if res is None or a[0] > res:
            res = a[0]
        x = f.read(step)
    if res is None:
        return -1
    return res


def forth(path, where, new_id, size):  # добавление
    f = open(path, 'rb+')
    f.seek(0, 0)
    for i in range(where):  # сдвиг до нужного места
        f.seek(step, 1)
    if where < size:
        cur = input_line(new_id)
        temp = f.read(step)
        f.seek(-step, 1)
        while temp != b'':  # перезапись нужного количества строк
            f.write(cur)
            cur = temp
            temp = f.read(step)
            f.seek(-step, 1)
        if cur != b'':
            f.seek(step, 1)
            f.write(cur)
    else:
        f.seek(0, 2)
        f.write(input_line(new_id))
    f.close()


def fifth(path, from_where, size):  # удаление
    f = open(path, 'rb+')
    f.seek(0, 0)
    for i in range(from_where + 1):  # сдвиг до нужного места
        f.seek(step, 1)
    cur = f.read(step)
    while cur != b'':  # перезапись нужного количества строк
        f.seek(-2*step, 1)
        #f.seek(-step, 1)
        f.write(cur)
        f.seek(step, 1)
        cur = f.read(step)
    f.truncate(step * (size - 1))  # удаление последней строки
    f.close()


def sixth(path):  # поиск по оценке
    while ValueError or AssertionError:
        try:
            print("Введите минимальную подходящую оценку (целое число): ", end='')
            rate = int(input())
            assert rate <= 10 and rate >= 0
        except ValueError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входными данными является одно целое число.")
        except AssertionError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входные данные больше нуля и меньше единицы.")
        else:
            break

    was_anything_shown = False
    f = open(path, 'rb')

    x = f.read(step)
    while x != b'':
        a = list(struct.unpack(format, x))
        # print(a)
        if x != b'':
            if int(a[4]) >= rate:
                if not was_anything_shown:
                    was_anything_shown = True
                    print('-' * 80)
                    print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format('id', 'Название', 'Режисёр',
                                                                              'Год выпуска', 'Оценка'))
                print('-' * 80)
                id = str(a[0])
                name = a[1].decode('utf-8')
                name = name.rstrip(' ')
                director = a[2].decode('utf-8')
                director = director.rstrip(' ')
                year_of_release = str(a[3])
                rating = str(a[4])
                print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format(id, name, director, year_of_release, rating))
        x = f.read(step)
    f.close()
    if not was_anything_shown:
        print("\nВ базе данных нет подходящих элементов.\n")


def seventh(path):  # поиск по оценке и году
    while ValueError or AssertionError:
        try:
            print("Введите минимальную подходящую оценку (целое число): ", end='')
            rate = int(input())
            assert rate <= 10 and rate >= 0
        except ValueError:
            print("Возникла проблема при вводе.")
            print("Убедитесь, что входными данными является одно целое число.")
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
    f = open(path, 'rb')

    x = f.read(step)
    while x != b'':
        a = list(struct.unpack(format, x))
        # print(a)
        if x != b'':
            if int(a[4]) >= rate and year <= int(a[3]):
                if not was_anything_shown:
                    was_anything_shown = True
                    print('-' * 80)
                    print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format('id', 'Название', 'Режисёр',
                                                                              'Год выпуска', 'Оценка'))
                print('-' * 80)
                id = str(a[0])
                name = a[1].decode('utf-8')
                name = name.rstrip(' ')
                director = a[2].decode('utf-8')
                director = director.rstrip(' ')
                year_of_release = str(a[3])
                rating = str(a[4])
                print("{0:^5s}|{1:^30s}|{2:^20s}|{3:^13s}|{4:^8s}".format(id, name, director, year_of_release, rating))
        x = f.read(step)
    f.close()
    if not was_anything_shown:
        print("\nВ базе данных нет подходящих элементов.\n")


'''i1 = 0
s1 = "abc\n"
sb1 = bytes(s1, encoding='utf-8')
f = open('l.bin', 'wb')
f.write(struct.pack('i4s', i1, sb1))
i2 = 1
s2 = "FG \n"
sb2 = bytes(s2, encoding='utf-8')
f.write(struct.pack('i4s', i2, sb2))
f.close()
f = open('l.bin', 'rb')
print(list(struct.unpack('i4s', f.readline())))
print(list(struct.unpack('i4s', f.readline())))'''
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
                  "4. Добавить запись в произвольное место базы данных.\n"
                  "5. Удалить произвольную запись из базы данных.\n"
                  "6. Поиск по оценке.\n"
                  "7. Поиск по оценке и году.\n"
                  "8. Завершение работы программы.\n")
            print("Выберите номер команды для выполнения (ввести целое число):", end=' ')
            N = int(input())
            assert N > 0 and N <= 8
        except ValueError:
            print("Возникла проблема при вводе номера команды.")
            print("Убедитесь, что входными данными является одно целое число.")
        except AssertionError:
            print("Возникла проблема при вводе номера команды.")
            print("Убедитесь, что вводится номер одной из существующих команд в промежутке от 1 до 8.")
        else:
            break
    if N == 1:  # выбор файла для работы
        cur_path = first()
    elif N == 2:  # инициализация бд
        cur_path = second()
    elif N == 3:  # вывод содержимого бд
        if cur_path is None:
            cur_path = first()
        if cur_path is not None:
            third(cur_path)
    elif N == 4:  # добавить запись в бд
        if cur_path is None:
            cur_path = first()
        if cur_path is not None:
            size = os.path.getsize(cur_path) // step
            while ValueError or AssertionError:
                try:
                    print("Введите позицию куда, нужно вставить поле (целое число от 0 до {0}): ".format(size), end='')
                    where = int(input())
                    assert where >= 0 and where <= size
                except ValueError:
                    print("Возникла проблема при вводе номера позиции записи.")
                    print("Убедитесь, что входными данными является одно целое число.")
                except AssertionError:
                    print("Возникла проблема при вводе номера позиции записи.")
                    print("Убедитесь, что входными данными является целое число от 0 до {0}.".format(size))
                else:
                    break
            new_id = max_id(cur_path) + 1
            forth(cur_path, where, new_id, size)
    elif N == 5:  # удалить запись из бд
        if cur_path is None:
            cur_path = first()
        if cur_path is not None:
            size = os.path.getsize(cur_path) // step
            while ValueError or AssertionError:
                try:
                    print("Введите позицию откуда, нужно удалить поле (целое число от 0 до {0}): ".format(size - 1),
                          end='')
                    where = int(input())
                    assert where >= 0 and where <= size - 1
                except ValueError:
                    print("Возникла проблема при вводе номера позиции записи.")
                    print("Убедитесь, что входными данными является одно целое число.")
                except AssertionError:
                    print("Возникла проблема при вводе номера позиции записи.")
                    print("Убедитесь, что входными данными является целое число от 0 до {0}.".format(size - 1))
                else:
                    break

            fifth(cur_path, where, size)

    elif N == 6:  # поиск по одному полю
        if cur_path is None:
            cur_path = first()
        sixth(cur_path)
    elif N == 7:  # поиск по двум полям
        if cur_path is None:
            cur_path = first()
        seventh(cur_path)
    elif N == 8:  # завершение работы
        working = False
        if cur_file != None:
            cur_file.close()

print("Работа завершена.")
