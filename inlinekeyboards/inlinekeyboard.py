from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from DB import get_all_books
from .inlinekeyboardtypes import *


class InlineKeyboard(object):
    def __init__(self, keyb_type, lang=None, data=None, history=None):

        self.__type = keyb_type
        self.__lang = lang
        self.__data = data
        self.__history = history
        self.__keyboard = self.__create_inline_keyboard(self.__type, self.__lang, self.__data, self.__history)

    def __create_inline_keyboard(self, keyb_type, lang, data, history):

        if keyb_type == books_keyboard:

            return self.__get_books_keyboard(data)

        elif keyb_type == book_keyboard:

            return self.__get_book_keyboard(inline_keyboard_types[keyb_type][lang], data)

        elif keyb_type == order_keyboard:

            return self.__get_order_keyboard(inline_keyboard_types[keyb_type][lang])

        elif keyb_type == basket_keyboard:

            return self.__get_basket_keyboard(inline_keyboard_types[keyb_type][lang])

        elif keyb_type == confirm_keyboard:

            return self.__get_confirm_keyboard(inline_keyboard_types[keyb_type][lang], data)

        elif keyb_type == orders_keyboard:

            return self.__get_orders_keyboard(inline_keyboard_types[keyb_type][lang], data)

        elif keyb_type == yes_no_keyboard:

            return self.__get_yes_no_keyboard(inline_keyboard_types[keyb_type][lang], data)

        elif keyb_type == delivery_keyboard:

            return self.__get_delivery_keyboard(inline_keyboard_types[keyb_type][lang], data)

        elif keyb_type == paginate_keyboard:

            return self.__get_paginate_keyboard(data, history)

        elif keyb_type == geo_keyboard:

            return self.__get_geo_keyboard(data)

    @staticmethod
    def __get_books_keyboard(data):

        inline_keyboard = [
            [InlineKeyboardButton(f'\U0001F4D5  {book["title"]}', callback_data=f'book_{book["id"]}')]
            for book in get_all_books()
        ]

        if data:
            inline_keyboard.append([InlineKeyboardButton('\U0001F6D2  Savat', callback_data='basket')])

        return InlineKeyboardMarkup(inline_keyboard)

    @staticmethod
    def __get_book_keyboard(buttons, book_data):

        button1_text = f'\U0001F4D6  {buttons[1]}'
        button1_url = book_data['description_url']

        button2_text = f'\U0001F4E6  {buttons[2]}'
        button2_data = 'ordering'

        button3_text = f'\U00002B05  {buttons[3]}'
        button3_data = 'back'

        inline_keyboard = [
            [InlineKeyboardButton(button2_text, callback_data=button2_data)],
            [InlineKeyboardButton(button3_text, callback_data=button3_data)],
        ]

        if book_data['description_url']:
            inline_keyboard.insert(0, [
                InlineKeyboardButton(button1_text, url=button1_url)
            ])

        return InlineKeyboardMarkup(inline_keyboard)

    @staticmethod
    def __get_order_keyboard(buttons):

        button1_text = f'\U0001F6D2  {buttons[1]}'
        button1_data = f'order'

        button2_text = f'\U00002B05  {buttons[2]}'
        button2_data = 'back'

        minus_sign = '\U00002796'
        pilus_sign = '\U00002795'

        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f'{minus_sign}', callback_data='-'),
                    InlineKeyboardButton('1', callback_data='1'),
                    InlineKeyboardButton(f'{pilus_sign}', callback_data='+'),
                ],

                [InlineKeyboardButton(button1_text, callback_data=button1_data)],

                [InlineKeyboardButton(button2_text, callback_data=button2_data)],
            ]
        )

    @staticmethod
    def __get_basket_keyboard(buttons):

        button1_text = f'\U0001F501  {buttons[1]}'
        button1_data = 'continue'

        button2_text = f'\U00002705  {buttons[2]}'
        button2_data = 'confirmation'

        return InlineKeyboardMarkup([

            [InlineKeyboardButton(button1_text, callback_data=button1_data)],
            [InlineKeyboardButton(button2_text, callback_data=button2_data)]
        ])

    @staticmethod
    def __get_confirm_keyboard(buttons, data):

        inline_keyboard = []
        button1_text = f'\U0001F4CD Geolokatsiyam'

        if data:
            from_latitude = data['latitude']
            from_longitude = data['longitude']
            inline_keyboard.append(
                [InlineKeyboardButton(button1_text,
                                      url=f'http://www.google.com/maps/place/{from_latitude},{from_longitude}/'
                                          f'@{from_latitude},{from_longitude},12z')])

        button2_text = f'\U00002705 {buttons[0]}'
        button2_data = 'confirm'

        button3_text = f'\U0000274C {buttons[1]}'
        button3_data = 'cancel'

        inline_keyboard.extend([
            [InlineKeyboardButton(button2_text, callback_data=button2_data)],
            [InlineKeyboardButton(button3_text, callback_data=button3_data)]
        ])

        return InlineKeyboardMarkup(inline_keyboard)

    @staticmethod
    def __get_orders_keyboard(buttons, data):

        inline_keyboard = []
        button1_text = f"\U0001F3C1 Manzilni xaritadan ko'rish"

        if data[0]:
            from_latitude = data[0]['latitude']
            from_longitude = data[0]['longitude']
            inline_keyboard.append(
                [InlineKeyboardButton(button1_text,
                                      url=f'http://www.google.com/maps/place/{from_latitude},{from_longitude}/'
                                          f'@{from_latitude},{from_longitude},12z')])

        button2_text = f'\U00002705 {buttons[1]}'
        button3_text = f'\U0000274C {buttons[2]}'

        inline_keyboard.extend([
            [InlineKeyboardButton(button2_text, callback_data=f'r_{data[-1]}')],
            [InlineKeyboardButton(button3_text, callback_data=f'c_{data[-1]}')]
        ])

        return InlineKeyboardMarkup(inline_keyboard)

    @staticmethod
    def __get_geo_keyboard(data):
        button2_text = f"\U0001F3C1 Manzilni xaritadan ko'rish"

        from_latitude = data['latitude']
        from_longitude = data['longitude']

        return InlineKeyboardMarkup([
            [InlineKeyboardButton(button2_text,
                                  url=f'http://www.google.com/maps/place/{from_latitude},{from_longitude}/'
                                      f'@{from_latitude},{from_longitude},12z')]
        ])

    @staticmethod
    def __get_yes_no_keyboard(buttons, data):

        return InlineKeyboardMarkup([

            [
                InlineKeyboardButton('\U00002705  ' + buttons[1], callback_data=f'{data[0]}_y_{data[-1]}'),
                InlineKeyboardButton('\U0000274C  ' + buttons[2], callback_data=f'{data[0]}_n_{data[-1]}')
            ],
        ])

    @staticmethod
    def __get_delivery_keyboard(buttons, order_id):

        return InlineKeyboardMarkup([
            [InlineKeyboardButton(buttons[0], callback_data=f'd_{order_id}')],
        ])

    @staticmethod
    def __get_paginate_keyboard(data, history=None):

        wanted, orders = data
        length = len(orders)

        state = 'h_' if history else ''

        if wanted == 1 and length == 1:
            button1_text = '.'
            button1_data = 'dot_1'

            button3_text = '.'
            button3_data = 'dot_2'

        elif wanted == 1 and length > 1:
            button1_text = '.'
            button1_data = 'dot'

            button3_text = '\U000023E9'
            button3_data = f'{state}w_{wanted + 1}'

        elif wanted == length:
            button1_text = '\U000023EA'
            button1_data = f'{state}w_{wanted - 1}'

            button3_text = '.'
            button3_data = 'dot'

        else:
            button1_text = '\U000023EA'
            button1_data = f'{state}w_{wanted - 1}'

            button3_text = '\U000023E9'
            button3_data = f'{state}w_{wanted + 1}'

        button2_text = f'{wanted}/{length}'
        button2_data = 'None'

        return InlineKeyboardMarkup([
            [
                InlineKeyboardButton(button1_text, callback_data=button1_data),
                InlineKeyboardButton(button2_text, callback_data=button2_data),
                InlineKeyboardButton(button3_text, callback_data=button3_data),
            ],
        ])

    def get_keyboard(self):

        return self.__keyboard
