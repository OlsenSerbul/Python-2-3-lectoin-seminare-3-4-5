# Найти в заданном списке элемент.

my_list = ['dfsg45', 'ts42fgg', 'wr4gd', '42345gf']

item = input('Введите число: ')
for i in range(len(my_list)):
    if item in my_list[i]:
        print (f' Число {item} в строке {my_list[i]} с индексом {i}')   
        break
else:
   print(f'В заданном списке нет числа {item}')
