from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = open('token.txt').read()

token = "".join(token.split())

bot = Bot(token=token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is now running')


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
