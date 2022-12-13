# Федченко Анастасия ИУ7-15Б
# защита 13
# задаётся имя файла, в котором содерждится текст по символу '.' и выходного
# записать в него предложения в обратном порядке, в которых есть хотя бы одна ','
# выходном

print('Введите имя входного файла: ', end='')
in_name = input()

cur_sentence = ''

try:
    f1 = open(in_name, 'r')
except IOError:
    print("Такого файла нет.")
else:
    print('Введите имя выходного файла: ', end='')
    out_name = input()
    f2 = open(out_name, 'w')
    for line in f1:
        for i in range(len(line)):
            if line[i] != '.':
                cur_sentence += line[i]
            else:
                if ',' in cur_sentence:
                    cur_sentence = cur_sentence.replace('\n', '')
                    a = cur_sentence.split(' ')
                    a = a[::-1]
                    res = ''
                    for j in range(len(a)):
                        if len(a[j])!= 0 and (a[j][len(a[j]) - 1] == ',' or a[j][len(a[j]) - 1] == ';'):
                            a[j] = a[j].replace(',', '')
                            a[j] = ',' + a[j]
                        res += (a[j] + ' ')
                    f2.write(res + '\n')
                cur_sentence = ''
        cur_sentence+=' '
    if ',' in cur_sentence:
        cur_sentence = cur_sentence.replace('\n', '')
        a = cur_sentence.split(' ')
        a = a[::-1]
        res = ''
        for j in range(len(a)):
            if len(a[j])!= 0 and (a[j][len(a[j]) - 1] == ',' or a[j][len(a[j]) - 1] == ';'):
                a[j] = a[j].replace(',', '')
                a[j] = ',' + a[j]
            res += (a[j] + ' ')
        f2.write(res + '\n')
    f2.close()