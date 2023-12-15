lang = ['Phyton', 'Java', 'JS', 'SQL']
users_lang = input('После какого элемента вставить?: ')
i_index = lang.index(users_lang)

lang.insert(i_index + 1, 'C++')
print(lang)



# lang = ['Phyton', 'Java', 'JS', 'SQL']
# users_lang = int(input('На какое место вставить объект?: '))
# lang.insert(users_lang - 1, 'C++')
# print(lang)


#new_langs = []
# for i_lang in range(2):
#     new_langs.append(lang[i_lang])
# new_langs.append('C++')
# for i_lang in range(2, len(lang)):
#     new_langs.append(lang[i_lang])
#prin t(new_langs)