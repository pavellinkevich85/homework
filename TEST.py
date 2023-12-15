
list = [1, 2, 4, 7, -10 , 89, -100]
new_list = ['Mama', 'Papa']

new_list.extend(list)
print(new_list)

new_list.insert(4, 'vip')
print(new_list)

which = input('which word you want?: ')
index = new_list.index(4)
new_list.insert(index, '4')

print(index + 1)
for i in range(5):
    new_list.append(-10)

print(new_list.count(-10))