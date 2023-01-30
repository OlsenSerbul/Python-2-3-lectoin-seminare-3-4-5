# split

# my_string = 'Питон самый лучший язык в мире'

# my_list = my_string.split(' ')

# print(my_list)

# replace

# my_string = 'Питон самый лучший язык в мире'

# my_list = my_string.replace('и', 'И')

# print(my_list)

#можно применять несколько replace

# my_string = 'Питон самый лучший язык в мире'

# my_list = my_string.replace('и', 'И').replace('а', '')

# print(my_list)

# заполните словать n ключами, где каждому n  соответсвует значение 3n+1

my_dict = {}

n = int(input('Введите число: '))

for i in range(1, n+1):
    my_dict[i]=3 * i + 1

print(my_dict)
