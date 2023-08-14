from aiogram import types
from loader import dp
from keyboards.default.keyboard_menu import profile_menu
from utils.dbapi import quick_commands


@dp.message_handler(text='⚙️ Аккаунт')
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        user = await quick_commands.select_user(message.from_user.id)
        count_ref = await quick_commands.count_refs(message.from_user.id)
        if user.status == 'active':
            create = f'{user.created_at}'
            lst = create.split()
            await message.answer(f'<strong>Ваш профиль</strong>\n'
                                 f'<em>Вся необходимая информация о вашем профиле</em>\n'
                                 f'\n'
                                 f'👤 <strong>ID: </strong>{user.user_id}\n'
                                 f'💶 <strong>Баланс: {user.balance}</strong>\n'
                                 f'👤 <strong>Регистрация: </strong>{lst[0]}\n'
                                 f'👨‍👦‍👦 <strong>Рефералы: </strong>{count_ref}\n', parse_mode='html',
                                 reply_markup=profile_menu)
        if user.status == 'ban':
            await message.answer('Вы заблокированы!')
