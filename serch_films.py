def list_films(movie, kino):
    for i_films in kino:
        if i_films == movie:
            return True
    return False

films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
new_list = []
while True:

    print('\nВаш текущий топ фильмов:', new_list)
    new_movie = input('Название фильма: ')
    if list_films(new_movie, films):
        command = input('Команды: добавить, удалить, вставить: ')
        if command == 'добавить':
            new_list.append(new_movie)
        if command == 'удалить':
            if list_films(new_movie,new_list):
                new_list.remove(new_movie)
            else:
                print('Фильма нет в вашем рейтинге')
        if command == 'вставить':
            index = int(input('На какое место поставить фильм? '))
            new_list.insert(index - 1, new_movie)
    else:
        print('Такого фильма нет в списке фильмов')
