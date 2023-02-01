import random
num_sweet = random.randint(100, 200)
print(num_sweet)
print('Привет! Прочитай правила игры: играют 2 игрока. На столе лежит неизвестное число конфет: от 100 до 300.\n'
     'Поочереди каждый из вас берет любое количество конфет, но НЕ БОЛЕЕ 28 штук. Победителем считается тот \n'
      'игрок, в чей ход конфеты заканчиваются. Первый ход определяется жеребьевкой.') 

play = int(input('Договоритесь сейчас, кто игрок № 1 и № 2. Если начинаем, введи 1 , если не хочешь играть - введи 0:  '))
if play == 1:
    number_human = random.randint(1,3)
    print(f'Жеребьевка закончена. Сейчас ход игрока № {number_human}')
    while num_sweet >= 0:

       took_sweet= int(input(f'Игрок № {number_human} сколько конфет ты берешь?  '))
       if took_sweet > 28 :
        print ('За один ход можно взять не более 28 конфет. Попробуй еще раз. ')
       else:
        num_sweet -= took_sweet
        if number_human == 2:
            number_human = 1
            took_sweet= int(input(f'Игра продолжается. Игрок № {number_human} сколько конфет ты берешь?  '))
        else:
            number_human = 2
            took_sweet= int(input(f'Игра продолжается. Игрок № {number_human} сколько конфет ты берешь?  '))
    print(f'Конфет больше нет!Победил игрок № {number_human}!') 

else:
    print('Может в следующий раз. Пока!')   


    



