N = int(input('Кол-во участников: '))
members = []

num = 1
for _ in range(N // 3):
    members.append(list(range(num, num + 3)))
    num += 3
#print(members)

for i_team in members:
    for man in i_team:
        print(man, end = ' ')
    print('\n')

