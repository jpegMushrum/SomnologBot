from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = open('token.txt').read()

token = "".join(token.split())

bot = Bot(token=token)
dp = Dispatcher(bot)

msg_on_start = 'Hello, it\'s a bot for tracking your dreams. You can add new dream, see your history of dreams, ' \
               'see statistic or set time notifications. Use shown commands: \n/add - Let you add new dream. ' \
               '\n/history - Shows your numbered dream. \n /statistic - Shows your statistic.\n ' \
               '/help - Show list of commands again.'

msg_on_help = 'Available commands: \n/add - Let you add new dream. \n/history - Shows your numbered dream. \n ' \
              '/statistic - Shows your statistic.\n /help - Show list of commands again.\n ' \
              'Call some to see information about this command.'

async def on_startup(_):
    print('Bot is now running')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, msg_on_start)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, msg_on_help)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.from_user.id)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
