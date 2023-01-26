# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

num = int(input('Введите число элементов списка: '))
my_list = []
for i in range(num):
    my_list.append(round(random.uniform(1, 5), 2))
print(f'Первоначальный список:  {my_list}')
new_list = []
for i in my_list:
    if i - int(i) != 0:
        new_list.append(round(i - int(i), 2))

print(f'Вывод дробной части элементов списка: {new_list}')
maxNum = new_list[0]
minNum = new_list[0]
for i in range(len(new_list)):
    if new_list[i] > maxNum:
       maxNum = new_list[i]
for i in range(len(new_list)):
    if new_list[i] < minNum:
       minNum = new_list[i]       
print(f'Разница между max дробной частью {maxNum} и min дробной частью {minNum} состовляет {round((maxNum - minNum), 2)}')

