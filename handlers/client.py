from aiogram import types, Dispatcher 
from create_bot import dp, bot 
from keyboards import kb_client, urlkb, inkb, first, close_keyboard
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text

answ = dict()
#Команда старт
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте, выберите команду:', reply_markup = first)
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

# @dp.message_handler(commands='test')
async def test_commands(message : types.Message):
    await message.answer('Заказ билетов', reply_markup=inkb)

@dp.callback_query_handler(text='like_+1')
async def like(callback: types.CallbackQuery):
    await callback.answer('Нравится')



@dp.callback_query_handler(text='zakaz')
async def zakaz(callback: types.CallbackQuery):
    await callback.message.answer('Выберите планету:')
    await sqlite_db.sql_read(callback)

# @dp.callback_querry_handler(Text(startwith='like'))
# async def www_call(callback : types.CallbackQuery):
#     res = int(callback.data.split('_')[1])
#     if f'{callback.from_user.id}' not in answ:
#         answ[f'{callback.from_user.id}'] = res
#         await callback.answer('Вы проголосовали')
#     else:
#         await callback.answer('Вы уже проголосовали', show_alert=True)

# @dp.message_handler(commands='Удалить')
# async def delete_item(message: types.Message):
#         #Вывод данных из таблицы
#         read = await sqlite_db.sql_read2()
#         for ret in read:
#             #Отправка списка планет
#             await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}')
#             #Добавление кнопки удалить
#             await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
#                 add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}'))) 


#Добавление команд
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(CosmoAlica_open_command, commands=['Режим_работы'])
    dp.register_message_handler(CosmoAlica_place_command, commands=['Расположение'])
    dp.register_message_handler(CosmoAlica_planets, commands=['Меню'])
    dp.register_message_handler(url_command, commands=['ссылки'])
    dp.register_message_handler(test_commands, commands=['test'])

    
    
 



# @dp.message_handler()_
# async def echo_send(message : types.Message):
#     if message.text == message.text:

#         await message.answer('Здравствуйте, выберите планету, которую вы хотите посетить.')
