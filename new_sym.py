word = input('Введиет слово: ')

replace_num = int(input('Введите номер символа для замены: '))
new_symbol = input('Введите символ: ')

new_word = list(word)

new_word[replace_num - 1] = new_symbol

for i in new_word:
    print(i, end = '')








#new_word = ' '

#count = 0
#for sym in word:
 #   count += 1
  #  if count != replace_num:
   #     new_word += sym
    #else:
     #   new_word += new_symbol

