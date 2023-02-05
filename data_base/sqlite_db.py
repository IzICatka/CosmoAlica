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
    base.execute('CREATE TABLE IF NOT EXISTS clients(account TEXT PRIMARY KEY, planet TEXT, name_client TEXT)')
    #Сохранение изменений
    base.commit()
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_client(state):
    async with state.proxy() as x:
        cur.execute('INSERT INTO clients VALUES (?, ?, ?)', tuple(x.values()))
        base.commit()



async def sql_read(callback):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(callback.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}')


async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_read_clients():
    return cur.execute('SELECT * FROM clients').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()


async def sql_delete_client(data):
    cur.execute('DELETE FROM clients WHERE account == ?', (data,))
    base.commit()