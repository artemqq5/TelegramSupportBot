from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def set_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(KeyboardButton("Категорії питань"))
    keyboard.add(KeyboardButton("FAQ"))
    return keyboard


def yes_no_status() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Так", callback_data="yes"))
    keyboard.add(InlineKeyboardButton("Ні", callback_data="no"))
    return keyboard
