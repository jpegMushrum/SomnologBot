from aiogram.dispatcher.filters.state import State, StatesGroup

class GettingName(StatesGroup):
    name = State()

