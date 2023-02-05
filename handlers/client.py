from aiogram import types, Dispatcher 
from create_bot import dp, bot 
from keyboards import kb_client, urlkb, inkb, first, close_keyboard
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

answ = dict()




class FSM_Clients(StatesGroup):
     planet = State()
     name_client = State()
    #  id = State()
#Команда старт
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте, выберите команду:', reply_markup = first)
        await message.delete()
    except:
        await message.reply('Для оформления билетов напишите нашему боту: \nhttp://t.me/CosmoAlicaBot')

async def menu(callback):
    await bot.send_message(callback.from_user.id, 'Здравствуйте, выберите команду:', reply_markup = first)

async def menu2(message):
    await bot.send_message(message.from_user.id, 'Здравствуйте, выберите команду:', reply_markup = first)

#Основное меню
@dp.callback_query_handler(text='zakaz')
async def zakaz(callback: types.CallbackQuery):
    await FSM_Clients.planet.set()
    await callback.message.reply('Введите название планеты.')
    

#Загрузка названия
@dp.message_handler(state = FSM_Clients.planet)
#Загрузка ответа в базу данных
async def load_planet(message: types.Message, state: FSMContext):
    async with state.proxy() as x:
        x['planet'] = message.text
    await FSM_Clients.next()
    await message.reply("Введите имя.")

@dp.message_handler(state = FSM_Clients.name_client)
#Загрузка ответа в базу данных
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as x:
        x['name_client'] = message.text
    await sqlite_db.sql_add_client(state)
    await state.finish()
    













    
@dp.callback_query_handler(text='spisok')
async def spisok(callback: types.CallbackQuery):
    await callback.message.answer('Список планет:')
    await sqlite_db.sql_read(callback)
    await menu(callback)

@dp.callback_query_handler(text='time')
async def time(callback: types.CallbackQuery):
    await callback.message.answer('Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')
    await menu(callback)

@dp.callback_query_handler(text='place')
async def place(callback: types.CallbackQuery):
    await callback.message.answer('ул. Научный центр, 5')
    await menu(callback)

@dp.callback_query_handler(text='support')
async def support(callback: types.CallbackQuery):
    await callback.message.answer('Коммпания CosmoAlica занимается путешествиями к планетам Солнечной системы.')
    await menu(callback)





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
    
 



@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == message.text:

        await message.answer('Здравствуйте, выберите планету, которую вы хотите посетить.', reply_markup=first)
