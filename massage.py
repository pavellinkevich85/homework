st = input('Введите строку: ')
more_symb = input('Ввведите дополнительный символ: ')

list_doble_sym = [i * 2 for i in st]
print(list_doble_sym)

new_doble_sym = [i + more_symb for i in list_doble_sym]
print(new_doble_sym)


