
list_words = [] # список слов

for i in range(3):
    print('Введите ', i + 1, 'слово из текста: ', end = ' ')
    word = input() # здесь запрос на слово! и оно вставляется выше где ЭНД = ''
    list_words.append(word) # ормируется список слов. Эта процедура идет 3 раза
print(list_words) # список из 3х слов

count = [0, 0, 0]  # список кол-ва слов
text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if list_words[index] == text:
            count[index] += 1

    text = input('Слово из текста: ')
print('\nПодсчёт слов в тексте')
for i in range(3):
    print(list_words[i], ':', count[i])