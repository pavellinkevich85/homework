list_numbers = []
count_numbers = int(input('Кол-во чисел в списке: '))

for _ in range(count_numbers):
    number = int(input('Введите число: '))
    list_numbers.append(number)
print(list_numbers)

new_list = []
devider = int(input('Введите делитель: '))
index = 0
sum_indexes = 0
for i in list_numbers:
    if i % devider == 0:
        new_list.append(i)
        sum_indexes += index
    index += 1

print('Сумма индексов', sum_indexes)
print(new_list)

