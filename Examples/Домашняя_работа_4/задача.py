# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите максимальную степень n: ')) # задаем натуральную степень k
def rand_equation(k):
    equation = {} # создаем пустой словарь
    
    # заполняем словарь степень- ключ, значение коэффициента при степени - рандомное число
    for i in range(k, -1, -1):
        if i == k:
            while True:
                koef = random.randint(-100, 100)
                if koef != 0:
                    break
            equation[i] = koef
        else:
            equation[i] = random.randint(-100, 100)
    return equation

my_dict = rand_equation(k)
print(my_dict)

my_list = list(my_dict.items())
print(my_list)

for i in range(len(my_list)):
    print(f'{my_list[list(i)]}*x**{my_list[list(i)]}')

    # for key in my_dict:
    #     for item in my_dict:
    #         if item == -1:
    #             rez = f'-x **{key} '
    #         elif item == 1:
    #             rez = f'x **{key} '
    #         else:
    #             rez = f'{item}x **{key} '

    # return rez
            
# rez = rez_equation(k, my_dict)          
# print(*rez)
#my_string = rez.replace("'", '').replace('[', '').replace(',','').replace(']', '')



# string1 = f'{my_string[]}*x**{my_string(1,2)}'
# print(string1)