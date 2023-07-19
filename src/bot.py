from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import messages, dbActions, states

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
async def setting_name(message: types.Message, state: FSMContext):
    if dbActions.checkUser(message.from_user.id):
        await dbActions.changeUserName(message.from_user.id, message.text)
    else:
        await dbActions.addUser(message.from_user.id, message.text)
    await bot.send_message(message.from_user.id, f"Ok, {dbActions.getName(message.from_user.id)}. " + messages.msg_on_name)
    await state.finish()

@dp.message_handler(commands=['add'])
async def command_add_1(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_adding_1)
    await states.AddingDream.name.set()


@dp.message_handler(state=states.AddingDream.name)
async def command_add_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dream_name'] = message.text.replace('\'', '\\\'')

    await bot.send_message(message.from_user.id, messages.msg_on_adding_2)
    await states.AddingDream.next()

@dp.message_handler(state=states.AddingDream.type)
async def command_add_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dream_type'] = message.text.replace('\'', '\\\'')

    await bot.send_message(message.from_user.id, messages.msg_on_adding_3)
    await states.AddingDream.next()

@dp.message_handler(state=states.AddingDream.description)
async def command_add_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dream_description'] = message.text.replace('\'', '\\\'')
        await dbActions.addDream(message.from_user.id, data['dream_name'], data['dream_type'], data['dream_description'])
    await bot.send_message(message.from_user.id, messages.msg_on_adding_4)
    await state.finish()


@dp.message_handler(commands=['delete'])
async def command_delete(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_deleting)
    await states.DeletingLastDream.delete.set()

@dp.message_handler(state=states.DeletingLastDream.delete)
async def delete_sure(message: types.Message, state: FSMContext):
    if ''.join(message.text.lower().split()) == 'yes':
        await dbActions.deleteLastDream(message.from_user.id)
        await bot.send_message(message.from_user.id, messages.msg_after_deleting)
    else:
        await bot.send_message(message.from_user.id, messages.msg_delete_denied)
    await state.finish()

@dp.message_handler(commands=['clear'])
async def command_clear(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_clear)
    await states.ClearingAllHistory.clear.set()

@dp.message_handler(state=states.ClearingAllHistory.clear)
async def clear_sure(message: types.Message, state: FSMContext):
    if ''.join(message.text.lower().split()) == 'yes':
        await dbActions.clearDreamHistory(message.from_user.id)
        await bot.send_message(message.from_user.id, messages.msg_after_clear)
    else:
        await bot.send_message(message.from_user.id, messages.msg_clear_denied)
    await state.finish()


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_help)

@dp.message_handler()
async def empty_handler(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_empty_handler)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
