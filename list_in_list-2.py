
words_list = []
counts = [['', 0], ['', 0], ['', 0]]

for i_num in range(3):
    print('Введите', i_num + 1, 'слово:', end=' ')
    word = input()
    words_list[i_num][0] = word


text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index][0] == text:
            words_list[index][1] += 1
        text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')

for index in range(3):
    print(words_list[index][0], ':', words_list[index][1])