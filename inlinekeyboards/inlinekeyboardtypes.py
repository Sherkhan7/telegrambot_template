from .inlinekeyboardvariables import *

inline_keyboard_types = {

    book_keyboard: {
        "uz": {1: "Kitob haqida", 2: "Buyurtma qilish", 3: "Ortga"},
    },

    confirm_keyboard: {
        "uz": ["Tasdiqlash", "Buyurtmani bekor qilish"],
        "cy": ["Тасдиқлаш", "Таҳрирлаш"],
        "ru": ["Подтвердить", "Редактировать"],
    },

    order_keyboard: {
        "uz": {1: "Buyurtma berish", 2: "Ortga"},
        "cy": {
            1: "Манзилни таҳрирлаш",
            2: "Юк маълумотларини таҳрирлаш",
            3: "Кун ва вақтни таҳрирлаш",
            4: "Таҳрирни якунлаш",
        },
        "ru": {
            1: "Редактировать адрес",
            2: "Редактировать информацию о грузе",
            3: "Редактировать дату и время",
            4: "Закончить редактирование",

        },
    },

    orders_keyboard: {
        "uz": {1: "Qabul qilish", 2: "Rad etish"},
        "cy": {
            1: "Манзилни таҳрирлаш",
            2: "Юк маълумотларини таҳрирлаш",
            3: "Кун ва вақтни таҳрирлаш",
            4: "Таҳрирни якунлаш",
        },
        "ru": {
            1: "Редактировать адрес",
            2: "Редактировать информацию о грузе",
            3: "Редактировать дату и время",
            4: "Закончить редактирование",

        },
    },

    yes_no_keyboard: {
        "uz": {1: "Ha", 2: "Yo'q"}
    },

    basket_keyboard: {
        "uz": {1: "Buyurtmani davom ettirish", 2: "Buyurtmani tasdiqlash"},
        "cy": ["Эълонни ёпиш", "Эълонни қайта очиш", "Эълонни қайта очилди"],
        "ru": ["Закрыть объявление", "Повторно открыть объявление", "Объявление было повторно открыто"],

    },

    delivery_keyboard: {
        "uz": ["Yetkazib berildi"]
    }
}
