from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram import Update, ParseMode, InlineKeyboardMarkup
from config import ACTIVE_ADMINS
from DB import *

from helpers import wrap_tags, set_user_data
from inlinekeyboards import InlineKeyboard
from inlinekeyboards.inlinekeyboardvariables import *
from globalvariables import *

import json
import re
import logging

logger = logging.getLogger()


def inline_keyboards_handler_callback(update: Update, context: CallbackContext):
    # with open('jsons/callback_query.json', 'w') as callback_query_file:
    #     callback_query_file.write(callback_query.to_json())
    user_data = context.user_data
    set_user_data(update.effective_user.id, user_data)
    user = user_data['user_data']

    callback_query = update.callback_query
    data = callback_query.data

    if user[IS_ADMIN] and user[TG_ID] in ACTIVE_ADMINS:

        match_obj = re.search(r'^[rc]_\d+$', data)
        match_obj_2 = re.search(r'[rc]_[yn]_\d+$', data)
        match_obj_3 = re.search(r'^w_\d+$', data)
        match_obj_4 = re.search(r'^h_w_\d+$', data)

        new_text = ''

        if match_obj or match_obj_2:

            if match_obj:
                data = match_obj.string.split('_')
                keyboard = yes_no_keyboard

            elif match_obj_2:
                data = match_obj_2.string.split('_')
                order = get_order(data[-1])

                geo = json.loads(order[GEOLOCATION]) if order[GEOLOCATION] else None

                if data[1] == 'n':
                    keyboard = orders_keyboard
                    data = [geo, data[-1]]

                elif data[1] == 'y':

                    status = 'canceled' if data[0] == 'c' else 'received'

                    if order[STATUS] == 'waiting':
                        update_result = update_order_status(status, data[-1])
                        status_text = 'rad etilgan' if status == 'canceled' else 'qabul qilingan'

                        if update_result:
                            client_text = 'Buyurtma rad qilindi.' if status == 'canceled' else 'Buyurtma qabul qilindi.'
                            client_text = wrap_tags(client_text) + f' [ \U0001F194 {order[ID]} ]'

                            if status == 'received':
                                client_text += '\nBuyurtma yetkazilganidan keyin ' \
                                               f'{wrap_tags("Yetkazib berildi")} tugmasini bosing.\n'
                                inline_keyboard = InlineKeyboard(delivery_keyboard, user[LANG],
                                                                 data=data[-1]).get_keyboard()
                            else:
                                inline_keyboard = None

                            context.bot.send_message(order[USER_TG_ID], client_text, parse_mode=ParseMode.HTML,
                                                     reply_to_message_id=order[MESSAGE_ID],
                                                     reply_markup=inline_keyboard)

                    elif order[STATUS] == 'received':
                        status_text = 'buyurtma avval qabul qilingan !'

                    elif order[STATUS] == 'delivered':
                        status_text = 'buyurtma avval yetkazilgan !'

                    elif order[STATUS] == 'canceled':
                        status_text = 'buyurtma avval rad qilingan !'

                    data, keyboard = (geo, geo_keyboard) if geo else (None, None)

                    new_text = callback_query.message.text_html.split('\n')
                    new_text[0] = ' '.join(new_text[0].split()[:2])
                    new_text[-1] = f'Status: {wrap_tags(status_text)}'
                    new_text = '\n'.join(new_text)

            callback_query.answer()

            if new_text:
                if keyboard:
                    inline_keyboard = InlineKeyboard(keyboard, user[LANG], data=data).get_keyboard()
                else:
                    inline_keyboard = None

                callback_query.edit_message_text(new_text, reply_markup=inline_keyboard, parse_mode=ParseMode.HTML)

            else:

                inline_keyboard = InlineKeyboard(keyboard, user[LANG], data=data).get_keyboard()
                callback_query.edit_message_reply_markup(inline_keyboard)

        elif match_obj_3 or match_obj_4:

            if match_obj_4:
                orders_list = get_orders_by_status(('delivered', 'canceled'))
                history = True
                label = '[Tarix]'

            else:
                orders_list = get_orders_by_status('received')
                history = None
                label = ''

            if orders_list:
                wanted = int(data.split('_')[-1])
                if wanted > len(orders_list):
                    wanted = 1

                order = orders_list[wanted - 1]
                status = 'yetkazilgan' if order[STATUS] == 'delivered' else 'rad etilgan' \
                    if order[STATUS] == 'canceled' else 'qabul qilingan'
                order_itmes = get_order_items(order[ID])
                new_dict = dict()

                for item in order_itmes:
                    new_dict.update({item['book_id']: item['quantity']})

                books_ids = [str(item['book_id']) for item in order_itmes]
                books = get_books(books_ids)
                books_text = ''

                for book in books:
                    books_text += f'Kitob nomi: {wrap_tags(book[TITLE])}\n' \
                                  f'Soni: {wrap_tags(str(new_dict[book[ID]]) + " ta")}' \
                                  f'\n{wrap_tags("".ljust(22, "-"))}\n\n'
                inline_keyboard = InlineKeyboard(paginate_keyboard, user[LANG], data=[wanted, orders_list],
                                                 history=history).get_keyboard()

                if order[GEOLOCATION]:
                    geo = json.loads(order[GEOLOCATION])
                    inline_keyboard = inline_keyboard.inline_keyboard
                    keyboard = InlineKeyboard(geo_keyboard, data=geo).get_keyboard().inline_keyboard
                    inline_keyboard += keyboard
                    inline_keyboard = InlineKeyboardMarkup(inline_keyboard)

                if order['with_action']:
                    label += "[🔥MEGA AKSIYA(5 + 1)🔥]"

                client = get_user(order[USER_ID])

                text = [
                    f'\U0001F194 {order[ID]} {label}\n',
                    f'Status: {wrap_tags(status)}',
                    f'Yaratilgan vaqti: {wrap_tags(order["created_at"].strftime("%d-%m-%Y %X"))}\n',
                    f'Ism: {wrap_tags(client[FULLNAME])}',
                    f'Tel: {wrap_tags(order[PHONE_NUMBER])}',
                    f'Telegram: {wrap_tags("@" + client[USERNAME])}' if client[USERNAME] else ''
                    # f'Manzil: {order["address"]}',
                ]

                text = '\n'.join(text)
                text += f'\n\n{books_text}'
                callback_query.answer()
                callback_query.edit_message_text(text, reply_markup=inline_keyboard, parse_mode=ParseMode.HTML)

            else:
                text = "Tarix bo'limiga o'ting !"

                callback_query.edit_message_text(text)

        else:
            callback_query.answer()

    elif not user[IS_ADMIN]:

        match_obj = re.search(r'^w_\d+$', data)
        match_obj_2 = re.search(r'^d_\d+$', data)
        callback_query.answer()

        if match_obj:

            wanted = int(match_obj.string.split('_')[-1])
            user_orders = get_user_orders(user[ID])
            order = user_orders[wanted - 1]
            order_itmes = get_order_items(order[ID])
            new_dict = dict()
            books_ids = []
            books_text = ''
            label = ''
            if order['with_action']:
                label = "[🔥MEGA AKSIYA(5 + 1)🔥]"

            for item in order_itmes:
                new_dict.update({item['book_id']: item['quantity']})
                books_ids += [str(item['book_id'])]

            books = get_books(books_ids)
            for book in books:
                books_text += f'Kitob nomi: {wrap_tags(book[TITLE])}\n' \
                              f'Soni: {wrap_tags(str(new_dict[book[ID]]) + " ta")}' \
                              f'\n{wrap_tags("".ljust(22, "-"))}\n\n'

            status = 'qabul qilingan' if order[STATUS] == 'received' else 'rad etilgan' \
                if order[STATUS] == 'canceled' else 'qabul qilish kutilmoqda' \
                if order[STATUS] == 'waiting' else 'yetkazilgan'

            text = [
                f'\U0001F194 {order[ID]} {label}\n',
                f'Status: {wrap_tags(status)}',
                f'Yaratilgan vaqti: {wrap_tags(order["created_at"].strftime("%d-%m-%Y %X"))}'
            ]
            text = '\n'.join(text)
            text += f'\n\n{books_text}'

            inline_keyboard = InlineKeyboard(paginate_keyboard, user[LANG], data=[wanted, user_orders]) \
                .get_keyboard()

            if order[STATUS] == 'received':
                deliv_keyb = InlineKeyboard(delivery_keyboard, user[LANG], data=order[ID]).get_keyboard()
                pag_keyb = inline_keyboard.inline_keyboard
                deliv_keyb = deliv_keyb.inline_keyboard
                inline_keyboard = InlineKeyboardMarkup(pag_keyb + deliv_keyb)

            callback_query.edit_message_text(text, reply_markup=inline_keyboard, parse_mode=ParseMode.HTML)

        elif match_obj_2:

            order_id = data.split('_')[-1]
            status = 'delivered'
            update_order_status(status, order_id)

            status = 'yetkazilgan'
            text = callback_query.message.text_html.split('\n')

            if len(callback_query.message.reply_markup.inline_keyboard) == 1:
                text += [
                    f'\nStatus: {wrap_tags(status)}'
                ]
                text = '\n'.join(text)

                callback_query.edit_message_text(text, parse_mode=ParseMode.HTML)

            else:

                text[2] = f'Status: {wrap_tags(status)}'
                text = '\n'.join(text)
                inline_keyboard = InlineKeyboardMarkup([callback_query.message.reply_markup.inline_keyboard[0]])

                callback_query.edit_message_text(text, reply_markup=inline_keyboard, parse_mode=ParseMode.HTML)

    else:
        callback_query.answer("Siz aktiv admin emassiz !!!\n"
                              "Siz siz bu operatsiyani bajara olmaysiz !!!\n\n"
                              "\U00002639\U00002639\U00002639\U00002639\U00002639", show_alert=True)

    # logger.info('user_data: %s', user_data)


callback_query_handler = CallbackQueryHandler(inline_keyboards_handler_callback)
