
list = [1, 2, 4, 7, -10 , 89, -100]

def select(new_list):
    for i in range(len(new_list)):
        for x in range(i, len(new_list)):
            if new_list[x] < new_list[i]:
                new_list[x], new_list[i] = new_list[i], new_list[x]

select(list)
print(list)

def change(change_list):
    for i in range(len(change_list)):
        for x in range(i, len(change_list)):
            change_list[x], change_list[i] = change_list[i], change_list[x]

change(list)
print(list)
