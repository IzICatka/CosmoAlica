import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur 
    base = sq.connect('CosmoAlica_base.db') #Подключение к файлу базы данных
    cur = base.cursor() #Поиск данных
    if base:
        print('Data base connected OK!')
    #Создание таблицы, в которую будут записываться данные. 
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT)')
    #Сохранение изменений
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}')