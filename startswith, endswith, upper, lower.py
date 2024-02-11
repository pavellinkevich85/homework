# user_name = input('Введите имя пользователя: ')
# new_file = input('Введите имя файла: ')
#
# way = 'D:/{0}/folder/data/{1}'.format(
#     user_name,
#     new_file)
# if not way.endswith('.txt'):
#     print('Ошибка: неверно указан диск.')
# elif not way.startswith('C:/'):
#     print('Ошибка: неверно указан диск.')
# else:
#     print('Путь к файлу: ', way)

# mama = input('Введите диск: ')
# papa = input('Введите расширение: ')
#
# text = '{0}:/user/docs/folder/new_file{1}'.format(mama, papa)
#
# if not text.endswith('.txt'):
#     print('Ошибка! ')
# elif not text.startswith('C:/'):
#     print('Ошибочка!')
# else:
#     print('Хорошечно!')


# line = input('Введите строку: ')
#
# upper = len([letter for letter in line if letter.isupper()])
# lower = len([letter for letter in line if letter.islower()])
#
# if upper > lower:
#     print(line.upper())
# else:
#     print(line.lower())

details_num = 500000000
price = 23.8589578
increase = 0.045678

print('На складе {:,d} деталей'.format(details_num))
print('Каждая деталь стоит {:.2f} рублей'.format(price))
print('Цена увеличилась на {:.2%} процентов'.format(increase))
print('На складе {:.0e} деталей'.format(details_num))

