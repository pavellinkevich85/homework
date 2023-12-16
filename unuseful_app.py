
first_sentence = input('Enter first sentence: ')
second_sentence = input('Enter second sentens: ')


new_list = []

if first_sentence.count('!') > second_sentence.count('?'):
    new_list.extend([first_sentence, second_sentence])
    for i_first in new_list:
        print(i_first, end = '')

if first_sentence.count('!') < second_sentence.count('?'):
    new_list.extend([second_sentence, first_sentence])
    for i_second in new_list:
        print(i_second, end = '')
else:
    print('OK!!!')


#print(new_list)







