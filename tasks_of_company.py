main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

complit_tasks = 0
not_complit_tasks = 0
main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

for i_tasks in main:
    if i_tasks == 0:
        not_complit_tasks += 1
    else:
        complit_tasks += 1

print('Общий список задач: ', main)
print('Кол-во невыполненных задач: ', not_complit_tasks)