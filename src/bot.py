import math
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import messages, dbActions, states, palettes

token = open('token.txt').read()
token = "".join(token.split())

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
    print('Bot is now running')

@dp.callback_query_handler((lambda call: call.data == 'cancel'), state='*')
async def command_cancel(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(call.from_user.id, messages.msg_on_cancel)
    await state.finish()

@dp.message_handler(state='*', commands=['cancel'])
async def command_cancel(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, messages.msg_on_cancel)
    await state.finish()

@dp.message_handler(state='*', commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    if not (await dbActions.checkUser(message.from_user.id)):
        await bot.send_message(message.from_user.id, messages.msg_on_start_new)
        await dbActions.addUser(message.from_user.id, message.from_user.first_name)
        await states.GettingName.name.set()
    else:
        await bot.send_message(message.from_user.id, messages.msg_on_start_old(await dbActions.getName(message.from_user.id)))
        await state.finish()

@dp.message_handler(state='*', commands=['rename'])
async def command_rename(message: types.Message):
    await states.GettingName.name.set()
    await bot.send_message(message.from_user.id, messages.msg_on_rename, reply_markup=palettes.cancel_keyboard)

@dp.message_handler(state='*', commands=['add'])
async def command_add_1(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_adding_1(await dbActions.getName(message.from_user.id)), reply_markup=palettes.cancel_keyboard)
    await states.AddingDream.name.set()

@dp.message_handler(state='*', commands=['delete'])
async def command_delete(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_deleting, reply_markup=palettes.yes_no_keyboard)
    await states.DeletingLastDream.delete.set()

@dp.message_handler(state='*', commands=['clear'])
async def command_clear(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_clear, reply_markup=palettes.yes_no_keyboard)
    await states.ClearingAllHistory.clear.set()

async def show_dream(message: types.Message):
    number = int(message.text)
    if number > await dbActions.getNumberOfDreams(message.from_user.id) or number < 1:
        await bot.send_message(message.from_user.id, messages.msg_on_wrong_number, reply_markup=palettes.show_dream_keyboard)
    else:
        dream = await dbActions.getOneDream(message.from_user.id, number)
        await bot.send_message(message.from_user.id, messages.msg_send_dream(dream["name"], dream["type"], dream["description"]),
                               reply_markup=palettes.show_dream_keyboard)

@dp.callback_query_handler((lambda call: call.data in ['next_page', 'previous_page', 'back_to_choose']), state='*')
async def choosing_page(call: types.CallbackQuery, state: FSMContext):
    try:
        async with state.proxy() as data:
            if call.data == 'next_page' and data["current_page"] < data["number_of_pages"]:
                data["current_page"] += 1
            elif call.data == 'previous_page' and data["current_page"] > 1:
                data["current_page"] -= 1
            page = await dbActions.getListOfDreams(call.from_user.id, data["current_page"])

        response = messages.msg_on_history(data["current_page"], data["number_of_pages"], page)
        await bot.edit_message_text(response, call.from_user.id, call.message.message_id, reply_markup=palettes.pages_keyboard)
    except:
        await call.answer(messages.msg_choosing_page_error)

@dp.message_handler(state='*', commands=['history'])
async def command_history(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["current_page"] = 1
        data["number_of_pages"] = math.ceil(await dbActions.getNumberOfDreams(message.from_user.id) / 20)
        if data["number_of_pages"] == 0:
            await bot.send_message(message.from_user.id, messages.msg_if_no_dreams)
            return

        page = await dbActions.getListOfDreams(message.from_user.id, data["current_page"])
        response = messages.msg_on_history(data['current_page'], data['number_of_pages'], page)

    await bot.send_message(message.from_user.id, response, reply_markup=palettes.pages_keyboard)
    await states.ShowingHistory.choose_dream.set()

@dp.message_handler(state='*', commands=['statistic'])
async def command_statistic(message: types.Message, state: FSMContext):
    if await dbActions.getNumberOfDreams(message.from_user.id) > 0:
        data = await dbActions.getStatistic(message.from_user.id)
        await bot.send_message(message.from_user.id, messages.msg_statistic(await dbActions.getName(message.from_user.id), data))
    else:
        await bot.send_message(message.from_user.id, messages.msg_if_no_dreams)
    await state.finish()
@dp.message_handler(state='*', commands=['help'])
async def command_help(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, messages.msg_on_help)
    await state.finish()

@dp.message_handler(state=states.GettingName.name)
async def setting_name(message: types.Message, state: FSMContext):
    await dbActions.changeUserName(message.from_user.id, message.text.replace('\'', '\"').replace('\\', '\\\\'))

    await bot.send_message(message.from_user.id, messages.msg_on_name(await dbActions.getName(message.from_user.id)))
    await state.finish()

@dp.message_handler(state=states.AddingDream.name)
async def command_add_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dream_name'] = message.text.replace('\'', '\"').replace('\\', '\\\\')

    await bot.send_message(message.from_user.id, messages.msg_on_adding_2, reply_markup=palettes.types_keyboard)
    await states.AddingDream.next()

@dp.callback_query_handler(lambda c: c.data in ['usual', 'erotic', 'nightmare'], state=states.AddingDream.type)
async def command_add_3(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['dream_type'] = call.data
        await bot.send_message(call.from_user.id, messages.msg_on_adding_3, reply_markup=palettes.cancel_keyboard)
        await states.AddingDream.next()

@dp.message_handler(state=states.AddingDream.type)
async def command_add_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() in ['erotic', 'nightmare', 'usual']:
            data['dream_type'] = message.text
            await bot.send_message(message.from_user.id, messages.msg_on_adding_3, reply_markup=palettes.cancel_keyboard)
            await states.AddingDream.next()
        else:
            data['dream_type'] = 'usual'
            await bot.send_message(message.from_user.id, messages.msg_on_adding_2)

@dp.message_handler(state=states.AddingDream.description)
async def command_add_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dream_description'] = message.text.replace('\'', '\"').replace('\\', '\\\\')
        await dbActions.addDream(message.from_user.id, data['dream_name'], data['dream_type'], data['dream_description'])
    await bot.send_message(message.from_user.id, messages.msg_on_adding_4(await dbActions.getName(message.from_user.id)))
    await state.finish()

@dp.callback_query_handler(lambda c: c.data in ['yes', 'no'], state=states.DeletingLastDream.delete)
async def delete_sure(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'yes':
        await dbActions.deleteLastDream(call.from_user.id)
        await bot.edit_message_text(messages.msg_after_deleting(await dbActions.getName(call.from_user.id)), call.from_user.id, call.message.message_id)
    else:
        await bot.edit_message_text(messages.msg_delete_denied(await dbActions.getName(call.from_user.id)), call.from_user.id, call.message.message_id)
    await state.finish()

@dp.callback_query_handler(lambda c: c.data in ['yes', 'no'], state=states.ClearingAllHistory.clear)
async def clear_sure(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'yes':
        await dbActions.clearDreamHistory(call.from_user.id)
        await bot.edit_message_text(messages.msg_after_clear(await dbActions.getName(call.from_user.id)), call.from_user.id, call.message.message_id)
    else:
        await bot.edit_message_text(messages.msg_clear_denied(await dbActions.getName(call.from_user.id)), call.from_user.id, call.message.message_id)
    await state.finish()

@dp.message_handler(state=states.ShowingHistory.choose_dream)
async def choosing_dream(message: types.Message):
    if message.text.isnumeric():
        await show_dream(message)
    else:
        await bot.send_message(message.from_user.id, messages.msg_if_smt_wrong, reply_markup=palettes.show_dream_keyboard)

@dp.message_handler()
async def empty_handler(message: types.Message):
    await bot.send_message(message.from_user.id, messages.msg_on_empty_handler(await dbActions.getName(message.from_user.id)))

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
