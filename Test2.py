# list = []
# for i in range(10):
#     list.append(i ** 2)
# print(list)
# print(sum(list))
#
# list = [i * 2 for i in 'abc']
# print(list)
#
# list = [i ** 2 for i in range(1, 10 + 1)]
# print(list)
#
# list = [i ** 3 for i in range(10, -1, -1)]
# print(list)
#
# def new_price(percent, price):
#     return round(price * (1 + percent / 100), 2)

# prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
# first_percent = int(input('Повышение на первый год: '))
# second_percent = int(input('Повышение на второй год: '))
#
# prices_first = [new_price(first_percent, i_price) for i_price in prices_now]
# prices_second = [new_price(second_percent, i_price) for i_price in prices_first]
#
#
# print(prices_second)
# print(prices_first)
# print('Сумма всех списков: ', sum(prices_now), sum(prices_first), sum(prices_second))

squares_odds = [i ** 2 for i in range(10) if i % 2 != 0]
squares_odds_triang_event = [(i ** 2 if i % 2 != 0 else i ** 3) for i in range(10)]

print(squares_odds)
print(squares_odds_triang_event)


import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3_condition = [('Погиб' if squad_1[i_damage] + squad_2[i_damage] > 100
                      else 'Выжил')
                     for i_damage in range(10)]
print('Урон первого отряда', squad_1)
print('Урон второго отряда', squad_2)
print('Состояние третьего отряд', squad_3_condition)