# list = []
# for i in range(10):
#     list.append(i ** 2)
# print(list)

# list = [i * 2 for i in 'abc' ]
# print(list)
#
# list = [i ** 2 for i in range(1, 10 + 1)]
# print(list)
#
# list = [i ** 3 for i in range(10, -1, -1)]
# print(list)
#
# prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]


N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", K, "человек.")
people = list(range(1, N+1))
out = 0

for i in range(N-1):
    print('Текущий круг людей', people)
    start_count = out % len(people)
    out = (start_count + K - 1) % len(people)
    print('Начало счёта с номера', people[start_count])
    print('Выбывает человек под номером', people[out])
    people.remove(people[out])
    print()

print('Остался человек под номером', people[0])



