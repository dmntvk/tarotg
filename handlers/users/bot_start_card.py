import time

from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import rasclad_menu, start_menu, faunds_menu, rasclad
from keyboards.inline.inline_menu import start_card3, next_card, n_card, start_love, two_cards, the_cards, fo_cards, fiv_cards, six_cards, sub_menu
from utils.dbapi import quick_commands
from states.quests import Quests
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io


# Функции по картам
async def card(my_card, bools):
    if bools == True:
        # загрузка картинки
        img = Image.open('card_pics/fon.png')
        cards = Image.open(f'card_pics/{my_card.card_pic}')

        cards = cards.resize((302, 436))

        # Работа с текстом
        font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                  size=14)
        font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                       size=18)
        font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                     size=12)
        wrapper = textwrap.TextWrapper(width=50)
        name = f'Эта карта {my_card.card_name}'
        crt_zn = 'Краткое значение карты:'
        zn = f'{my_card.card_cratc}'
        texts = f'Карта указывает на {my_card.card_zn}'
        word_list = wrapper.wrap(text=texts)
        text_new = ''
        t = 0
        for ii in word_list[:-1]:
            t = t + 1
            text_new = text_new + ii + '\n'

        text_new += word_list[-1]
        draw_text = ImageDraw.Draw(img)

        W, H = img.size
        w, h = draw_text.textsize(text_new, font=font)
        if t >= 17:
            x, y = 0.50 * (W - w), 530
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=11)
            wrapper = textwrap.TextWrapper(width=75)
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'
        if 16 >= t >= 11:
            x, y = 0.50 * (W - w), 0.90 * (H - h)
        if 10 >= t >= 7:
            x, y = 0.50 * (W - w), 0.80 * (H - h)
        if t <= 6:
            x, y = 0.50 * (W - w), 0.70 * (H - h)
        draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

        w, h = draw_text.textsize(name, font=font_name)
        xx, yy = 0.50 * (W - w), 0.53 * H - h
        draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

        w, h = draw_text.textsize(crt_zn, font=font_name)
        xxx, yyy = 0.50 * (W - w), 0.56 * H - h
        draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

        w, h = draw_text.textsize(zn, font=font_cr)
        xxxx, yyyy = 0.50 * (W - w), 0.58 * H - h
        draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

        img.paste(cards, (107, 5), cards)
        photo = io.BytesIO()
        img.save(photo, format='PNG')
        photo.seek(0)
        return photo

    if bools == False:
        img = Image.open('card_pics/fon.png')
        cards = Image.open(f'card_pics/{my_card.card_pic}')
        cards = cards.resize((302, 436))
        cards = cards.rotate(180)

        # Работа с текстом
        font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',size=14)
        font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',size=18)
        font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',size=12)
        wrapper = textwrap.TextWrapper(width=50)
        name = f'Эта карта {my_card.card_name}(Перевернутая)'
        crt_zn = 'Краткое значение карты:'
        zn = f'{my_card.card_cratc_obr}'
        texts = f'Перевернутая карта указывает на {my_card.card_obzn}'
        word_list = wrapper.wrap(text=texts)
        text_new = ''
        t = 0
        for ii in word_list[:-1]:
            t = t + 1
            text_new = text_new + ii + '\n'

        text_new += word_list[-1]
        draw_text = ImageDraw.Draw(img)

        W, H = img.size
        w, h = draw_text.textsize(text_new, font=font)
        if t >= 17:
            x, y = 0.50 * (W - w), 530
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=11)
            wrapper = textwrap.TextWrapper(width=75)
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'
        if 16 >= t >= 11:
            x, y = 0.50 * (W - w), 0.90 * (H - h)
        if 10 >= t >= 7:
            x, y = 0.50 * (W - w), 0.80 * (H - h)
        if t <= 6:
            x, y = 0.50 * (W - w), 0.70 * (H - h)
        draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

        w, h = draw_text.textsize(name, font=font_name)
        xx, yy = 0.50 * (W - w), 0.53 * H - h
        draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

        w, h = draw_text.textsize(crt_zn, font=font_name)
        xxx, yyy = 0.50 * (W - w), 0.56 * H - h
        draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

        w, h = draw_text.textsize(zn, font=font_cr)
        xxxx, yyyy = 0.50 * (W - w), 0.58 * H - h
        draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

        img.paste(cards, (107, 5), cards)
        photo = io.BytesIO()
        img.save(photo, format='PNG')
        photo.seek(0)
        return photo


