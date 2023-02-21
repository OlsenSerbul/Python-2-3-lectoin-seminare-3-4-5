from loader import dp
from aiogram.types import Message



@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}')
    print(message) # команда которая дает полную инфо об параметрах сообщения

@dp.message_handler(commands=['help'])
async def mes_start(message: Message):
    await message.answer('Чем могу помочь?')
   


