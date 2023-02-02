import random
num_sweet = random.randint(100, 200)
#print(num_sweet)
print('Привет! Меня зовут Max. Давай сыграем в игру! \n '
     'На столе лежит неизвестное число конфет: от 100 до 200.\n'
     'Поочереди каждый из нас берет любое количество конфет, но НЕ БОЛЕЕ 28 штук. Победителем считается тот \n'
      'игрок, в чей ход конфеты заканчиваются. Первый ход определяется жеребьевкой.') 

play = int(input('Если начинаем, введи 1 , если не хочешь играть - введи 0:  '))
if play == 1:
    player_list = ['Человек', 'Max']
    random.shuffle(player_list)
    print(f'Жеребьевка закончена. Сейчас ход игрока {player_list[0]}')
    while num_sweet >= 0:
         print('Конфеты есть, играем')
         if player_list[0] == 'Max':
            took_sweet = random.randint(1, 29)
            print(f'Я беру {took_sweet} конфет')
            num_sweet -= took_sweet
            if num_sweet > 0:
               player_list[0] = 'Человек'


         else:
             took_sweet= int(input(f'Сейчас ход {player_list[0]} сколько конфет ты берешь?  '))   
             while took_sweet > 28 :
                print ('За один ход можно взять не более 28 конфет. Попробуй еще раз. ')
                took_sweet= int(input('Cколько конфет ты берешь?  '))
             num_sweet -= took_sweet
             if num_sweet > 0:
               player_list[0] = 'Max'
    print(f'Конфет больше нет!Победил {player_list[0]}!') 
else:
     print('Может в следующий раз. Пока!')   
            
            







#        took_sweet= int(input(f'Сейчас ход {player_list[0]} сколько конфет ты берешь?  '))
#        if took_sweet > 28 :
#         print ('За один ход можно взять не более 28 конфет. Попробуй еще раз. ')
#        else:
#         num_sweet -= took_sweet
#         if number_human == 2:
#             number_human = 1
#             took_sweet= int(input(f'Игра продолжается. Игрок № {number_human} сколько конфет ты берешь?  '))
#         else:
#             number_human = 2
#             took_sweet= int(input(f'Игра продолжается. Игрок № {number_human} сколько конфет ты берешь?  '))
#     print(f'Конфет больше нет!Победил игрок № {number_human}!') 

# else:
#     print('Может в следующий раз. Пока!')   