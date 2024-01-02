# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# list = [i for i in range(a, b + 1) if i % 2 == 0]
# print(list)
#
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_prices = [(i_price if i_price > 0 else 0)
#                    for i_price in original_prices]
# print(new_prices)


import random

team_1 = [random.randint(50, 80) for _ in range(10)]
team_2 = [random.randint(30, 60) for _ in range(10)]
team_3 = [('Убит' if team_1[i_damage] + team_2[i_damage] > 100
           else 'Выжил')
          for i_damage in range(10)]

print('Урон первого отряда: ', team_1)
print('Урон второго отряда: ', team_2)
print('Состояние третьего отряда: ', team_3)
