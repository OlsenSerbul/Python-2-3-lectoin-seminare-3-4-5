from loader import dp, bot
from aiogram import types
from glob import glob
import random
from bot import my_bot


num_sweet = random.randint(100, 150)

            

@dp.message_handler(commands=['start', 'Привет', 'привет'])
async def mes_start(message: types.Message):
   await message.answer(f'Привет, {message.from_user.first_name}! Я самый красивый и обаятельный бот.'
                        ' Сыграем в "Конфетки"? Введи /game для начала игры ')

 

@dp.message_handler(commands=['game'])
async def mes_game(message: types.Message):
    global num_sweet
    await message.answer('Правила игры: на столе лежит неизвестное число конфет: от 100 до 200.'
                    'Поочереди каждый из нас берет любое количество конфет, но НЕ БОЛЕЕ 28 штук. Победителем считается тот '
                    'игрок, в чей ход конфеты заканчиваются. Начинаем жеребьевку.')
    
    player_list = ['бот', f'{message.from_user.first_name}']
    random.shuffle(player_list)
    await message.answer(f'Первым ходит, {player_list[0]}')
    if player_list[0] == 'бот':
        num = my_bot(num_sweet)
        num_sweet -= num
        await message.answer(f'Я взяла {num} конфет.Твой ход...')   
        num_sweet -= int(message.text)
    else:
         await message.answer('Сколько конфет ты берешь? ') 
         


@dp.message_handler()
async def mes_all(message: types.Message):
    if message.text.isdigit():
        player_list = ['бот', f'{message.from_user.first_name}']
        global num_sweet
        if 0 < int(message.text) < 29:
            
            num_sweet -= int(message.text)
            if num_sweet > 0:
               await message.answer(f'Конфеты есть, играем')
               num = my_bot(num_sweet)
               await message.answer(f'Я беру {num} конфет')
               num_sweet-= num
               if num_sweet < 0:
                  await message.answer(f'Последние конфеты забрала я. Победитель - бот! Для новой игры жми /game ')
                  
               else:
                  await message.answer(f'Конфеты есть, играем')
                  await message.answer('Твой ход. Сколько конфет ты берешь? ')
            else:
                await message.answer(f'Конфеты кончились.{player_list[1]} , ты победитель ! Для новой игры жми /game ')
                
        else:       
            await message.answer('Можно взять не более 28 конфет! Повтори ввод ')             
    else:
        await message.answer('Не поняла, повтори ввод') 
                

    
    
        
                
      

