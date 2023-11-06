from aiogram import Bot, Dispatcher, types, executor
import logging

from aiogram.types import ParseMode

from buttons.other_btn import set_menu, yes_no_status
from config import TELEGRAM_BOT_ID
from buttons.categories_btn import *
from constants import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_ID)
dp = Dispatcher(bot)


@dp.message_handler(lambda m: m.text in ["FAQ", "Категорії питань", "/start"])
async def start_cmd(message: types.Message):
    if message.text == "/start":
        await message.answer(text=HELLO_MESSAGE, parse_mode=ParseMode.HTML, reply_markup=set_menu())
    elif message.text == "FAQ":
        await message.answer(text=FAQ_MESSAGE, parse_mode=ParseMode.HTML, reply_markup=set_menu())
    elif message.text == "Категорії питань":
        await message.answer(text="Категорії питань", reply_markup=categories_all())


@dp.callback_query_handler(lambda call: call.data in (
        ORDER_TOURS, PAYMENT_AND_PRICES, TRANSPORT, ACCOMMODATION, EXCURSIONS_AND_SERVICES, INSURANCE))
async def category_handler(call: types.CallbackQuery):
    if call.data == ORDER_TOURS:
        await call.message.answer(BUTTON_ORDER_TOURS, reply_markup=subcategory_order())

    elif call.data == PAYMENT_AND_PRICES:
        await call.message.answer(BUTTON_PAYMENT_AND_PRICES, reply_markup=subcategory_price())

    elif call.data == TRANSPORT:
        await call.message.answer(BUTTON_TRANSPORT, reply_markup=subcategory_transport())

    elif call.data == ACCOMMODATION:
        await call.message.answer(BUTTON_ACCOMMODATION, reply_markup=subcategory_rent())

    elif call.data == EXCURSIONS_AND_SERVICES:
        await call.message.answer(BUTTON_EXCURSIONS_AND_SERVICES, reply_markup=subcategory_additional())

    elif call.data == INSURANCE:
        await call.message.answer(BUTTON_INSURANCE, reply_markup=subcategory_guarantee())


@dp.callback_query_handler(lambda call: call.data in (
        HOW_TO_ORDER_TOUR, HOW_TO_CHANGE_ORDER, HOTEL_CHOICE_PACKAGE, CAN_ORDER_INDIVIDUAL_TOUR, WHAT_PAYMENT_METHODS,
        ARE_THERE_EXTRA_FEES, CAN_GET_DISCOUNT, HOW_TO_GET_TOUR_ON_CREDIT, WHICH_AIRLINES, IS_THERE_AIRPORT_TRANSFER,
        HOW_TO_CHANGE_FLIGHT_DATE, CAN_CHOOSE_ROOM, IS_THERE_DIET_FOOD, WHICH_EXCURSIONS_INCLUDED,
        HOW_TO_ORDER_EXTRA_EXCURSIONS, DO_YOU_HAVE_RENTAL_EQUIPMENT, DO_NEED_TRAVEL_INSURANCE, WHAT_RISKS_ARE_COVERED,
        HOW_TO_ASK_FOR_INSURANCE_HELP))
async def subcategory_handler(call: types.callback_query):
    print(call.data)
    if call.data == HOW_TO_ORDER_TOUR:
        await call.message.answer(ANSWER_HOW_TO_ORDER_TOUR, parse_mode=ParseMode.HTML)

    elif call.data == HOW_TO_CHANGE_ORDER:
        await call.message.answer(ANSWER_HOW_TO_CHANGE_ORDER, parse_mode=ParseMode.HTML)

    elif call.data == HOTEL_CHOICE_PACKAGE:
        await call.message.answer(ANSWER_HOTEL_CHOICE_PACKAGE, parse_mode=ParseMode.HTML)

    elif call.data == CAN_ORDER_INDIVIDUAL_TOUR:
        await call.message.answer(ANSWER_CAN_ORDER_INDIVIDUAL_TOUR, parse_mode=ParseMode.HTML)

    elif call.data == WHAT_PAYMENT_METHODS:
        await call.message.answer(ANSWER_WHAT_PAYMENT_METHODS, parse_mode=ParseMode.HTML)

    elif call.data == ARE_THERE_EXTRA_FEES:
        await call.message.answer(ANSWER_ARE_THERE_EXTRA_FEES, parse_mode=ParseMode.HTML)

    elif call.data == CAN_GET_DISCOUNT:
        await call.message.answer(ANSWER_CAN_GET_DISCOUNT, parse_mode=ParseMode.HTML)

    elif call.data == HOW_TO_GET_TOUR_ON_CREDIT:
        await call.message.answer(ANSWER_HOW_TO_GET_TOUR_ON_CREDIT, parse_mode=ParseMode.HTML)

    elif call.data == WHICH_AIRLINES:
        await call.message.answer(ANSWER_WHICH_AIRLINES, parse_mode=ParseMode.HTML)

    elif call.data == IS_THERE_AIRPORT_TRANSFER:
        await call.message.answer(ANSWER_IS_THERE_AIRPORT_TRANSFER, parse_mode=ParseMode.HTML)

    elif call.data == HOW_TO_CHANGE_FLIGHT_DATE:
        await call.message.answer(ANSWER_HOW_TO_CHANGE_FLIGHT_DATE, parse_mode=ParseMode.HTML)

    elif call.data == CAN_CHOOSE_ROOM:
        await call.message.answer(ANSWER_CAN_CHOOSE_ROOM, parse_mode=ParseMode.HTML)

    elif call.data == IS_THERE_DIET_FOOD:
        await call.message.answer(ANSWER_IS_THERE_DIET_FOOD, parse_mode=ParseMode.HTML)

    elif call.data == WHICH_EXCURSIONS_INCLUDED:
        await call.message.answer(ANSWER_WHICH_EXCURSIONS_INCLUDED, parse_mode=ParseMode.HTML)

    elif call.data == HOW_TO_ORDER_EXTRA_EXCURSIONS:
        await call.message.answer(ANSWER_HOW_TO_ORDER_EXTRA_EXCURSIONS, parse_mode=ParseMode.HTML)

    elif call.data == DO_YOU_HAVE_RENTAL_EQUIPMENT:
        await call.message.answer(ANSWER_DO_YOU_HAVE_RENTAL_EQUIPMENT, parse_mode=ParseMode.HTML)

    elif call.data == DO_NEED_TRAVEL_INSURANCE:
        await call.message.answer(ANSWER_DO_NEED_TRAVEL_INSURANCE, parse_mode=ParseMode.HTML)

    elif call.data == WHAT_RISKS_ARE_COVERED:
        await call.message.answer(ANSWER_WHAT_RISKS_ARE_COVERED, parse_mode=ParseMode.HTML)

    elif call.data == HOW_TO_ASK_FOR_INSURANCE_HELP:
        await call.message.answer(ANSWER_HOW_TO_ASK_FOR_INSURANCE_HELP, parse_mode=ParseMode.HTML)

    await call.message.answer("Ваше питання було вирішено?", reply_markup=yes_no_status())


@dp.callback_query_handler(lambda call: call.data in ('yes', 'no'))
async def answer_status_handler(call: types.callback_query):
    if call.data == 'yes':
        await call.message.answer("Чудово! Якщо ще будуть питання - звертайтеся)")
    elif call.data == 'no':
        link_button = InlineKeyboardMarkup()
        link_button.add(InlineKeyboardButton(text="Для зв'язку з оператором", url=f"https://t.me/test"))
        await call.message.answer("📨", reply_markup=link_button)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
