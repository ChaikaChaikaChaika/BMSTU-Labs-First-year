# Федченко Анастасия ИУ7-15Б
# защита 12
# найти предложение содержащее слово с наибольшим количеством гласных латинских букв
def counting_vowels(s):
       vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
       res = 0
       for v in vowels:
              res+= s.count(v)
       return res

arr = ['jngjtb jnughuoir ;jyp9ub6p84y6 h kjyhu. rtuh etiu',
       'druht. rh4u gj. srk jo r;j tyokto aoii iiIue! kjtn ',
       'kgjuh jrhnggtf ituhygrgyg drtj5iu4g. ijtuigk ikrhyg jth jth w85. pouh rkk kliejertoo oooIU',
       'jnjhj po kkiqa oiueAa? ds;ldgjw glmhkei',
       'jhtuh4 kjrv imkim nte b6.   po68 kyUhAAPIIi        oij7jibn   5o7gb.']

max_vowel = 0
#max_vowel_word = ''
max_vowel_sentence = ''
cur_sentence = ''

for i in range(len(arr)):
       for j in range(len(arr[i])):
              if not(arr[i][j] == '.' or arr[i][j] == '!' or arr[i][j] == '?'):
                     cur_sentence+=arr[i][j]
              else:
                     cur_sentence+=arr[i][j]
                     words = cur_sentence.split(' ')
                     for word in words:
                            if counting_vowels(word)>max_vowel:
                                   max_vowel = counting_vowels(word)
                                   max_vowel_sentence = cur_sentence
                     cur_sentence = ''
       cur_sentence+=' '
print("Предложение, содержащее слово с наибольшим количеством гласных латинских букв: ")
print(max_vowel_sentence)