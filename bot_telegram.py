from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == message.text:

        await message.answer('Здравствуйте, выберите планету, которую вы хотите посетить.')




executor.start_polling(dp, skip_updates=True)