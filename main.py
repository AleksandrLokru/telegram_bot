import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаем объект бота
bot = Bot(token=config.token)

#Диспечер
dp = Dispatcher()


#Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Окей, лэтсгоуй')
    name = message.chat.first_name
    await message.answer(f'Привет, {name}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())