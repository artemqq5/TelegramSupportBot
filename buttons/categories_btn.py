from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants import *


def categories_all() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(BUTTON_ORDER_TOURS, callback_data=ORDER_TOURS))
    keyboard.add(InlineKeyboardButton(BUTTON_PAYMENT_AND_PRICES, callback_data=PAYMENT_AND_PRICES))
    keyboard.add(InlineKeyboardButton(BUTTON_TRANSPORT, callback_data=TRANSPORT))
    keyboard.add(InlineKeyboardButton(BUTTON_ACCOMMODATION, callback_data=ACCOMMODATION))
    keyboard.add(InlineKeyboardButton(BUTTON_EXCURSIONS_AND_SERVICES, callback_data=EXCURSIONS_AND_SERVICES))
    keyboard.add(InlineKeyboardButton(BUTTON_INSURANCE, callback_data=INSURANCE))
    # keyboard.add(InlineKeyboardButton(BUTTON_OTHER_QUESTION, callback_data=OTHER_QUESTION))
    return keyboard


# ------------------------------------- subcategories  ------------------------------------- #


def subcategory_order() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(BUTTON_HOW_TO_ORDER_TOUR, callback_data=HOW_TO_ORDER_TOUR))
    keyboard.add(InlineKeyboardButton(BUTTON_HOW_TO_CHANGE_ORDER, callback_data=HOW_TO_CHANGE_ORDER))
    keyboard.add(InlineKeyboardButton(BUTTON_HOTEL_CHOICE_PACKAGE, callback_data=HOTEL_CHOICE_PACKAGE))
    keyboard.add(InlineKeyboardButton(BUTTON_CAN_ORDER_INDIVIDUAL_TOUR, callback_data=CAN_ORDER_INDIVIDUAL_TOUR))
    return keyboard


def subcategory_price() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(BUTTON_WHAT_PAYMENT_METHODS, callback_data=WHAT_PAYMENT_METHODS))
    keyboard.add(InlineKeyboardButton(BUTTON_ARE_THERE_EXTRA_FEES, callback_data=ARE_THERE_EXTRA_FEES))
    keyboard.add(InlineKeyboardButton(BUTTON_CAN_GET_DISCOUNT, callback_data=CAN_GET_DISCOUNT))
    keyboard.add(InlineKeyboardButton(BUTTON_HOW_TO_GET_TOUR_ON_CREDIT, callback_data=HOW_TO_GET_TOUR_ON_CREDIT))
    return keyboard


def subcategory_transport() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(BUTTON_WHICH_AIRLINES, callback_data=WHICH_AIRLINES))
    keyboard.add(InlineKeyboardButton(BUTTON_IS_THERE_AIRPORT_TRANSFER, callback_data=IS_THERE_AIRPORT_TRANSFER))
    keyboard.add(InlineKeyboardButton(BUTTON_HOW_TO_CHANGE_FLIGHT_DATE, callback_data=HOW_TO_CHANGE_FLIGHT_DATE))
    return keyboard


def subcategory_rent() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(BUTTON_CAN_CHOOSE_ROOM, callback_data=CAN_CHOOSE_ROOM))
    keyboard.add(InlineKeyboardButton(BUTTON_IS_THERE_DIET_FOOD, callback_data=IS_THERE_DIET_FOOD))
    return keyboard


def subcategory_additional() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(BUTTON_WHICH_EXCURSIONS_INCLUDED, callback_data=WHICH_EXCURSIONS_INCLUDED))
    keyboard.add(
        InlineKeyboardButton(BUTTON_HOW_TO_ORDER_EXTRA_EXCURSIONS, callback_data=HOW_TO_ORDER_EXTRA_EXCURSIONS))
    keyboard.add(InlineKeyboardButton(BUTTON_DO_YOU_HAVE_RENTAL_EQUIPMENT, callback_data=DO_YOU_HAVE_RENTAL_EQUIPMENT))
    return keyboard


def subcategory_guarantee() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(BUTTON_DO_NEED_TRAVEL_INSURANCE, callback_data=DO_NEED_TRAVEL_INSURANCE))
    keyboard.add(InlineKeyboardButton(BUTTON_WHAT_RISKS_ARE_COVERED, callback_data=WHAT_RISKS_ARE_COVERED))
    keyboard.add(
        InlineKeyboardButton(BUTTON_HOW_TO_ASK_FOR_INSURANCE_HELP, callback_data=HOW_TO_ASK_FOR_INSURANCE_HELP))
    return keyboard
