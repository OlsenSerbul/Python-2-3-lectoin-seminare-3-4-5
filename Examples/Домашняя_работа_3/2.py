# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

num = int(input('Введите число элементов списка: '))
my_list = []
for i in range(num):
    my_list.append(random.randint(1, 100))
print(f'Первоначальный список:  {my_list}')

new_list = []
if num % 2 == 0:
   for i in range(int(num / 2 )):
       new_list.append(my_list[i] * my_list[num -1 - i])
else:
    for i in range(int(num / 2 + 1 )):
        new_list.append(my_list[i] * my_list[num -1 - i])

print(f'Результатом будет список: {new_list} ')

