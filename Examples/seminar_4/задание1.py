# в квадратном уравнении нужно посчитать количество корней:  "Аx2 - Вx + С = 0"

# первое- вычленить из строки значения коэффициентов
# второе - написать функцию в которую передать значение коэффициентов и по формуле дискриминанта посчитать количество корней

import math

new_equation = '3*x**2 - 12*x + 6 = 0'
#убираем все пробелы, - меняем на +-, и делаем сплит по +
my_list = new_equation.replace(' ', '').replace('-', '+-').replace('=0', '').replace('**2', '').replace('*x', '').split('+')

a = int(my_list[0])
b = int(my_list[1])
c = int(my_list[2])

discr = b**2 - 4*a*c
print('Дискриминант D = %.2f'% discr)
if discr > 0 :
    x1 = (-b + math.sqrt(discr)) / (2* a)
    x2 = (-b - math.sqrt(discr)) / (2* a)
    print('x1 = %.2f\nx2 = %.2f'% (x1,x2))

elif discr == 0:
    x = -b / 2*a
    print('x = %.2f'% x)
else:
    print('Корней нет')

# 2 вариант решения
def equation(string:str):
    eq = []
    string = string.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -').split()
    for item in string:
        if item.startswith('x'):
            eq.append(1)
        elif item.startswith('-x'):
            eq.append(-1)
        else:
            eq.append(int(item.split('*x')[0]))
    return eq

    a, b, c = equation(new_equation)

    print(a)
    print(b)
    print(c)