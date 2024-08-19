from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

from bot.conustant import (ORDERS, MY_ORDERS, OPERATOR, SETTINGS, WEB_ORDERS,
                           BACK, LANG_CHANGE, LOCATION,
                           SETTINGS_RU,
                           OPERATOR_RU, ORDERS_RU, MY_ORDERS_RU, WEB_ORDERS)

# from aiogram.utils.i18n import gettext as _


def main_menu():
    kb = [
        [KeyboardButton(text=ORDERS), KeyboardButton(text=MY_ORDERS)],
        [KeyboardButton(text=OPERATOR), KeyboardButton(text=SETTINGS)],
        [KeyboardButton(text=WEB_ORDERS)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def main_menu_ru():
    kb = [
        [KeyboardButton(text=ORDERS_RU), KeyboardButton(text=MY_ORDERS_RU)],
        [KeyboardButton(text=OPERATOR_RU), KeyboardButton(text=SETTINGS_RU)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def contact_user():
    kb = [
        [KeyboardButton(text='contact', request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


def location_user():
    kb = [
        [KeyboardButton(text=LOCATION, request_location=True)
         ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def back():
    kb = [
        [KeyboardButton(text=BACK)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def settings():
    kb = [
        [KeyboardButton(text=LANG_CHANGE),
         KeyboardButton(text=BACK)
         ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def lang_change():
    kb = [
        [KeyboardButton(text='🇺🇿'),
         KeyboardButton(text='🇷🇺'), ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


def lang_change_settings():
    kb = [
        [KeyboardButton(text='🇺🇿UZ'),
         KeyboardButton(text='🇷🇺RU'), ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def person():
    kb = [
        [KeyboardButton(text='yuridik shaxs'),
         KeyboardButton(text='jismoniy shaxs'), ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def person_ru():
    kb = [
        [KeyboardButton(text='юридическое лицо'),
         KeyboardButton(text='физическое лицо'), ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def web():
    kb = [
        [KeyboardButton(text='webapp', web_app=WebAppInfo(url='https://bellissimo.uz/')),
         KeyboardButton(text=BACK)]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard
