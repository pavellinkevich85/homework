s = input('Введите строку: ')
new_sym = input('Введите новый символ: ')
new_word = list(s)
count = 0

print('Исправленная строка: ', end = '')
for i in new_word:
    if i == ':':
        i == new_sym
        count += 1

    print(i, end = '')

print('\nКоличество замен: ', count)


# text = input("Введите строку: ")
# letters = list(text)            # список
#
# what_replace = ":"             # что меняем!
# for_what_replace = ";"         # на что меняем?
# index = 0                # это зачем?
# replace_count = 0        # кол-во замен
#
# for i in letters:
#     if i == what_replace:
#         letters[index] = for_what_replace # индекс где меняется его значение?
#         replace_count += 1
#     index += 1
#
# print("Исправленная строка:", end=' ')
#
# for i in letters:
#     print(i, end='')
#
# print("\nКол-во замен:", replace_count)