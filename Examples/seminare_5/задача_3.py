# Дан список чисел. Создайте список, в которую попадают числа, описываемые 
# возрастающую последовательность. Порядок элементов менять нельзя

from random import randint as RI

my_list = [RI(1, 20) for i in range(20)]
print(my_list)
new_list = []
list1= []
for i in range(len(my_list)):
    num = my_list[i]
    new_list = [num]
    for j in range(i +1 , len(my_list)):
        if num + 1 == my_list[j]:
           new_list.append(my_list[j])
           num += 1
    if len(new_list) >= 2 and new_list not in list1:
        list1.append(new_list)
print(list1)
max = 0
for i, item in enumerate(list1):
    if len(item) > len(list1[max]):
        max = i
print(list1[max])