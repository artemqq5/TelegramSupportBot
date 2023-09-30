from aiogram import Bot, Dispatcher, types, executor
import logging

from buttons import categories_all
from config import TELEGRAM_BOT_ID

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_ID)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer(text="Категорії питань", reply_markup=categories_all())


@dp.callback_query_handler()
async def call_back_handler(call: types.CallbackQuery):
    await call.message.answer(call.data)

    # match call.data:
    #     case "":


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