async def yes_not(my_card, voprs):
    # загрузка картинки
    img = Image.open('card_pics/fon.png')
    cards = Image.open(f'card_pics/{my_card.card_pic}')
    cards = cards.resize((302, 436))

    # Работа с текстом
    font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
    font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
    font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
    wrapper = textwrap.TextWrapper(width=50)
    name = f'Эта карта {my_card.card_name}'
    crt_zn = 'Краткое значение карты:'
    zn = f'{my_card.card_cratc}'
    onv = 'Ответ на ваш вопрос'
    vopr = 'Ваш вопрос'
    vopros = f'{voprs}'
    texts = f'{my_card.yes_no}'
    word_list = wrapper.wrap(text=texts)
    text_new = ''
    t = 0
    for ii in word_list[:-1]:
        t = t + 1
        text_new = text_new + ii + '\n'

    text_new += word_list[-1]
    draw_text = ImageDraw.Draw(img)

    # Отображение текста
    W, H = img.size
    w, h = draw_text.textsize(text_new, font=font)
    if 16 >= t >= 11:
        x, y = 0.50 * (W - w), 0.90 * (H - h)
    if 10 >= t >= 7:
        x, y = 0.50 * (W - w), 0.84 * (H - h)
    if t <= 6:
        x, y = 0.50 * (W - w), 0.78 * (H - h)
    draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

    w, h = draw_text.textsize(name, font=font_name)
    xx, yy = 0.50 * (W - w), 0.53 * H - h
    draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

    w, h = draw_text.textsize(crt_zn, font=font_name)
    xxx, yyy = 0.50 * (W - w), 0.56 * H - h
    draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

    w, h = draw_text.textsize(zn, font=font_cr)
    xxxx, yyyy = 0.50 * (W - w), 0.58 * H - h
    draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

    w, h = draw_text.textsize(vopr, font=font_name)
    xxxxx, yyyyy = 0.50 * (W - w), 0.62 * H - h
    draw_text.text((xxxxx, yyyyy), vopr, fill='#ffffff', font=font_name)  # ваш вопрос

    w, h = draw_text.textsize(vopros, font=font_cr)
    xxxxxx, yyyyyy = 0.50 * (W - w), 0.64 * H - h
    draw_text.text((xxxxxx, yyyyyy), vopros, fill='#ffffff', font=font_cr)  # ваш вопрос

    w, h = draw_text.textsize(onv, font=font_name)
    xxxxx, yyyyy = 0.50 * (W - w), 0.67 * H - h
    draw_text.text((xxxxx, yyyyy), onv, fill='#ffffff', font=font_name)  # ответ на ваш вопрос

    # Вывод картинки
    img.paste(cards, (107, 5), cards)
    photo = io.BytesIO()
    img.save(photo, format='PNG')
    photo.seek(0)
    return photo


