from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔮️ Вытянуть карты'),
            KeyboardButton(text='☀️ Карта дня'),
        ], [
            KeyboardButton(text='⚙️ Аккаунт'),
        ]
    ], resize_keyboard=True
)

profile_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📥 Пополнить баланс'),
            KeyboardButton(text='🔮️ Вытянуть карты'),
        ],
        [
            KeyboardButton(text='💸️ Промокод')
        ],
        [
            KeyboardButton(text='🤝 Реферальная программа')
        ]
    ], resize_keyboard=True
)

ref_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⚙️ Аккаунт')
        ]
    ], resize_keyboard=True
)

rasclad_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🃏 Одна карта(Лучше всего ответит на один вопрос)'),
            KeyboardButton(text='🃏 Да или нет'),
        ],
        [
            KeyboardButton(text='♣️♦️♠️ Расклад на три карты(прошлое, настоящее, будущее)'),
        ],
        [
            KeyboardButton(text='♥️ Расклад истинная любовь(6 карт)'),
        ],
        [
            KeyboardButton(text='☀️ Карта дня'),
        ],
        [
            KeyboardButton(text='🔙 Назад'),
        ]
    ], resize_keyboard=True
)

faunds_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📥 Пополнить баланс'),
            KeyboardButton(text='⚙️ Аккаунт'),
        ]
    ],     resize_keyboard=True
)

rasclad = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Идет расклад ⌛')
        ]
    ],     resize_keyboard=True
)


amount_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='25'),
            KeyboardButton(text='50'),
        ],
        [
            KeyboardButton(text='100'),
            KeyboardButton(text='250'),
            KeyboardButton(text='500'),
        ],
        [
            KeyboardButton(text='Отменить оплату ❌'),
        ]
    ],     resize_keyboard=True
)

promo_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Назад'),]
    ], resize_keyboard=True
)