from aiogram import types, Dispatcher 
from create_bot import dp, bot 
from keyboards import kb_client, urlkb, inkb, first, close_keyboard
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

answ = dict()




class FSM_Clients(StatesGroup):
    account = State()
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
    await FSM_Clients.account.set()
    await callback.message.answer('Введите номер телефона (любое число):')


#Загрузка названия
@dp.message_handler(state = FSM_Clients.account)
#Загрузка ответа в базу данных
async def load_account(message: types.Message, state: FSMContext):
    async with state.proxy() as x:
        x['account'] = message.text
    await FSM_Clients.next()
    await message.answer("Введите название планеты:")

@dp.message_handler(state = FSM_Clients.planet)
#Загрузка ответа в базу данных
async def load_planet(message: types.Message, state: FSMContext):
    async with state.proxy() as x:
        x['planet'] = message.text
    await FSM_Clients.next()
    await message.answer('Введите имя:')

@dp.message_handler(state = FSM_Clients.name_client)
#Загрузка ответа в базу данных
async def load_planet(message: types.Message, state: FSMContext):
    async with state.proxy() as x:
        x['name_client'] = message.text
    await FSM_Clients.next()
    await message.answer('Ваш заказ готов. Для редактирования таблицы клиентов введите команду (клиенты).')
    await sqlite_db.sql_add_client(state)
    await state.finish()



@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_client(callback_query.data.replace('del ', ''))
    await callback_query.answer('Клиент удален из таблицы.', show_alert=True)

@dp.message_handler(Text(equals='клиенты', ignore_case=True), state="*")
async def delete_item(message: types.Message):
        #Вывод данных из таблицы
    await bot.send_message(message.from_id, 'Таблица клиентов:')
    read = await sqlite_db.sql_read_clients()
    for ret in read:
        #Отправка списка клиентов
        await bot.send_message(message.from_user.id, 'Данные клиента:\n' f'Номер телефона: {ret[0]}\nПланета: {ret[1]}\nИмя: {ret[2]}', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(f'Удалить клиента {ret[2]}', callback_data=f'del {ret[0]}')))
    












    
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

#Добавление команд
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    
 



@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == message.text:

        await message.answer('Здравствуйте, выберите планету, которую вы хотите посетить.', reply_markup=first)