async def cards_3(my_card, card_num):
    if 1 == card_num:
        # загрузка картинки
        img = Image.open('card_pics/fon.png')
        cards = Image.open(f'card_pics/{my_card.card_pic}')
        cards = cards.resize((302, 436))

        # Работа с текстом
        font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
        font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
        font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
        wrapper = textwrap.TextWrapper(width=50)
        name = f'Ваша карта прошлого {my_card.card_name}'
        crt_zn = 'Краткое значение карты:'
        zn = f'{my_card.card_cratc}'
        om = f'Прошлое:'
        texts = f'{my_card.card_back}'
        word_list = wrapper.wrap(text=texts)
        text_new = ''
        t = 0
        for ii in word_list[:-1]:
            t = t + 1
            text_new = text_new + ii + '\n'

        text_new += word_list[-1]
        draw_text = ImageDraw.Draw(img)

        W, H = img.size
        w, h = draw_text.textsize(text_new, font=font)
        if t >= 17:
            x, y = 0.50 * (W - w), 530
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=11)
            wrapper = textwrap.TextWrapper(width=75)
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'
        if 16 >= t >= 11:
            x, y = 0.50 * (W - w), 0.90 * (H - h)
        if 10 >= t >= 7:
            x, y = 0.50 * (W - w), 0.80 * (H - h)
        if t <= 6:
            x, y = 0.50 * (W - w), 0.72 * (H - h)
        draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

        w, h = draw_text.textsize(name, font=font_name)
        xx, yy = 0.50 * (W - w), 0.53 * H - h
        draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

        w, h = draw_text.textsize(crt_zn, font=font_name)
        xxx, yyy = 0.50 * (W - w), 0.56 * H - h
        draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

        w, h = draw_text.textsize(zn, font=font_cr)
        xxxx, yyyy = 0.50 * (W - w), 0.58 * H - h
        draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

        w, h = draw_text.textsize(om, font=font_name)
        xxxxx, yyyyy = 0.50 * (W - w), 0.63 * H - h
        draw_text.text((xxxxx, yyyyy), om, fill='#ffffff', font=font_name)  # ответ на ваш вопрос

        img.paste(cards, (107, 5), cards)
        photo = io.BytesIO()
        img.save(photo, format='PNG')
        photo.seek(0)
        return photo

    if 2 == card_num:
        # загрузка картинки
        img = Image.open('card_pics/fon.png')
        cards = Image.open(f'card_pics/{my_card.card_pic}')
        cards = cards.resize((302, 436))

        # Работа с текстом
        font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
        font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
        font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
        wrapper = textwrap.TextWrapper(width=50)
        name = f'Ваша карта настоящего {my_card.card_name}'
        crt_zn = 'Краткое значение карты:'
        zn = f'{my_card.card_cratc}'
        om = f'Настоящее:'
        texts = f'{my_card.card_tyday}'
        word_list = wrapper.wrap(text=texts)
        text_new = ''
        t = 0
        for ii in word_list[:-1]:
            t = t + 1
            text_new = text_new + ii + '\n'

        text_new += word_list[-1]
        draw_text = ImageDraw.Draw(img)

        W, H = img.size
        w, h = draw_text.textsize(text_new, font=font)
        if t >= 17:
            x, y = 0.50 * (W - w), 530
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=11)
            wrapper = textwrap.TextWrapper(width=75)
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'
        if 16 >= t >= 11:
            x, y = 0.50 * (W - w), 0.90 * (H - h)
        if 10 >= t >= 7:
            x, y = 0.50 * (W - w), 0.80 * (H - h)
        if t <= 6:
            x, y = 0.50 * (W - w), 0.72 * (H - h)
        draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

        w, h = draw_text.textsize(name, font=font_name)
        xx, yy = 0.50 * (W - w), 0.53 * H - h
        draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

        w, h = draw_text.textsize(crt_zn, font=font_name)
        xxx, yyy = 0.50 * (W - w), 0.56 * H - h
        draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

        w, h = draw_text.textsize(zn, font=font_cr)
        xxxx, yyyy = 0.50 * (W - w), 0.58 * H - h
        draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

        w, h = draw_text.textsize(om, font=font_name)
        xxxxx, yyyyy = 0.50 * (W - w), 0.63 * H - h
        draw_text.text((xxxxx, yyyyy), om, fill='#ffffff', font=font_name)  # ответ на ваш вопрос

        img.paste(cards, (107, 5), cards)
        photo = io.BytesIO()
        img.save(photo, format='PNG')
        photo.seek(0)
        return photo

    if 3 == card_num:
        # загрузка картинки
        img = Image.open('card_pics/fon.png')
        cards = Image.open(f'card_pics/{my_card.card_pic}')
        cards = cards.resize((302, 436))

        # Работа с текстом
        font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
        font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
        font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
        wrapper = textwrap.TextWrapper(width=50)
        name = f'Ваша карта будущего {my_card.card_name}'
        crt_zn = 'Краткое значение карты:'
        zn = f'{my_card.card_cratc}'
        om = f'Будущее:'
        texts = f'{my_card.card_next}'
        word_list = wrapper.wrap(text=texts)
        text_new = ''
        t = 0
        for ii in word_list[:-1]:
            t = t + 1
            text_new = text_new + ii + '\n'

        text_new += word_list[-1]
        draw_text = ImageDraw.Draw(img)

        W, H = img.size
        w, h = draw_text.textsize(text_new, font=font)
        if t >= 17:
            x, y = 0.50 * (W - w), 530
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=11)
            wrapper = textwrap.TextWrapper(width=75)
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'
        if 16 >= t >= 11:
            x, y = 0.50 * (W - w), 0.90 * (H - h)
        if 10 >= t >= 7:
            x, y = 0.50 * (W - w), 0.80 * (H - h)
        if t <= 6:
            x, y = 0.50 * (W - w), 0.72 * (H - h)
        draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

        w, h = draw_text.textsize(name, font=font_name)
        xx, yy = 0.50 * (W - w), 0.53 * H - h
        draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

        w, h = draw_text.textsize(crt_zn, font=font_name)
        xxx, yyy = 0.50 * (W - w), 0.56 * H - h
        draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

        w, h = draw_text.textsize(zn, font=font_cr)
        xxxx, yyyy = 0.50 * (W - w), 0.58 * H - h
        draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

        w, h = draw_text.textsize(om, font=font_name)
        xxxxx, yyyyy = 0.50 * (W - w), 0.63 * H - h
        draw_text.text((xxxxx, yyyyy), om, fill='#ffffff', font=font_name)  # ответ на ваш вопрос

        img.paste(cards, (107, 5), cards)
        photo = io.BytesIO()
        img.save(photo, format='PNG')
        photo.seek(0)
        return photo


