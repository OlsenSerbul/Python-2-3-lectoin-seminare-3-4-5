# Дана последовательность чисел. Получить список уникальных элементов в заданной последовательности.
# Пример:
#[1,5,7,4,1,6,5] => [4,6,7]

my_list = [1, 4, 3, 7, 8, 8, 1]
my_list = list(filter(lambda x: my_list.count(x) == 1, my_list))
print(my_list)

# 2 способ решения с помощью словаря:
my_list = [1, 4, 3, 7, 8, 8, 1]
# создаем пустой словарь:
my_dict={}
# записываем каждый элемент в качстве ключа, а заначение - это количество вхождений
for i in my_list:
    my_dict[i] = my_dict.get(i, 0) + 1
print(my_dict)
#если в словаре значение =1, то выводим
for key, value in my_dict.items():
    if value == 1:
        print(key)

# или использовать list comprehension:
my_list = [1, 4, 3, 7, 8, 8, 1]
new_list = (x for x in my_list if my_list.count(x) == 1) 