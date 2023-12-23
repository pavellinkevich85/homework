a = int(input('Левая граница: '))
b = int(input('Правая граница: '))

square = [i ** 2 for i in range(a, b + 1)]
print('Список квадратов чисел в диапазоне от', a, 'до', b, ':', square)

cube = [i ** 3 for i in range (a, b + 1)]
print('Список кубов чисел в диапазоне от ', a, 'до', b, ':', cube)

