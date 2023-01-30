from aiogram import types, Dispatcher 
from create_bot import dp, bot 
from keyboards import kb_client, urlkb
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

#Команда старт
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Выберите планету, которую вы хотите посетить.', reply_markup = kb_client)
        await message.delete()
    except:
        await message.reply('Для оформления билетов напишите нашему боту: \nhttp://t.me/CosmoAlicaBot')


#Команда режим работы
async def CosmoAlica_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


#Команда расположение
async def CosmoAlica_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Научный центр, 5', reply_markup = ReplyKeyboardRemove())

# @dp.message_handler(commands=['Меню'])
async def CosmoAlica_planets(message : types.Message):
    await sqlite_db.sql_read(message)

# @dp.message_handler(commands='ссылки')
async def url_command(message : types.Message):
    await message.answer('Ссылки:', reply_markup = urlkb)
    

#Добавление команд
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(CosmoAlica_open_command, commands=['Режим_работы'])
    dp.register_message_handler(CosmoAlica_place_command, commands=['Расположение'])
    dp.register_message_handler(CosmoAlica_planets, commands=['Меню'])
    dp.register_message_handler(url_command, commands=['ссылки'])
 



# @dp.message_handler()
# async def echo_send(message : types.Message):
#     if message.text == message.text:

#         await message.answer('Здравствуйте, выберите планету, которую вы хотите посетить.')
