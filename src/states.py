from aiogram.dispatcher.filters.state import State, StatesGroup

class GettingName(StatesGroup):
    name = State()

class AddingDream(StatesGroup):
    name = State()
    type = State()
    description = State()

class DeletingLastDream(StatesGroup):
    delete = State()

class ClearingAllHistory(StatesGroup):
    clear = State()

class ShowingHistory(StatesGroup):
    choose_dream = State()

class AddingReview(StatesGroup):
    text = State()