from aiogram import Bot, Dispatcher, types, executor
import logging

from config import TELEGRAM_BOT_ID

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_ID)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    print("start")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
