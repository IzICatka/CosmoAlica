from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')

#Заменяет клавиатуру на кнопки
kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

#Пишет каждую команду с новой строки
kb_client.add(b1).row(b2, b3)