async def cards_6(my_card, card_num, bools):
    if 1 == card_num:
        if bools == True:
            # загрузка картинки
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')

            cards = cards.resize((302, 436))

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                         size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта которая представляет вас'
            names = f'{my_card.card_name}'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc}'
            texts = f'Карта указывает на {my_card.card_zn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo

        if bools == False:
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')
            cards = cards.resize((302, 436))
            cards = cards.rotate(180)

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта которая представляет вас'
            names = f'{my_card.card_name}(Перевернутая)'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc_obr}'
            texts = f'Перевернутая карта указывает на {my_card.card_obzn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo
    if 2 == card_num:
        if bools == True:
            # загрузка картинки
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')

            cards = cards.resize((302, 436))

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                         size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта которая представляет вашего партнера'
            names = f'{my_card.card_name}'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc}'
            texts = f'Карта указывает на {my_card.card_zn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo

        if bools == False:
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')
            cards = cards.resize((302, 436))
            cards = cards.rotate(180)

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта которая представляет вашего партнера '
            names = f'{my_card.card_name}(Перевернутая)'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc_obr}'
            texts = f'Перевернутая карта указывает на {my_card.card_obzn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo
    if 3 == card_num:
        if bools == True:
            # загрузка картинки
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')

            cards = cards.resize((302, 436))

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                         size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта подключения'
            names = f'{my_card.card_name}'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc}'
            texts = f'Карта указывает на {my_card.card_zn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo

        if bools == False:
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')
            cards = cards.resize((302, 436))
            cards = cards.rotate(180)

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта подключения'
            names = f'{my_card.card_name}(Перевернутая)'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc_obr}'
            texts = f'Перевернутая карта указывает на {my_card.card_obzn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo
    if 4 == card_num:
        if bools == True:
            # загрузка картинки
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')

            cards = cards.resize((302, 436))

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                         size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта силы ваших отношений'
            names = f'{my_card.card_name}'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc}'
            texts = f'Карта указывает на {my_card.card_zn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo

        if bools == False:
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')
            cards = cards.resize((302, 436))
            cards = cards.rotate(180)

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта силы ваших отношений'
            names = f'{my_card.card_name}(Перевернутая)'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc_obr}'
            texts = f'Перевернутая карта указывает на {my_card.card_obzn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo
    if 5 == card_num:
        if bools == True:
            # загрузка картинки
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')

            cards = cards.resize((302, 436))

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                         size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта слабых мест ваших отношений'
            names = f'{my_card.card_name}'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc}'
            texts = f'Карта указывает на {my_card.card_zn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo

        if bools == False:
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')
            cards = cards.resize((302, 436))
            cards = cards.rotate(180)

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Карта слабых мест ваших отношений'
            names = f'{my_card.card_name}(Перевернутая)'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc_obr}'
            texts = f'Перевернутая карта указывает на {my_card.card_obzn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo
    if 6 == card_num:
        if bools == True:
            # загрузка картинки
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')

            cards = cards.resize((302, 436))

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                      size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                         size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Ваша настоящая любовная карта'
            names = f'{my_card.card_name}'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc}'
            texts = f'Карта указывает на {my_card.card_zn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo

        if bools == False:
            img = Image.open('card_pics/fon.png')
            cards = Image.open(f'card_pics/{my_card.card_pic}')
            cards = cards.resize((302, 436))
            cards = cards.rotate(180)

            # Работа с текстом
            font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
            font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
            font_cr = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=12)
            wrapper = textwrap.TextWrapper(width=50)
            name = f'Ваша настоящая любовная карта'
            names = f'{my_card.card_name}(Перевернутая)'
            crt_zn = 'Краткое значение карты:'
            zn = f'{my_card.card_cratc_obr}'
            texts = f'Перевернутая карта указывает на {my_card.card_obzn}'
            word_list = wrapper.wrap(text=texts)
            text_new = ''
            t = 0
            for ii in word_list[:-1]:
                t = t + 1
                text_new = text_new + ii + '\n'

            text_new += word_list[-1]
            draw_text = ImageDraw.Draw(img)

            W, H = img.size
            w, h = draw_text.textsize(text_new, font=font)
            if t >= 17:
                x, y = 0.50 * (W - w), 530
                font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf',
                                          size=11)
                wrapper = textwrap.TextWrapper(width=75)
                word_list = wrapper.wrap(text=texts)
                text_new = ''
                for ii in word_list[:-1]:
                    t = t + 1
                    text_new = text_new + ii + '\n'
            if 16 >= t >= 11:
                x, y = 0.50 * (W - w), 0.93 * (H - h)
            if 10 >= t >= 7:
                x, y = 0.50 * (W - w), 0.83 * (H - h)
            if t <= 6:
                x, y = 0.50 * (W - w), 0.73 * (H - h)
            draw_text.text((x, y), text_new, fill='#ffffff', font=font)  # основное описание

            w, h = draw_text.textsize(name, font=font_name)
            xx, yy = 0.50 * (W - w), 0.53 * H - h
            draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(names, font=font_name)
            xx, yy = 0.50 * (W - w), 0.55 * H - h
            draw_text.text((xx, yy), names, fill='#ffffff', font=font_name)  # название карты

            w, h = draw_text.textsize(crt_zn, font=font_name)
            xxx, yyy = 0.50 * (W - w), 0.58 * H - h
            draw_text.text((xxx, yyy), crt_zn, fill='#ffffff', font=font_name)  # крт зн карты

            w, h = draw_text.textsize(zn, font=font_cr)
            xxxx, yyyy = 0.50 * (W - w), 0.60 * H - h
            draw_text.text((xxxx, yyyy), zn, fill='#ffffff', font=font_cr)  # краткое значение

            img.paste(cards, (107, 5), cards)
            photo = io.BytesIO()
            img.save(photo, format='PNG')
            photo.seek(0)
            return photo

