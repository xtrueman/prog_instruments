#!python3

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot_token = 'xxxxx'

bot = Bot(token = bot_token)
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def echo_message(msg: types.Message):
     await bot.send_message( msg.from_user.id, 'MsgLen: %d' % len(msg.text) )

# Запуск процесса поллинга новых апдейтов
async def main():
    print('Run bot...')
    await dp.start_polling(bot)

asyncio.run(main())

