# user_name = input('Введите имя пользователя: ')
# new_file = input('Введите имя файла: ')
# way = 'C:/{user}/folder/data/{file}.txt'.format(
#     user=user_name,
#     file=new_file)
# way2 = 'C:/{0}/folder/{0}/data/{1}.txt'.format(
#     user_name,
#     new_file)
# way3 = f'C:/{user_name}/folder/data/{new_file}.txt'
# print(way)
# print(way2)
# print(way3)


# while True:
#     grates_taples = input('Введите шаблон поздравления, '
#                           'в шаблоне использовать конструкцию {name}: ')
#     if '{name}' in grates_taples:
#         break
#     print('Ошибка ввода, отсутсвует конструкция {name}.')
# print('Введите список имен (заканчивается на end): ')
# name_list = []
# while True:
#     name = input('Имя: ')
#     if name != 'end':
#         name_list.append(name)
#     else:
#         break
# for i_names in name_list:
#     print(grates_taples.format(name=i_names))

# name = input('Имя получателя заказа: ')
# number = int(input('Введите номер заказа: '))
# list = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(name, number)
# print(list)

# name = input('Имя должника: ')
# number = int(input('Размер долга : '))
# list = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!'.format(name, number)
# print(list)

# import random
#
# num = random.randint(1, 255)
# num1 = random.randint(1, 255)
# num2 = random.randint(1, 255)
# num3 = random.randint(1, 255)
#
# ip_address = f'{num}.{num1}.{num2}.{num3}'
# print(ip_address)

while True:
    grates_taples = input('Введите шаблон поздравления, '
                          'в шаблоне использовать конструкцию {name}: ')
    if '{name}' in grates_taples:
        break
    print('Ошибка ввода, отсутсвует конструкция {name}.')

name_list = input('Список людей через запятую ').split(', ')


for i_names in name_list:
    print(grates_taples.format(name=i_names))