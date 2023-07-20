from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_rename = KeyboardButton('/rename')
button_add = KeyboardButton('/add')
button_history = KeyboardButton('/history')
button_statistic = KeyboardButton('/statistic')
button_delete = KeyboardButton('/delete')
button_clear = KeyboardButton('/clear')
button_cancel = KeyboardButton('/cancel')
button_help = KeyboardButton('/help')

standard_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
standard_keyboard.row(button_add, button_history, button_statistic)
standard_keyboard.row(button_delete, button_clear)
standard_keyboard.row(button_rename, button_help)

button_yes = KeyboardButton('yes')
button_no = KeyboardButton('no')
yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
yes_no_keyboard.row(button_yes, button_no)

button_next_page = KeyboardButton('next page')
button_previous_page = KeyboardButton('previous page')
pages_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pages_keyboard.row(button_previous_page, button_next_page).add(button_cancel)

cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_keyboard.add(button_cancel)
