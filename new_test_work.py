# nice_list = \
#     [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# output2 = [i for i_3 in nice_list for i_2 in i_3 for i in i_2]
# print('Exemple: ', output2)


def ceaser(text, shifted):
    decoder = [(alphabet[(alphabet.index(i_text) + shifted) % 33]
               if i_text != ' ' else ' ')
               for i_text in text]
    new_text = ' '
    for i in decoder:
        new_text += i
    return new_text

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
erl_text = input('Введите преложение: ')
shift = int(input('Введите сдвиг: '))

cifr = ceaser(erl_text, shift)
print(cifr)