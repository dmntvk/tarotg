from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import start_menu
from utils.dbapi import quick_commands
from aiogram.dispatcher.filters import CommandStart
from PIL import Image, ImageDraw, ImageFont
import io

async def hello(name):
    img = Image.open('card_pics/fon_start.png')
    font = ImageFont.truetype('card_pics/ofont.ru_Catallina.ttf', size=50)
    texts = f'Привет, {name}'

    draw_text = ImageDraw.Draw(img)

    W, H = img.size
    w, h = draw_text.textsize(texts, font=font)
    x, y = 0.50 * (W - w), 0.35 * (H - h)

    draw_text.text((x, y), texts, fill='#ffffff', font=font)  # основное описание

    photo = io.BytesIO()
    img.save(photo, format='PNG')
    photo.seek(0)
    return photo


@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        args = message.get_args()
        new_args = await quick_commands.check_args(args, message.from_user.id)
        try:
            user = await quick_commands.select_user(message.from_user.id)
            if user.status == 'active':
                photo = await hello(message.from_user.first_name)
                await message.bot.send_photo(chat_id=message.from_user.id, photo=photo)
                await message.answer(f'<strong>Добро пожаловать в мир Таро!</strong>\n'
                                     f'Я, ваш бот-чтец, готов раскладывать для вас карты и помочь вам улучшить понимание своей ситуации. Начнем?', parse_mode='html', reply_markup=start_menu)
            if user.status == 'ban':
                await message.answer('Вы заблокированы!')
        except Exception:
            await quick_commands.add_user(user_id=message.from_user.id,
                                          f_name=message.from_user.first_name,
                                          l_name=message.from_user.last_name,
                                          referral_id=int(new_args),
                                          username=message.from_user.username,
                                          status='active',
                                          balance=0,
                                          card_day='0')
            photo = await hello(message.from_user.first_name)
            await message.bot.send_photo(chat_id=message.from_user.id, photo=photo)
            await message.answer(f'<strong>Добро пожаловать в мир Таро!</strong>\n'
                                 f'Я, ваш бот-чтец, готов раскладывать для вас карты и помочь вам улучшить понимание своей ситуации. Начнем?', parse_mode='html', reply_markup=start_menu)
