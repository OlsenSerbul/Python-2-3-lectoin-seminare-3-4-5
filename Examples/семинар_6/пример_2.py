# Напишите программу вычисления арифметического выражения,заданного строкой.
# Используйте операции "+, -, /, *", приоритет операций стандартный.
my_string = ' 56 - 7+6* 3-21' # input('Введите арифметическое выражение:  ')
my_list = my_string.replace(' ','').replace('+',' + ').replace('-', ' - ').replace('*',' * ').replace('/', ' / ').split()
print(my_list)

while len(my_list) > 1:
    i = 0
    while '*' in my_list or '/' in my_list:
        if my_list[i] == '*':
          my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
          my_list.pop(i)
          my_list.pop(i)
        elif my_list[i] == '/':
          my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
          my_list.pop(i)
          my_list.pop(i)
        else:
            i+=1
    i = 0
    while '+' in my_list or '-' in my_list:
        if my_list[i] == '+':
          my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
          my_list.pop(i)
          my_list.pop(i)
        elif my_list[i] == '-':
          my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
          my_list.pop(i)
          my_list.pop(i)
        else:
            i +=1
    
print(my_list)