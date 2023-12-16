
list = [1, 2, 4, 7, -10 , 89, -100]
print(list[0:7:2])

a = [1, 2, 3]
b1, b2, b3 = a

print(b3, b1, b2)

a = [-100, 90, -4, 4, 2]
print(len(a))

a = [1, 2, 3, 4, 5]
a.append(2)
print(a)

a.extend([9,4,5,5])
print(a)

i = a.index(5)
print(i + 1)

a.insert(i + 1, 777)
print(a)

b = ['cat', 'dog', 'bat']
b.extend(['mouse'])
print(b)

b = ['cat', 'dog', 'bat']
b.extend('mouse')
print(b)

a.remove(777) # удаление эл-та по названию
print(a)

a.pop(6) # удаление элемента по индексу
print(a)

a.sort()
print(a)

a.reverse()
print(a)

a.sort(reverse=True) # [5, 4, 2, 1]
print(a)

a.reverse()
print(a)

del a[1:5]  # удаляет с индекса 1 по 4 (не 5!!)
            # то есть граница с 0 до 5! (а не с 1 до 5) удалил 1-4!
print(a)

new_list = [1, 2, 'ddd', ['qwerty', 43, 'zxcvb'], 23, 999, 10000]
del new_list[2:5]
print(new_list)

