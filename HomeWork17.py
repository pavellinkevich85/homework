# Задание номер 1
# text = input('Введите текст: ')
# new_list = []
#
# new_list = [i for i in text
#             if i == 'у' or i == 'е' or i == 'ы' or i == 'а'
#             or i == 'о' or i == 'э' or i == 'я' or i == 'и' or i == 'ю']
#
# print(new_list)
# print('Длина списка: ', len(new_list))

# Задание номер 2.
# n = int(input('Введите число: '))
# list_n = [(i % 5 if i % 2 != 0 else 1) for i in range(n)]
# print(list_n)

#Задание номер 3
# import random
#
# team_1 = [round(random.uniform(5, 10), 2) for it_1 in range(1, 21)]
# team_2 = [round(random.uniform(5, 10), 2) for it_2 in range(1, 21)]
#
# won_team = [(team_2[i - 1] if team_1[i - 1] < team_2[i - 1] else team_1[i - 1])
#           for i in range(1, 21)]
#
# print('Первая команда: ', team_1)
# print('Вторая команда: ', team_2)
# print('Победители тура: ', won_team)

#Задание номер 4
# alphabet = 'abcdefg'
# print('1:', alphabet[:])
# print('2:', alphabet[::-1])
# print('3:', alphabet[::2])
# print('4:', alphabet[1::2])
# print('5:', alphabet[:1])
# print('6:', alphabet[::-7])
# print('7:', alphabet[3:4])
# print('8:', alphabet[4:])
# print('9:', alphabet[3:5])
# print('10:', alphabet[-3:-5:-1])

#Задание номер 5
# new_list = []
# line = input('Введите строку: ')
# a = line.rindex("h", 0, len(line))
# line = line[:a]
# line = line[::-1]
# b = line.rindex("h", 0, len(line))
# line = line[:b]
# print('Развёрнутая последовательность между первым и последним h:', line)

#Задание номер 6  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# needed_list = [[(i_list + 1), (i_list + 5), (i_list+ 9)] for i_list in range(4)]
# print(needed_list)

#Задание номер 7
# nice_list = \
#     [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# print('nice_list = ', nice_list)
#
# new_list = [i for i_3 in nice_list for i_2 in i_3 for i in i_2]
# print('nice_list: ', new_list)
# #
# #
# # nice_list = list(nice_list[0][0][0:3] + nice_list[0][1][0:3] + nice_list[0][2][0:3] +
# #       nice_list[1][0][0:3] + nice_list[1][1][0:3] + nice_list[1][2][0:3])
# # print('Ответ: ', nice_list)

#Задание номер 8
# def serched_list(shift, text1):
#     new_list = [(alphabet[(alphabet.index(i_text) + shift) % 33] if i_text != ' ' else ' ') for i_text in text1]
#     line = ''
#     for i_line in new_list:
#         line += i_line
#     return line
#
# alphabet = 'абвгдеежзийклмнопрстуфхцчшщъыьэюя '
# text = input('Введите сообщение: ')
# k = int(input('Введите сдвиг: '))
# cifer = serched_list(k, text)
# print('Зашифрованная строка: ', cifer)

# alfa = list(alphabet)
# text = list(text)
# list_index = [alfa.index(i_let) for i_text in text for i_let in alfa if i_let == i_text]
# #print('Индексы: ', list_index)
# new_list = []
# for i_new in range(len(list_index)):
#     if list_index[i_new] == 33:
#         new_list.append(list_index[i_new])
#     elif list_index[i_new] + k >= 33:
#         new_list.append((list_index[i_new] + k) % 33)
#     else:
#         new_list.append(list_index[i_new] + k)
# #print('Новые индексы: ', new_list)
# new_text = [alphabet[n_text] for n_text in new_list]
# #
# new_line = ' '
# for i_line in new_text:
#     new_line += i_line
# print('Зашифрованное сообщение: ', new_line)



# list_index = []
# for i_text in text:
#     for i_let in alfa:
#         if i_let == i_text:
#             index = alfa.index(i_let)
#             list_index.append(index)
#
# print(list_index)

# new_list = []
# for i_new in range(len(list_index)):
#     if list_index[i_new] == 33:
#         new_list.append(list_index[i_new])
#     elif list_index[i_new] > 33:
#         new_list.append(list_index[i_new] % 32)
#     else:
#         new_list.append(list_index[i_new] + k)
# print(new_list)

# for i_new in range(len(list_index)):
#     if list_index[i_new] == 33:
#         new_list.append(list_index[i_new])
#     elif list_index[i_new] + k >= 33:
#         new_list.append((list_index[i_new] + k) % 33)
#     else:
#         new_list.append(list_index[i_new] + k)
# print('Новые индексы: ', new_list)
