
first_sentence = input('Enter first sentence: ')
second_sentence = input('Enter second sentens: ')


new_list = []
if first_sentence.count('!') > second_sentence.count('?'):
    new_list.append(first_sentence)
    new_list.append(second_sentence)
    for f_list in new_list:
        print(f_list, end = '')

if first_sentence.count('!') < second_sentence.count('?'):
    new_list.append(second_sentence)
    new_list.append(first_sentence)
    for s_list in new_list:
        print(s_list, end = '')

if first_sentence.count('!') == second_sentence.count('?'):
    print('Ой!')







