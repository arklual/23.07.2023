from aiogram import types
from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import Executor

import os

from settings import *

bot = Bot(TOKEN)
dp = Dispatcher(bot)
e = Executor(dp)

@dp.message_handler(lambda m: m.text.startswith('/start'))
async def start(message: types.Message):
    if message.text == '/start':
        await message.answer('Чтобы включить бота введите: "/start название_бота"\nЧтобы выключить бота: "/stop название_бота"\nЧтобы посмотреть статус бота: "/status название_бота"')
        return
    bot_to_start = message.text.split(' ')[-1]
    os.system(f'systemctl start {bot_to_start}')
    await message.answer(f'{bot_to_start} запущен')


@dp.message_handler(lambda m: m.text.startswith('/stop'))
async def stop(message: types.Message):
    if message.text == '/stop':
        await message.answer('Вы не ввели название бота')
        return
    bot_to_stop = message.text.split(' ')[-1]
    os.system(f'systemctl stop {bot_to_stop}')
    await message.answer(f'{bot_to_stop} остановлен')

@dp.message_handler(lambda m: m.text.startswith('/status'))
async def status(message: types.Message):
    if message.text == '/status':
        await message.answer('Вы не ввели название бота')
        return
    bot_to_status= message.text.split(' ')[-1]
    status = os.popen(f'systemctl status {bot_to_status}').read()
    await message.answer(status.split('\n')[0])




e.start_polling()