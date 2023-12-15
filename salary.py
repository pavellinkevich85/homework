list_salarys = []

count_employee = int(input('Уол-во сотрудников: '))
rest_empl = 0
for empl in range(count_employee):
    print('Зарплата', empl + 1, 'сотрудника', end = ' ')
    salary = int(input())
    if salary > 0:
        list_salarys.append(salary)
        rest_empl += 1
print('Зарплаты: ', list_salarys)
print('Осталось сотрудников', rest_empl)

max_sal = max(list_salarys)
print('Максимальная зарплата: ', max_sal)

min_sal = min(list_salarys)
print('Минимальная зарплата: ', min_sal)