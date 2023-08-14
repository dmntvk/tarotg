from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_card3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Начать', callback_data='card_start3'),
    ]
])

next_card = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту настоящего', callback_data='today_card'),
    ]
])

n_card = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту будущего', callback_data='next_card'),
    ]
])

start_love = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Начать', callback_data='start_love'),
    ]
])

two_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту представляющая вашего партнера', callback_data='two_cards'),
    ]
])

the_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту подключения', callback_data='the_cards'),
    ]
])

fo_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту силы ваших отношений', callback_data='fo_cards'),
    ]
])

fiv_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать карту слабых мест ваших отношений', callback_data='fiv_cards'),
    ]
])

six_cards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Показать вашу настоящую любовную карту', callback_data='six_cards'),
    ]
])

b_up_menu = InlineKeyboardMarkup(inline_keyboard=
                                 [
                                     [
                                    InlineKeyboardButton('10₽', callback_data='10'),
                                     InlineKeyboardButton('25₽', callback_data='25'),
                                     InlineKeyboardButton('50₽', callback_data='50'),
                                     ],
                                        [
                                           InlineKeyboardButton('100₽', callback_data='100'),
                                           InlineKeyboardButton('250₽', callback_data='250'),
                                           InlineKeyboardButton('500₽', callback_data='500'),
                                       ]
                                 ]
)


def oplata(isUrl=True, url='', bill=''):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        oplata_link = InlineKeyboardButton(text='Оплатить', url=url)
        qiwiMenu.insert(oplata_link)
    btncheckQiwi = InlineKeyboardButton(text='Проверить оплату', callback_data='check_'+bill)
    qiwiMenu.insert(btncheckQiwi)
    cancel = InlineKeyboardButton(text='Отменить оплату', callback_data='cancel'+bill)
    qiwiMenu.insert(cancel)
    return qiwiMenu


sub_menu = InlineKeyboardMarkup(inline_keyboard=
                                [
                                    [
                                        InlineKeyboardButton('Подписаться!', url='https://t.me/tarotvisions')
                                    ],
                                    [
                                        InlineKeyboardButton('Проверить подписку!', callback_data='checks_sub')
                                    ]
                                ])