# Федченко Анастасия ИУ7-15Б
# Лабораторная работа №12
# Текстовый процессор

# print(180*'*')
def max_len_str(arr):  # определение самой длинной строки в массиве
    max_len = 0
    for i in range(len(arr)):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])
    return max_len


def output(arr):  # вывод
    print("\nРезультат:")
    for i in range(len(arr)):
        print(arr[i])
    print()


def removing_insignificant_spaces(arr, current_mode):
    # удаление левых незначащих пробелов
    if current_mode == 2:
        for i in range(len(arr)):
            count_spaces = 0
            s = str(arr[i])
            for j in range(len(s)):
                if s[j] == ' ':
                    count_spaces += 1
                else:
                    break
            arr[i] = s[count_spaces:len(s)]
    # удаление правых незначащих пробелов
    '''for i in range(len(arr)):
        count_spaces = 0
        for j in range(len(arr[i]) - 1, -1, -1):
            if arr[i][j] == ' ':
                count_spaces += 1
            else:
                break
        arr[i] = arr[i][0:(len(arr[i]) - count_spaces)]'''
    # удаление средних незначащих пробелов
    if current_mode == 3:
        for i in range(len(arr)):
            while '  ' in arr[i]:
                arr[i] = arr[i].replace('  ', ' ')


def first(arr, current_mode):  # выравнивание по левому краю
    removing_insignificant_spaces(arr, current_mode)

    output(arr)


def second(arr, current_mode):  # выравнивание по правому краю
    removing_insignificant_spaces(arr, current_mode)
    for i in range(len(arr)):
        arr[i] = ' ' * (max_len_str(arr) - len(arr[i])) + arr[i]

    output(arr)


