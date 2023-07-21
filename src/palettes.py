from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_cancel = InlineKeyboardButton(text='cancel', callback_data='cancel')
button_yes = InlineKeyboardButton(text='yes', callback_data='yes')
button_no = InlineKeyboardButton(text='no', callback_data='no')
yes_no_keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
yes_no_keyboard.row(button_yes, button_no)

button_usual = InlineKeyboardButton(text='usual', callback_data='usual')
button_very_strange = InlineKeyboardButton(text='very strange', callback_data='very_strange')
button_nightmare = InlineKeyboardButton(text='nightmare', callback_data='nightmare')
button_erotic = InlineKeyboardButton(text='erotic', callback_data='erotic')
types_keyboard = InlineKeyboardMarkup()
types_keyboard.row(button_usual, button_erotic, button_nightmare, button_very_strange).add(button_cancel)

button_next_page = InlineKeyboardButton(text='next page', callback_data='next_page')
button_previous_page = InlineKeyboardButton(text='previous page', callback_data='previous_page')
pages_keyboard = InlineKeyboardMarkup(row_width=2)
pages_keyboard.row(button_previous_page, button_next_page).add(button_cancel)

button_to_choose = InlineKeyboardButton(text='back to pages', callback_data='back_to_choose')
show_dream_keyboard = InlineKeyboardMarkup()
show_dream_keyboard.add(button_to_choose).add(button_cancel)

cancel_keyboard = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cancel_keyboard.add(button_cancel)
