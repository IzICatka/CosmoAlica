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