from utils.dbapi.schemas.user import User, Card, Check, Promocode, Promoactive
from asyncpg import UniqueViolationError
from utils.dbapi.db_gino import db
import random


# Команды для пользователя
async def add_user(user_id: int, f_name: str, l_name: str, username: str, referral_id: int, status: str,
                   balance: float, card_day: str):
    try:
        user = User(user_id=user_id, f_name=f_name, l_name=l_name, referral_id=referral_id, username=username,
                    status=status, balance=balance, card_day=card_day)
        await user.create()
    except UniqueViolationError:
        print('Ошибка добавления юзера')


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def gdn_balance(user_id: int, amount):
    user = await select_user(user_id)
    new_balance = user.balance - amount
    await user.update(balance=new_balance).apply()

async def data_card(user_id: int, card_day:str):
    user = await User.query.where(User.user_id == user_id).gino.first()
    await user.update(card_day=card_day).apply()

async def user_count():
    users = await User.query.gino.all()
    return len(users)


# Рефералы
async def check_args(args, user_id: int):
    if args == '':
        args = '0'
        return args
    elif not args.isnumeric():
        args = '0'
        return args
    elif args.isnumeric():
        if int(args) == user_id:
            args = '0'
            return args
        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args
        else:
            args = str(args)
            return args
    else:
        args = '0'
        return args


async def count_refs(user_id):
    refs = await User.query.where(User.referral_id == user_id).gino.all()
    return len(refs)


# Работа картами
async def one_card():
    card = await Card.query.gino.all()
    rn = len(card)
    return card[random.randint(0, rn - 1)]


async def card_3():
    card = await Card.query.gino.all()
    rn = len(card)
    start = True
    while start:
        card_one = card[random.randint(0, rn - 1)]
        card_two = card[random.randint(0, rn - 1)]
        card_tre = card[random.randint(0, rn - 1)]
        if card_one != card_two and card_one != card_tre and card_two != card_tre:
            start = False
            return card_one, card_two, card_tre
        else:
            start = True


async def card_love():
    card = await Card.query.gino.all()
    rn = len(card)
    start = True
    while start:
        card_one = card[random.randint(0, rn - 1)]
        card_two = card[random.randint(0, rn - 1)]
        card_tre = card[random.randint(0, rn - 1)]
        card_fo = card[random.randint(0, rn - 1)]
        card_five = card[random.randint(0, rn - 1)]
        card_six = card[random.randint(0, rn - 1)]
        if card_one != card_two and card_one != card_tre and card_one != card_fo and card_one != card_five and card_one != card_six and card_two != card_tre and card_two != card_fo and card_two != card_five and card_two != card_six and card_tre != card_fo and card_tre != card_five and card_tre != card_six and card_fo != card_five and card_fo != card_six and card_five != card_six:
            start = False
            return card_one, card_two, card_tre, card_fo, card_five, card_six
        else:
            start = True


# Работа с балансом и пополнение
async def create_check(user_id: int, amount: int, bill_id: str, url_p: str):
    check = Check(user_id=user_id, amount=amount, bill_id=bill_id, url_p=url_p)
    await check.create()


async def get_check(bill_id: str):
    get_check = await Check.query.where(Check.bill_id == bill_id).gino.first()
    if get_check is None:
        return False
    else:
        return get_check


async def del_check(bill_id: str):
    del_check = await Check.query.where(Check.bill_id == bill_id).gino.first()
    await del_check.delete()


async def deposit_balance(user_id: int, amount):
    user = await select_user(user_id)
    new_balance = user.balance + amount
    await user.update(balance=new_balance).apply()


# Система промокода
async def promo_check(promo: str):
    promo = await Promocode.query.where(Promocode.promo == promo).gino.first()
    if promo is None:
        return False
    else:
        return True


async def promo_chek_active(user_id: int, promo: str):
    promo_active = await Promoactive.query.where(Promoactive.user_id == user_id).gino.all()
    if promo_active is None:
        return True
    else:
        for prom in promo_active:
            if prom.promo == promo:
                return False