def third(arr, current_mode):  # Выравнивание текста по ширине
    removing_insignificant_spaces(arr, current_mode)
    max_len = max_len_str(arr)
    for i in range(len(arr) - 1):
        spaces_for_spaces = arr[i].count(' ')
        if spaces_for_spaces == 0:
            arr[i] = ((max_len - len(arr[i])) // 2) * ' ' + arr[i] + ((max_len - len(arr[i])) // 2) * ' '
        # по сколько можно равно вставить пробелов между словами
        else:
            equal_spaces = (max_len - (len(arr[i]) - spaces_for_spaces)) // spaces_for_spaces
            s = str(' ' * equal_spaces)
            arr[i] = arr[i].replace(' ', s)
            # сколько осталось вставить после замены пробелов на максимальное количество равных
            n = (max_len - (len(arr[i]) - spaces_for_spaces)) % spaces_for_spaces
            arr[i] = arr[i].replace(s, str(s + ' '), n)

    output(arr)


def forth(arr, current_mode, word):  # Удаление всех вхождений заданного слова.
    # слово как лексическая единица, то есть по сторонам должны быть либо пробелы, либо знаки препинания
    # дописать вариант двух знаков препинания по бокам
    char = [' ', ',', '.', ';', ':', '...', '?', '!', '—', '(', ')', '"']
    count = 0
    for i in range(len(arr)):
        for c1 in char:
            # если с двух сторон есть пробелы или знаки препинания
            for c2 in char:
                w = c1 + word + c2
                while arr[i].count(w) > 0:
                    count += 1
                    arr[i] = arr[i].replace(w, str(c1 + c2))
            # если слово в начале строки
            w = word + c1
            if arr[i][0:len(w)] == w:
                count += 1
                arr[i] = arr[i][len(w):len(arr[i])]
            # если слово в конце строки
            w = c1 + word
            if arr[i][len(arr[i]) - len(w): len(arr[i])] == w:
                count += 1
                arr[i] = arr[i][len(arr[i]) - len(w): len(arr[i])]
    if count == 0:
        print("Не обнаружено ни одного вхождения заданного слова.")
    else:
        '''if current_mode == 1:
            first(arr, current_mode)
        elif current_mode == 2:
            second(arr, current_mode)
        elif current_mode == 3:
            third(arr, current_mode)'''
        output(arr)


def fifth(arr, current_mode, old_word, new_word):  # Замена одного слова другим во всём тексте.
    char = [' ', ',', '.', ';', ':', '...', '?', '!', '—', '(', ')', '"']
    count = 0
    for i in range(len(arr)):
        for c1 in char:
            # если с двух сторон есть пробел или знаки препинания
            for c2 in char:
                w = c1 + old_word + c2
                while arr[i].count(w) > 0:
                    count += 1
                    arr[i] = arr[i].replace(w, str(c1 + new_word + c2))
            # если слово в начале строки
            w = old_word + c1
            if arr[i][0:len(w)] == w:
                count += 1
                arr[i] = new_word + c1 + arr[i][len(w):len(arr[i])]
            # если слово в конце строки
            w = c1 + old_word
            if arr[i][len(arr[i]) - len(w): len(arr[i])] == w:
                count += 1
                arr[i] = arr[i][len(arr[i]) - len(w): len(arr[i])] + c1 + new_word
    if count == 0:
        print("Не обнаружено ни одного вхождения заданного слова.")
    else:
        # сделать проверку на то, если новое слово длиннее или короче старого
        # и если надо вызвать или second, или third
        '''if current_mode == 1:
            first(arr, current_mode)
        elif current_mode == 2:
            second(arr, current_mode)
        elif current_mode == 3:
            third(arr, current_mode)'''
        output(arr)


def is_arithmetic_expression(s):  # проверка является ли первая строка арифметическим выражением
    flag_fd = False  # flag first digit
    flag_sign = False  # flag for sign
    flag_sd = False  # flag second digit
    for i in range(len(s)):
        if s[i].isdigit() and not flag_fd:
            flag_fd = True
        if (s[i] == '+' or s[i] == '-') and flag_fd:
            flag_sign = True
        elif s[i].isdigit() and flag_fd == True and flag_sign == True:
            flag_sd = True
        if flag_fd and flag_sign and flag_sd:
            return True
    return False


def calculation(s):
    # работа со знаками
    '''for el1 in ['+', '-']:
        for el2 in ['+', '-']:
            if el1 == el2:
                while str(el1+el2) in s:
                    s = s.replace(str(el1+el2), '+')
            else:
                while str(el1 + el2) in s:
                    s = s.replace(str(el1 + el2), '-')'''
    i = 1
    while i < len(s):
        if s[i] == '+':
            if s[i - 1] == '+':
                s = s.replace("++", "+")
                i -= 1
            if s[i - 1] == '-':
                s = s.replace("-+", "-")
                i -= 1
        elif s[i] == '-':
            if s[i - 1] == '+':
                s = s.replace("+-", "-")
                i -= 1
            if s[i - 1] == '-':
                s = s.replace("--", "+")
                i -= 1
        i += 1
    r = []  # массив, куда будем записывать все числа в вычислениях вместе со знаками, после чего просто сложим их
    cur = ''  # строка для отмерения чисел со знаками
    for j in range(len(s)):
        cur += s[j]
        if s[j].isdigit() and ((j + 1) < len(s) and (s[j + 1] == '+' or s[j + 1] == '-')):
            r.append(cur)
            cur = ''
    r.append(cur)
    res = 0
    for j in range(len(r)):  # сложение
        res += int(r[j])
    return res


def sixth(arr, current_mode):  # Сложение и вычитание арифметических выражений над целыми числами внутри текста
    changes = 0
    for i in range(len(arr)):
        # формирование массива с предположителными арифметическими выражениями
        a = ''  # переменная для отмерения одного предположительного арифметического выражения
        a_list = []  # массив со всеми предположителными арифметическими выражениями
        sf_list = []  # массив со всеми началами и концами предположительных арифметических выражений
        start = False  # флаг идёт ли сейчас арифметическое выражение или нет
        sj = None  # начало нынешнего
        fj = None  # конец нынешнего
        for j in range(len(arr[i])):
            if arr[i][j].isdigit() or arr[i][j] == '+' or arr[i][j] == '-':  # если знак или число
                if start == False:
                    start = True
                    sj = j
                    fj = j
                else:
                    fj += 1
                a += arr[i][j]
            elif arr[i][j] == ' ':  # если пробел
                # если пробел между цифрами
                if j > 0 and arr[i][j - 1].isdigit():
                    d = False  # следующее значимое цифра или нет
                    for t in range(j, len(arr[i])):
                        if arr[i][t].isdigit():
                            d = True
                            break
                        if not (arr[i][t].isdigit() or arr[i][t] == ' '):
                            d = False
                            break
                    if d:  # если следующее цифра, то нынешнее арифметическое выражение считаем законченным
                        a_list.append(a)
                        sf_list.append([sj, fj])
                        a = ''
                        start = False
                        sj = None
                        fj = None
                    else:  # если следующее не цифра, движимся дальше
                        a += arr[i][j]
                        fj += 1
                elif start == True:  # если предыдущее не цифра
                    fj += 1
                    a += arr[i][j]
                # fj+=1
            else:  # если не цифра, не пробел и не знак
                if start:
                    a_list.append(a)
                    sf_list.append([sj, fj])
                    a = ''
                    start = False
                    sj = None
                    fj = None
        if start:
            a_list.append(a)
            sf_list.append([sj, fj])

        '''if len(a_list) > 0:
            print(a_list)
            print(sf_list)'''
        # проверка, отсеивание и чистка арифметических выражений
        for k in range(len(a_list)):
            copy = a_list[k].replace(' ', '')
            if is_arithmetic_expression(copy):  # если предположительное арифм выражение всё-таки является им
                changes += 1
                # a_list[k] = calculation(a_list[k])
                # print(calculation(a_list[k]))
                res = str(calculation(copy))  # вычисление
                if a_list[k][len(a_list[k]) - 1] == ' ':  # если в изначалдьной версии в конце был пробел
                    res += ' '
                for l in range(k + 1, len(sf_list)):  # двигаем индексы начала и конца других
                    sf_list[l][0] -= (len(a_list[k]) - len(res))
                    sf_list[l][1] -= (len(a_list[k]) - len(res))
                    # print(sf_list)
                arr[i] = arr[i][0:sf_list[k][0]] + res + arr[i][(sf_list[k][1] + 1):len(arr[i])]
    if changes == 0:
        print("Арифметических выражений не обнаружено.")
    else:
        '''if current_mode == 1:
            first(arr, current_mode)
        elif current_mode == 2:
            second(arr, current_mode)
        elif current_mode == 3:
            third(arr, current_mode)'''
        output(arr)


def is_a_word(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
    return False


def seventh(arr, current_mode):  # Найти и затем удалить самое короткое по количеству слов предложение
    min_s = None
    min_f = None
    min_amount_words = None
    cur_s = [0, 0]
    cur_f = [0, 0]
    min_sentence = ''
    cur_sentence = ''
    flag = False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not(arr[i][j] == '.' or arr[i][j] == '!' or arr[i][j] == '?'):
                if not flag:
                    flag = True
                    cur_s = [i, j]
                cur_f = [i, j]
                cur_sentence += arr[i][j]
            else:
                cur_f = [i, j]
                cur_sentence += arr[i][j]
                flag = False
                words = cur_sentence.split(' ')
                count = 0
                for t in range(len(words)):
                    if is_a_word(words[t]):
                        count += 1
                # print('cur', cur_s, cur_f, count)
                # print(words)
                if min_amount_words is None or min_amount_words > count and not (count == 0):
                    min_amount_words = count
                    min_s = cur_s
                    min_f = cur_f
                    min_sentence = cur_sentence
                    # print(min_amount_words, min_s, min_f)
                    # print(words)
                cur_s = None
                cur_f = None
                cur_sentence = ''
        cur_sentence += ' '
    if min_amount_words is None:
        print("\nБольше предложений в тексте нет.\n")
        return
    elif min_amount_words is None or min_amount_words > count and not (count == 0):
        min_amount_words = count
        min_s = cur_s
        min_f = cur_f
    #print(min_amount_words, min_s, min_f)
    # удаление предложения
    if min_s[0] == min_f[0]:
        arr[min_s[0]] = arr[min_s[0]][0:min_s[1]] + arr[min_s[0]][(min_f[1] + 1): len(arr[min_s[0]])]
    else:
        arr[min_s[0]] = arr[min_s[0]][0:min_s[1]]
        min_s[0] += 1
        while min_s[0] != min_f[0]:
            arr[min_s[0]] = ''
            min_s[0] += 1
        arr[min_f[0]] = arr[min_f[0]][(min_f[1] + 1):len(arr[min_f[0]])]

    '''if current_mode == 1:
        first(arr, current_mode)
    elif current_mode == 2:
        second(arr, current_mode)
    elif current_mode == 3:
        third(arr, current_mode)'''
    print("\nМинимальное по количеству слов предлжение:")
    print(min_sentence + '\n')
    output(arr)


# f = open('Text Document.txt', encoding='utf-8')
arr = ['Она                     доверчиво и без страха поглядывала',
       'на него и слегка махала хвостиком! Он отвернулся, зажмурился и разжал руки. Герасим ничего не слыхал, ни быстрого визга',
       'падающей Муму, ни тяжкого всплеска воды; для него самый шумный день',
       'and exit',
       's',
       'был безмолвен и беззвучен, как ни одна самая тихая ночь не беззвучна для нас,',
       '-7 -8 и когда он снова раскрыл глаза, по-прежнему - --415  + 5 -    6  8 - 4спешили по реке, как бы ++3+2 гоняясь друг за дружкой, маленькие волны,',
       'по-прежнему поплескивали они о бока лодки, и только далеко назади к берегу 9-3',
       'разбегались какие-то широкие круги. Ерошка, как только Герасим скрылся у него из виду, вернулся домой и донес',
       'всё, что видел. — Ну, да, — заметил Степан, — он ее',
       'утопит. Уж можно быть спокойным. Коли он что',
       'обещал.В --8+-9 течение (дня) никто не видел Герасима. Он дома не обедал Настал вечер; собрались к',
       'ужину , кроме .']

current_mode = 1  # показывает, как в текущий момент должен быть выровнен текст по дэфолту 1 (по левому)
new_mode = 1
working = True
while working:
    while ValueError or AssertionError:
        try:
            print("Список команд:")

            print("1. Выровнять текст по левому краю.\n"
                  "2. Выровнять текст по правому краю.\n"
                  "3. Выровнять текст по ширине.\n"
                  "4. Удаление всех вхождений заданного слова.\n"
                  "5. Замена одного слова другим во всём тексте.\n"
                  "6. Вычисление арифметических выражений над целыми числами внутри текста (сложение и вычитание).\n"
                  "7. Найти (вывести на экран) и затем удалить самое короткое по количеству слов предложение.\n"
                  "8. Завершение работы программы.\n")
            print("Выберите номер команды для выполнения (ввыести целое число):", end=' ')
            N = int(input())
            assert N >= 1 and N <= 8
        except ValueError:
            print("Возникла проблема при вводе номера команды.")
            print("Убедитесь, что входными данными является одно целое число.")
        except AssertionError:
            print("Возникла проблема при вводе номера команды.")
            print("Убедитесь, что вводится номер одной из существующих команд в промсежутке от 1 до 8.")
        else:
            break
    if N == 1:
        first(arr, current_mode)
        current_mode = 1
    elif N == 2:
        second(arr, current_mode)
        current_mode = 2
    elif N == 3:
        third(arr, current_mode)
        current_mode = 3
    elif N == 4:
        print("Задайте слово для удаления:", end=' ')
        word = input()
        forth(arr, current_mode, word)
    elif N == 5:
        print("Задайте слово, которое надо заменить:", end=' ')
        old_word = input()
        print("Задайте слово, НА которое надо заменить:", end=' ')
        new_word = input()
        fifth(arr, current_mode, old_word, new_word)
    elif N == 6:
        sixth(arr, current_mode)
    elif N == 7:
        seventh(arr, current_mode)
    else:
        working = False

print("Работа завершена.")
