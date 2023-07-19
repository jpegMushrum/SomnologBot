from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import dbActions, messages, states

token = open('token.txt').read()
token = "".join(token.split())

storage = MemoryStorage()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
    print('Bot is now running')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if not (dbActions.checkUser(message.from_user.id)):
        await bot.send_message(message.from_user.id, messages.msg_on_start_new)
        await states.GettingName.name.set()
    else:
        await bot.send_message(message.from_user.id, f'Hi, {dbActions.getName(message.from_user.id)}. ' + messages.msg_on_start_old)


@dp.message_handler(commands=['rename'])
async def command_rename(message: types.Message):
    await states.GettingName.name.set()
    await bot.send_message(message.from_user.id, "How can I call you?")

@dp.message_handler(state=states.GettingName.name)
async def getting_name(message: types.Message, state: FSMContext):
    if dbActions.checkUser(message.from_user.id):
        dbActions.changeUserName(message.from_user.id, message.text)
    else:
        dbActions.addUser(message.from_user.id, message.text)
    await bot.send_message(message.from_user.id, f"Ok, {dbActions.getName(message.from_user.id)}. " + messages.msg_on_name)
    await state.finish()

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_help)

@dp.message_handler()
async def empty_handler(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_empty_handler)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
