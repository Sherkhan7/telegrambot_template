from DB import get_main_menu_buttons
from telegram import ReplyKeyboardMarkup, KeyboardButton
from .replykeyboardtypes import *


class ReplyKeyboard(object):

    def __init__(self, keyb_type, lang):

        self.__type = keyb_type
        self.__lang = lang

        self.__keyboard = self.__create_reply_keyboard(self.__type, self.__lang)

    def __create_reply_keyboard(self, keyb_type, lang):

        if keyb_type == main_menu_keyboard:
            return self.__get_main_menu_keyboard(get_main_menu_buttons(), lang)

        elif keyb_type == settings_keyboard:
            return self.__get_settings_keyboard(reply_keyboard_types[keyb_type], lang)

        elif keyb_type == phone_number_keyboard:
            return self.__get_phone_number_keyboard(reply_keyboard_types[keyb_type], lang)

        elif keyb_type == location_keyboard:
            return self.__get_location_keyboard(reply_keyboard_types[keyb_type], lang)

        elif keyb_type == passenger_mail_keyboard:
            return self.__get_passenger_mail_keyboard(reply_keyboard_types[keyb_type], lang)

    @staticmethod
    def __get_main_menu_keyboard(buttons, lang):

        return ReplyKeyboardMarkup([
            [
                KeyboardButton(f'{buttons[0]["icon"]} {buttons[0][f"text_{lang}"]}'),
                KeyboardButton(f'{buttons[1]["icon"]} {buttons[1][f"text_{lang}"]}')
            ],
            [
                KeyboardButton(f'{buttons[2]["icon"]} {buttons[2][f"text_{lang}"]}'),
                KeyboardButton(f'{buttons[3]["icon"]} {buttons[3][f"text_{lang}"]}')
            ],

        ], resize_keyboard=True)

    @staticmethod
    def __get_settings_keyboard(buttons, lang):

        return ReplyKeyboardMarkup([
            [
                KeyboardButton(f'{buttons[0]["icon"]} {buttons[0][f"text_{lang}"]}'),
                KeyboardButton(f'{buttons[1]["icon"]} {buttons[1][f"text_{lang}"]}')
            ],
            [KeyboardButton(f'{buttons[2]["icon"]} {buttons[2][f"text_{lang}"]}')],

        ], resize_keyboard=True)

    @staticmethod
    def __get_phone_number_keyboard(buttons, lang):

        return ReplyKeyboardMarkup([
            [KeyboardButton(f'{buttons[0]["icon"]} {buttons[0][f"text_{lang}"]}', request_contact=True)]
        ], resize_keyboard=True)

    @staticmethod
    def __get_location_keyboard(buttons, lang):

        return ReplyKeyboardMarkup([
            [KeyboardButton(f'{buttons[0]["icon"]} {buttons[0][f"text_{lang}"]}', request_location=True)],
        ], resize_keyboard=True)

    @staticmethod
    def __get_passenger_mail_keyboard(buttons, lang):

        return ReplyKeyboardMarkup([

            [
                KeyboardButton(f'{buttons[0]["icon"]} {buttons[0][f"text_{lang}"]}'),
                KeyboardButton(f'{buttons[1]["icon"]} {buttons[1][f"text_{lang}"]}')
            ],
            [
                KeyboardButton(f'{buttons[2]["icon"]} {buttons[2][f"text_{lang}"]}'),
                KeyboardButton(f'{buttons[3]["icon"]} {buttons[3][f"text_{lang}"]}')
            ],
            [
                KeyboardButton(f'{buttons[4]["icon"]} {buttons[4][f"text_{lang}"]}'),
                KeyboardButton(f'{buttons[5]["icon"]} {buttons[5][f"text_{lang}"]}')
            ],

        ], resize_keyboard=True)

    def get_keyboard(self):
        return self.__keyboard
