
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print(zoo)

zoo.insert(1, 'bear')
print(zoo)

i_index = zoo.index('elephant')
zoo.remove('elephant')
print(zoo)

l_index = zoo.index('lion')
print('Лев сидит в клетке номер', l_index + 1)

m_index = zoo.index('monkey')
print('Обезьяна сидит в клетке номер', m_index + 1)