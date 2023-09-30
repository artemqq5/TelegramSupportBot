from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def categories_all() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton("Замовлення турів", callback_data="Замовлення турів"))
    keyboard.add(InlineKeyboardButton("Оплата та ціни", callback_data="Оплата та ціни"))
    keyboard.add(InlineKeyboardButton("Транспорт", callback_data="Транспорт"))
    keyboard.add(InlineKeyboardButton("Проживання", callback_data="Проживання"))
    keyboard.add(InlineKeyboardButton("Екскурсії та додаткові послуги", callback_data="Екскурсії та додаткові послуги"))
    keyboard.add(InlineKeyboardButton("Страхування", callback_data="Страхування"))

    return keyboard


# ------------------------------------- subcategories  ------------------------------------- #


def subcategory_order() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton("Як замовити тур?", callback_data="Як замовити тур?"))
    keyboard.add(InlineKeyboardButton("Як змінити замовлення?", callback_data="Як змінити замовлення?"))
    keyboard.add(
        InlineKeyboardButton("Можливість вибору готелю в пакеті", callback_data="Можливість вибору готелю в пакеті"))
    keyboard.add(InlineKeyboardButton("Чи можна замовити індивідуальний тур?",
                                      callback_data="Чи можна замовити індивідуальний тур?"))

    return keyboard


def subcategory_price() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton("Які способи оплати доступні?", callback_data="Які способи оплати доступні?"))
    keyboard.add(
        InlineKeyboardButton("Чи є додаткові збори чи податки?", callback_data="Чи є додаткові збори чи податки?"))
    keyboard.add(InlineKeyboardButton("Які способи оплати доступні?", callback_data="Які способи оплати доступні?"))
    keyboard.add(InlineKeyboardButton("Чи можна отримати знижку?", callback_data="Чи можна отримати знижку?"))
    keyboard.add(InlineKeyboardButton("Як взяти тур в кредит?", callback_data="Як взяти тур в кредит?"))

    return keyboard


def subcategory_transport() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton("Які авіакомпанії ви використовуєте?",
                                      callback_data="Які авіакомпанії ви використовуєте?"))
    keyboard.add(
        InlineKeyboardButton("Чи є трансфер від/до аеропорту?", callback_data="Чи є трансфер від/до аеропорту?"))
    keyboard.add(InlineKeyboardButton("Як змінити дату вильоту?", callback_data="Як змінити дату вильоту?"))

    return keyboard


def subcategory_rent() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton("Чи можна вибрати номер в готелі?", callback_data="Чи можна вибрати номер в готелі?"))
    keyboard.add(InlineKeyboardButton("Чи є можливість дієтичного харчування?",
                                      callback_data="Чи є можливість дієтичного харчування?"))

    return keyboard


def subcategory_additional() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton("Які екскурсії входять у вартість туру?",
                                      callback_data="Які екскурсії входять у вартість туру?"))
    keyboard.add(
        InlineKeyboardButton("Як замовити додаткові екскурсії?", callback_data="Як замовити додаткові екскурсії?"))
    keyboard.add(
        InlineKeyboardButton("Чи є у вас прокат спорядження (наприклад, для підводного плавання)?",
                             callback_data="Чи є у вас прокат спорядження (наприклад, для підводного плавання)?"))

    return keyboard


def subcategory_guarantee() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(InlineKeyboardButton("Чи потрібно оформляти страхування для подорожі?",
                                      callback_data="Чи потрібно оформляти страхування для подорожі?"))
    keyboard.add(
        InlineKeyboardButton("Які ризики покриває страхування?", callback_data="Які ризики покриває страхування?"))
    keyboard.add(InlineKeyboardButton("Як звернутися за допомогою за страховим випадком?",
                                      callback_data="Як звернутися за допомогою за страховим випадком?"))

    return keyboard
