from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')


#Заменяет клавиатуру на кнопки
kb_client = ReplyKeyboardMarkup(resize_keyboard = True)


#Пишет каждую команду с новой строки
kb_client.add(b1).row(b2, b3)


urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='https://google.com'), InlineKeyboardButton(text='Ссылка4', url='https://google.com'),\
    InlineKeyboardButton(text='Ссылка5', url='https://google.com')]
urlkb.add(urlButton, urlButton2).row(*x)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_+1'),\
    InlineKeyboardButton(text='DisLike', callback_data='like_-1'))



first = InlineKeyboardMarkup(row_width=1)
zakaz_biletov = InlineKeyboardMarkup(text='Заказ билетов', callback_data='zakaz')
spisok_planet = InlineKeyboardMarkup(text='Список планет', callback_data='spisok')
time_work = InlineKeyboardMarkup(text='Режим работы', callback_data='time')
place_street = InlineKeyboardMarkup(text='Расположение', callback_data='place')
help = InlineKeyboardMarkup(text='Служба поддержки', callback_data='support' )
first.add(zakaz_biletov, spisok_planet, time_work, place_street, help)



close_keyboard = InlineKeyboardMarkup(row_width=1)
close_button = InlineKeyboardButton(text='Отмена', callback_data='close')
close_keyboard.add(close_keyboard)





