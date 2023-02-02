import random
num_sweet = random.randint(100, 200)
#print(num_sweet)
print('Привет! Прочитай правила игры: играют 2 игрока. На столе лежит неизвестное число конфет: от 100 до 200.\n'
     'Поочереди каждый из вас берет любое количество конфет, но НЕ БОЛЕЕ 28 штук. Победителем считается тот \n'
      'игрок, в чей ход конфеты заканчиваются. Первый ход определяется жеребьевкой.') 

play = int(input('Договоритесь сейчас, кто игрок № 1 и № 2. Если начинаем, введи 1 , если не хочешь играть - введи 0:  '))
if play == 1:
    number_human1 = [1, 2]
    random.shuffle(number_human1)
    print(f'Жеребьевка закончена. Сейчас ход игрока № {number_human1[0]}')
    while num_sweet >= 0:
         print('Конфеты есть, играем')
         took_sweet= int(input(f'Игрок № {number_human1[0]} сколько конфет ты берешь?  '))
         while took_sweet > 28 :
              print ('За один ход можно взять не более 28 конфет. Попробуй еще раз. ')
              took_sweet= int(input('Cколько конфет ты берешь?  '))
              num_sweet -= took_sweet
         num_sweet -= took_sweet
         if num_sweet > 0:
            temp = number_human1[0]
            number_human1[0]=number_human1[1]
            number_human1[1]=temp
    print(f'Конфет больше нет!Победил игрок № {number_human1[0]}!')
else:
     print('Может в следующий раз. Пока!')   
           

