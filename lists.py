my_list = ['Taxist', 'Outdoor', 'Matrix', 'Father']
your_list = ['Lord Of The Rings', 'Hobbit', 'Harry Potter', 'Ms. Murpple']

my_list.extend(your_list)
print(my_list)

users = input('Which element you want to change?: ')
i_user = my_list.index(users)

my_list.insert(i_user + 1, 'RIP')

for i_elem in my_list:
    print(i_elem)