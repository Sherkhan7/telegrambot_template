from globalvariables import *

BOOK_DICT = {
    "uz": {
        TITLE_TEXT: "Kitob nomi",
        AUTHOR_TEXT: "Muallif(lar)",
        AMOUNT_TEXT: "Hajmi",
        LANG_TEXT: "Til",
        TRANSLATOR_TEXT: "Tarjimon(lar)",
        COVER_TYPE_TEXT: "Muqovasi",
        PRICE_TEXT: "Narxi",
        YEAR_TEXT: "Yil",
    },
    "ru": {
        TITLE_TEXT: "Откуда",
        AUTHOR_TEXT: "Куда",
        AMOUNT_TEXT: "Вес груза",
        LANG_TEXT: "Объем груза",
        TRANSLATOR_TEXT: "Описание груза",
        INSCRIPTION_TEXT: "Дата отправки груза",
        COVER_TYPE_TEXT: "Время отправки груза",
        PRICE_TEXT: "сейчас",
        YEAR_TEXT: "Объявитель",
        USER_PHONE_NUMBER_TEXT: "Тел номер",
        STATUS_TEXT: "Статус",
        OPENED_STATUS: "объявление открыто",
        CLOSED_STATUS: "объявление закрыто",
        NOT_CONFIRMED_STATUS: "объявление не подтверждено",
        TG_ACCOUNT_TEXT: "Telegram аккаунт",
        UNDEFINED_TEXT: "неизвестно",
        ADDRESS: 'nameRu'
    },
    "cy": {
        TITLE_TEXT: "Қаердан",
        AUTHOR_TEXT: "Қаерга",
        AMOUNT_TEXT: "Юк оғирлиги",
        LANG_TEXT: "Юк ҳажми",
        TRANSLATOR_TEXT: "Юк тавсифи",
        INSCRIPTION_TEXT: "Юкни жўнатиш куни",
        COVER_TYPE_TEXT: "Юкни жўнатиш вақти",
        PRICE_TEXT: "ҳозир",
        YEAR_TEXT: "Эълон берувчи",
        USER_PHONE_NUMBER_TEXT: "Тел номер",
        STATUS_TEXT: "Статус",
        OPENED_STATUS: "эълон очиқ",
        CLOSED_STATUS: "эълон ёпилган",
        NOT_CONFIRMED_STATUS: "эълон тасдиқланмаган",
        TG_ACCOUNT_TEXT: "Телеграм аккаунт",
        UNDEFINED_TEXT: "номаълум",
        ADDRESS: 'nameCy'
    }
}

# USER_INFO_LAYOUT_DICT = {
#     'uz': {
#         NAME: "Ism",
#         SURNAME: "Familya",
#         PHONE_NUMBER: "Tel"
#     },
#     'cy': {
#         NAME: "Исм",
#         SURNAME: "Фамиля",
#         PHONE_NUMBER: "Тел"
#     },
#     'ru': {
#         NAME: "Имя",
#         SURNAME: "Фамилия",
#         PHONE_NUMBER: "Тел"
#     }
# }

PHONE_NUMBER_LAYOUT_DICT = {
    "uz": {
        1: "Telefon raqamini quyidagi shaklda yuboring",
        2: "Misol",
        3: "yoki",
    },
    "cy": {
        1: "Телефон рақамини қуйидаги шаклда юборинг",
        2: "Мисол",
        3: "ёки",
    },
    "ru": {
        1: "Отправьте номер телефона в виде ниже",
        2: "Папример",
        3: "или",
    }
}
