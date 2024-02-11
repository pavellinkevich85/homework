# text = input('Введите текст: ')
# word_list = text.split()
# print(word_list)
#
# new_text = '---'.join(word_list)
# print(new_text)


while True:
    grates_taples = input('Введите шаблон поздравления, '
                          'в шаблоне использовать конструкцию '
                          '{name} и {age}: ')
    if '{name}' in grates_taples and '{age}' in grates_taples :
        break
    print('Ошибка ввода, отсутсвует конструкция '
          '{name} и {age}.')

name_list = input('Список людей через запятую: ').split(', ')

ages_str = input('Введите возраст через пробел: ')

ages = [int(i_number) for i_number in ages_str.split()]
for i_man in range(len(name_list)):
    print(grates_taples.format(name=name_list[i_man], age = ages[i_man]))
people = [''.join([name_list[i_man], str(ages[i_man])])
    for i_man in range(len(name_list))]
people_str = ', '.join(people)
print('\nИменинники: ', people_str)
#
#
#
# list = 'Mamas and Papas'
#
# word_list = list.split()
# print(word_list)
# print('In the sentences are', len(word_list), 'words ')

# massage = 'У       нас         пошёл                    снег    !     '
# new_massage = massage.split()
# print(new_massage)
# new_massage = ' '.join(new_massage)
# print(new_massage)


#