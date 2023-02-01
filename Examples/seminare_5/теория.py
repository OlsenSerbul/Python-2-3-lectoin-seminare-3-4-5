# функция list comprehension

# задание: заполнить список рандомно:
# from random import randint as RI

# my_list = [RI(0, 100) for i in range(10)]
# print(my_list)

# задать словарь:

# my_dict = {i:i**2 for i in range(10)}
# print(my_dict)
 

 # инструмент map (для применения какой то любой функции для дюбого элемента указанного списка):
 # Пример:

string = '1 2 3 4 5 6 7 8'
# перевести стоку в список чисел
string = string.split()

my_list = []
for i in string:
    my_list.append(int(i))

print(my_list)
# или:
my_list = list(map(int, string.split()))
print(my_list)

# инструмент filter:
my_list = list(filter(lambda x: x % 2 != 0, list(map(int, string.split()))))
print(my_list)
# данный инструмент в примере отсеит все четные элементы и оставит только нечетные
# Пример: в заданной строке из символов найти все содержащие букву "с":

string = 'a b scd vbn rtc cer xsac co gh jcm'
my_list = list(filter(lambda x: 'c' in x, string.split()))
print(my_list)

# Инструмент enumerate (позволяет обратиться к элементу и его индексу, может заменить range)
#Пример: в заданном списке вывести инлекс элемента 'cer'
string = 'a b scd vbn rtc cer xsac co gh jcm'
my_list = string.split()

for i, item in enumerate(my_list):
    if item == 'cer':
        print(i)


