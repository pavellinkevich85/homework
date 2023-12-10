# text = []
#
# first_word = input('Введите 1-е слово: ')
# secnd_word = input('Введите 2-е слово: ')
# thert_word = input('Введите 3-е слово: ')
#
# count_word = 0
# while True:
#     word = input('Слово из текста: ')
#     count_word += 1
#     text.append(word)
#     if word == 'end':
#         break
#
# count_first_word = 0
# count_secnd_word = 0
# count_thert_word = 0
#
# for i in text:
#     if first_word == i:
#         count_first_word += 1
#     if secnd_word == i:
#         count_secnd_word += 1
#     if thert_word == i:
#         count_thert_word += 1
#
# print('Слово ', first_word, 'встречается ', count_first_word, 'раз')
# print('Слово ', secnd_word, 'встречается ', count_secnd_word, 'раз')
# print('Слово ', thert_word, 'встречается ', count_thert_word, 'раз')
# print('Слов в тексте: ', count_word)
# #print(text)

list_word = []
for i in range(3):
    print('Введите', i + 1, 'слово: ', end = '')
    word = input()
    list_word.append(word)
print(list_word)

count = [0, 0, 0]
text = input('Введите текст: ')
while text != 'end':
    for index in range(3):
        if list_word[index] == text:
            count[index] += 1
    text = input('Введите текст: ')
print(count)

for i in range(3):
    print(list_word[i], count [i] )




