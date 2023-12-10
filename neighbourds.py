
S = input('Введите строку: ')
num_symb = int(input(('Номер символа: ')))
word = list(S)
before = num_symb - 1
after = num_symb + 1
count = 0
for i in word:
    count += 1
    if count == after:
        right_sym = i
        print('Символ справа: ', right_sym)
    if count == before:
        left_sym = i
        print('Символ слева: ', left_sym)

if word[before] == left_sym:
    print('Есть ровно один такой же символ.')
elif right_sym == word[after]:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет.')



