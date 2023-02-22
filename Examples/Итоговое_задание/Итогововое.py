
# f(x) = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30

# 1.Определить корни

# 2.Найти интервалы, на которых функция возрастает

# 3.Найти интервалы, на которых функция убывает

# 4.Построить график

# 5.Вычислить вершину

# 6.Определить промежутки, на котором f > 0

# 7.Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

a, b ,c, d ,e = -12, -18, 5, 10, -30

limit = 100
step = 0.01
step_acr = 0.0001 
line_style = '-'
color = 'b'
direct_up = True


def switch_line():
    global line_style
    if line_style == '-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

def func(x):
    f = a* x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
    return f


x = np.arange(-limit, limit + step, step)


new_x = [(-limit, 'limit')]



for i in range(len(x)-1):
    if func(x[i])>0 and func(x[i+1])<0 or func(x[i])<0 and func(x[i+1])>0:
        x_acr = np.arange(x[i], x[i+1]+step_acr, step_acr)
        for j in range(len(x_acr)-1):
            if func(x_acr[j])>0 and func(x_acr[j+1])<0 or func(x_acr[j])<0 and func(x_acr[j+1])>0:
                new_x.append((x_acr[j], 'zero'))
    if direct_up:
        if func(x[i])>func(x[i+1]):
            direct_up = False
            new_x.append((x[i], 'dir'))
    else:
        if func(x[i])<func(x[i+1]):
            direct_up = True
            new_x.append((x[i], 'dir'))
        

new_x.append((limit, 'limit'))

print(f'Корни на промежутке [-100; 100] : {new_x}')


for i in range(len(new_x)-1):
    cur_x = np.arange(new_x[i][0], new_x[i+1][0] + step, step)
    if new_x[i][1] == 'zero':
        plt.plot(new_x[i][0], new_x[i+1][0], 'go')
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
         plt.plot(cur_x, func(cur_x), switch_color())
plt.grid()
plt.show()

