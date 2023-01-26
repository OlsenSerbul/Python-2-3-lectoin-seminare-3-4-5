# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число: '))
my_list = []
my_list.append(num % 2)
while num != 1: 
    num = int(num / 2)
    my_list.append(num % 2)
my_list.reverse()
print(f'Число в двоичной системе :', end=' ')
print(*my_list, sep='')