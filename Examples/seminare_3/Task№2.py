# Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что ее нет

my_list = ['сок', 'носок', 'соковыжималка', 'cок', 'арааи', 'сок', 'список' ]

item = 'сок'
count = 0
for i in range(len(my_list)):
    if item == my_list[i]:
        count +=1
        if count ==2:
            print(f'позиция равна {i}')
            break

else:
    print(f'-1')

# 2 способ решения через список
my_list = ['сок', 'носок', 'соковыжималка', 'cок', 'арааи', 'сок', 'список' ]

item = 'сок'
index_list = []

for i in range(len(my_list)):
    if item == my_list[i]:
        index_list.append(i)
else:
    if len(index_list)< 2:
        print('-1') 
    else:
        print(f'Индекс второго вхождения {index_list[1]}')      