# Отслеживание запросов
@dp.message_handler(text='🔮️ Вытянуть карты')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        chat_member = await message.bot.get_chat_member(chat_id=-1001596794390, user_id=message.from_user.id)
        if chat_member['status'] == 'left':
            await message.answer(f'<strong>Чтоб пользоваться функционалом Вам нужно быть подписанным на наш канал!</strong>', reply_markup=sub_menu)
        else:
            user = await quick_commands.select_user(message.from_user.id)
            if user.status == 'active':
                await message.answer(f'<strong>Выберите нужный расклад:</strong>\n'
                                     f'\n'
                                     f'🃏 Одна карта(Лучше всего ответит на один вопрос) - <strong>5₽</strong>\n'
                                     f'🃏 Да или нет - <strong>5₽</strong>\n'
                                     f'♣️♦️♠️ Расклад на три карты(прошлое, настоящее, будущее) - <strong>10₽</strong>\n'
                                     f'♥️ Расклад истинная любовь(6 карт) - <strong>20₽</strong>\n'
                                     f'☀️ Карта дня - <strong>Бесплатно</strong>', parse_mode='html',
                                     reply_markup=rasclad_menu)
            if user.status == 'ban':
                await message.answer('Вы заблокированы!')


@dp.message_handler(text='🃏 Одна карта(Лучше всего ответит на один вопрос)')
async def one_quest(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 5.0:
                await quick_commands.gdn_balance(user_id=message.from_user.id, amount=5)
                await message.answer(f'Таро с одной картой используется для краткого прочтения, сохраняя лаконичность и предметность. Этот тип чтения может быть полезен, когда требуется более определенный ответ, это как смотреть на чтение под увеличительным стеклом!\n'
                                     f'\n'
                                     f'Напишите ваш вопрос на который нужно получить ответ:', reply_markup=rasclad)
                await Quests.v1.set()
                @dp.message_handler(state=Quests.v1)
                async def one_quest(message: types.Message, state: FSMContext):
                    async with state.proxy() as quest:
                        quest['quest'] = message.text
                        if quest['quest'] == 'Идет расклад ⌛':
                            await message.answer('Введите вопрос на который вы хотите получить ответ:')
                        else:
                            await state.finish()
                            my_card = await quick_commands.one_card()
                            rev = ['False', 'True']
                            revers = random.choice(rev)
                            if revers == 'True':
                                photo = await card(my_card, True)
                                await message.bot.send_photo(chat_id=message.from_user.id, photo=photo, reply_markup=start_menu)
                            if revers == 'False':
                                photo = await card(my_card, False)
                                await message.bot.send_photo(chat_id=message.from_user.id, photo=photo, reply_markup=start_menu)
            elif user.balance <= 4.9:
                await message.answer(f'У Вас не достаточно средств на этот расклад, пополните баланс!\n'
                                             f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')


@dp.message_handler(text='🃏 Да или нет')
async def yes_no(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 5.0:
                await quick_commands.gdn_balance(user_id=message.from_user.id, amount=5)
                await message.answer(f'Спросите карты Таро для простого вопроса с простым результатом - да или нет раздача карт Таро.\n'
                                     f'Нет никаких ограничений на ваш вопрос - любовь, карьера, семья или любая другая тема.\n'
                                     f'\n'
                                     f'Напишите ваш вопрос на который нужно получить ответ:', reply_markup=rasclad)
                await Quests.yes_no.set()


                @dp.message_handler(state=Quests.yes_no)
                async def yes_no(message: types.Message, state: FSMContext):
                    async with state.proxy() as quest:
                        quest['yes_no'] = message.text
                        if quest['yes_no'] == 'Идет расклад ⌛':
                            await message.answer('Введите вопрос на который вы хотите получить ответ:')
                        else:
                            await state.finish()
                            my_card = await quick_commands.one_card()
                            photo = await yes_not(my_card, quest['yes_no'])
                            await message.bot.send_photo(chat_id=message.from_user.id, photo=photo, reply_markup=start_menu)
            elif user.balance <= 4.9:
                await message.answer(f'У Вас не достаточно средств на этот расклад, пополните баланс!\n'
                                             f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')


@dp.message_handler(text='♣️♦️♠️ Расклад на три карты(прошлое, настоящее, будущее)')
async def card3(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 10.0:
                await message.answer(f'Метод 3 карт дает информацию о вашем прошлом, настоящем и будущем.', reply_markup=start_card3)

                @dp.callback_query_handler(text='card_start3')
                async def card3(callback: types.CallbackQuery):
                    await quick_commands.gdn_balance(user_id=message.from_user.id, amount=10)
                    asd = await quick_commands.card_3()
                    photo_one = await cards_3(asd[0],1)
                    await callback.message.delete()
                    await callback.message.answer(text='Начинаем расклад', reply_markup=rasclad)
                    await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_one, reply_markup=next_card)

                    @dp.callback_query_handler(text='today_card')
                    async def today_card(callback: types.CallbackQuery):
                        photo_two = await cards_3(asd[1],2)
                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_two, reply_markup=n_card)

                        @dp.callback_query_handler(text='next_card')
                        async def next_card(callback: types.CallbackQuery):
                            photo_tre = await cards_3(asd[2],3)
                            await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_tre, reply_markup=start_menu)
            elif user.balance <= 9.9:
                await message.answer(f'У Вас не достаточно средств на этот расклад, пополните баланс!\n'
                                             f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')


@dp.message_handler(text='♥️ Расклад истинная любовь(6 карт)')
async def love_card(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            if user.balance >= 20.0:
                await message.answer(f'Расклад на 6 карт истинной любви дает информацию о:\n'
                                     f'<strong>1 карта</strong> - представляет вас. Это означает, что вы в настоящее время думаете о ваших отношениях, вашем подходе и вашем мировоззрении.\n'
                                     f'<strong>2 карта</strong> - представляет вашего партнера.Это также представляет его текущие эмоции по отношению к вам, его отношение и его ожидания относительно ваших отношений.\n'
                                     f'<strong>3 карта</strong> - это карта подключения.Каковы ваши общие черты и как они вас объединяют?\n'
                                     f'<strong>4 карта</strong> - указывает на силу ваших отношений. Какие качества делают ваши отношения процветающими?\n'
                                     f'<strong>5 карта</strong> - показывает слабые места в ваших отношениях. Что вам обоим нужно улучшить?\n'
                                     f'<strong>6 карта</strong> - ваша настоящая любовная карта. Он интерпретирует то, что нужно решить.',
                                     reply_markup=start_love)

                @dp.callback_query_handler(text='start_love')
                async def love_start(callback: types.CallbackQuery):
                    await callback.message.delete()
                    await quick_commands.gdn_balance(user_id=callback.from_user.id, amount=20)
                    await callback.message.answer(text='Начинаем расклад', reply_markup=rasclad)
                    card = await quick_commands.card_love()
                    rev = ['False', 'True']
                    revers = random.choice(rev)
                    if revers == 'True':
                        photo_one = await cards_6(card[0], 1, True)
                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_one, reply_markup=two_cards)

                        @dp.callback_query_handler(text='two_cards')
                        async def two_card(callback: types.CallbackQuery):
                            rev = ['False', 'True']
                            revers = random.choice(rev)
                            if revers == 'True':
                                photo_two = await cards_6(card[1], 2, True)
                                await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_two,
                                                              reply_markup=the_cards)

                                @dp.callback_query_handler(text='the_cards')
                                async def the_card(callback: types.CallbackQuery):
                                    rev = ['False', 'True']
                                    revers = random.choice(rev)
                                    if revers == 'True':
                                        photo_the = await cards_6(card[2], 3, True)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the,
                                                                      reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                    if revers == 'False':
                                        photo_the = await cards_6(card[2], 3, False)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the,
                                                                      reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                            if revers == 'False':
                                photo_two = await cards_6(card[1], 2, False)
                                await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_two,
                                                              reply_markup=the_cards)

                                @dp.callback_query_handler(text='the_cards')
                                async def the_card(callback: types.CallbackQuery):
                                    rev = ['False', 'True']
                                    revers = random.choice(rev)
                                    if revers == 'True':
                                        photo_the = await cards_6(card[2], 3, True)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the,
                                                                      reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                    if revers == 'False':
                                        photo_the = await cards_6(card[2], 3, False)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the,
                                                                      reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                    if revers == 'False':
                        photo_one = await cards_6(card[0], 1, False)
                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_one,
                                                      reply_markup=two_cards)

                        @dp.callback_query_handler(text='two_cards')
                        async def two_card(callback: types.CallbackQuery):
                            rev = ['False', 'True']
                            revers = random.choice(rev)
                            if revers == 'True':
                                photo_two = await cards_6(card[1], 2, True)
                                await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_two, reply_markup=the_cards)

                                @dp.callback_query_handler(text='the_cards')
                                async def the_card(callback: types.CallbackQuery):
                                    rev = ['False', 'True']
                                    revers = random.choice(rev)
                                    if revers == 'True':
                                        photo_the = await cards_6(card[2], 3, True)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the,
                                                                      reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                    if revers == 'False':
                                        photo_the = await cards_6(card[2], 3, False)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the,
                                                                      reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                            if revers == 'False':
                                photo_two = await cards_6(card[1], 2, False)
                                await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_two,
                                                              reply_markup=the_cards)

                                @dp.callback_query_handler(text='the_cards')
                                async def the_card(callback: types.CallbackQuery):
                                    rev = ['False', 'True']
                                    revers = random.choice(rev)
                                    if revers == 'True':
                                        photo_the = await cards_6(card[2], 3, True)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the, reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                    if revers == 'False':
                                        photo_the = await cards_6(card[2], 3, False)
                                        await callback.bot.send_photo(chat_id=callback.from_user.id, photo=photo_the,
                                                                      reply_markup=fo_cards)

                                        @dp.callback_query_handler(text='fo_cards')
                                        async def fo_card(callback: types.CallbackQuery):
                                            rev = ['False', 'True']
                                            revers = random.choice(rev)
                                            if revers == 'True':
                                                photo_fo = await cards_6(card[3], 4, True)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                            if revers == 'False':
                                                photo_fo = await cards_6(card[3], 4, False)
                                                await callback.bot.send_photo(chat_id=callback.from_user.id,
                                                                              photo=photo_fo,
                                                                              reply_markup=fiv_cards)

                                                @dp.callback_query_handler(text='fiv_cards')
                                                async def fiv_card(callback: types.CallbackQuery):
                                                    rev = ['False', 'True']
                                                    revers = random.choice(rev)
                                                    if revers == 'True':
                                                        photo_fiv = await cards_6(card[4], 5, True)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv, reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
                                                    if revers == 'False':
                                                        photo_fiv = await cards_6(card[4], 5, False)
                                                        await callback.bot.send_photo(
                                                            chat_id=callback.from_user.id,
                                                            photo=photo_fiv,
                                                            reply_markup=six_cards)

                                                        @dp.callback_query_handler(text='six_cards')
                                                        async def six_card(callback: types.CallbackQuery):
                                                            rev = ['False', 'True']
                                                            revers = random.choice(rev)
                                                            if revers == 'True':
                                                                photo_six = await cards_6(card[5], 6, True)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)

                                                            if revers == 'False':
                                                                photo_six = await cards_6(card[5], 6, False)
                                                                await callback.bot.send_photo(
                                                                    chat_id=callback.from_user.id,
                                                                    photo=photo_six, reply_markup=start_menu)
            elif user.balance <= 19.9:
                    await message.answer(f'У Вас не достаточно средств на этот расклад, пополните баланс!\n'
                                                 f'\n', parse_mode='html', reply_markup=faunds_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')


@dp.message_handler(text='🔙 Назад')
async def back(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer('Выберите действие:', reply_markup=start_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')


@dp.message_handler(text='☀️ Карта дня')
async def back(message: types.Message):
    if message.chat.type == 'private':
        chat_member = await message.bot.get_chat_member(chat_id=-1001596794390, user_id=message.from_user.id)
        if chat_member['status'] == 'left':
            await message.answer(f'<strong>Чтоб пользоваться функционалом Вам нужно быть подписанным на наш канал!</strong>',
                                 reply_markup=sub_menu)
        else:
            user = await quick_commands.select_user(message.from_user.id)
            today = datetime.now()
            if user.status == 'active':
                if user.card_day == f'{today.day}.{today.month}.{today.year}':
                    await message.answer('<strong>Карту дня можно получить 1 раз в день!</strong>\n'
                                         'Вы уже получили свою карту!', reply_markup=start_menu)
                else:
                    await quick_commands.data_card(user_id=message.from_user.id, card_day=f'{today.day}.{today.month}.{today.year}')
                    my_card = await quick_commands.one_card()
                    img = Image.open('card_pics/fon.png')
                    cards = Image.open(f'card_pics/{my_card.card_pic}')

                    cards = cards.resize((302, 436))

                    # Работа с текстом
                    font = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=14)
                    font_name = ImageFont.truetype('card_pics/ofont.ru_Hero.ttf', size=18)
                    wrapper = textwrap.TextWrapper(width=50)
                    name = f'Ваша карта дня {my_card.card_name}'
                    texts = f'{my_card.card_day}'
                    word_list = wrapper.wrap(text=texts)
                    text_new = ''
                    t = 0
                    for ii in word_list[:-1]:
                        t = t + 1
                        text_new = text_new + ii + '\n'

                    text_new += word_list[-1]
                    draw_text = ImageDraw.Draw(img)

                    w, h = draw_text.textsize(text_new, font=font)
                    W, H = img.size
                    if t >= 17:
                        x, y = 0.50 * (W - w), 0.95 * (H - h)
                    if t <= 16 and t >= 11:
                        x, y = 0.50 * (W - w), 0.80 * (H - h)
                    else:
                        x, y = 0.50 * (W - w), 0.70 * (H - h)

                    w, h = draw_text.textsize(name, font=font_name)
                    xx, yy = 0.50 * (W - w), 0.53 * H - h

                    draw_text.text((x, y), text_new, fill='#ffffff', font=font)
                    draw_text.text((xx, yy), name, fill='#ffffff', font=font_name)
                    img.paste(cards, (107, 5), cards)
                    photo = io.BytesIO()
                    img.save(photo, format='PNG')
                    photo.seek(0)
                    await message.bot.send_photo(chat_id=message.from_user.id, photo=photo)

            if user.status == 'ban':
                await message.answer('Вы заблокированы!')


@dp.message_handler(text='Идет расклад ⌛')
async def rasc(message: types.Message):
    if message.chat.type == 'private':
        await message.answer('Продолжайте расклад')


@dp.callback_query_handler(text='checks_sub')
async def check_sub_channel(callbacl: types.CallbackQuery):
    chat_member = await callbacl.bot.get_chat_member(chat_id=-1001596794390, user_id=callbacl.from_user.id)
    if chat_member['status'] == 'left':
        await callbacl.message.delete()
        await callbacl.message.answer('Вы не подписались на канал!', reply_markup=sub_menu)
    else:
        await callbacl.message.delete()
        await callbacl.message.answer(f'Спасибо за подписку 😊, теперь функционал открыт для Вас!', reply_markup=start_menu)