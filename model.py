# Здесь храним все перменные и методы для их чтения и установки (а-ля работа с классами)
from aiogram import types
from bot import bot

total_count = 150
turn = False
win = False


async def bot_turn(message: types.Message):
    global turn
    global total_count

    await win_calc(message)

    turn = True

    if 29 < total_count < 57:
        await bot.send_message(message.from_user.id, f'{total_count - 29}')
        total_count -= total_count - 29
    else:
        await bot.send_message(message.from_user.id, f'{28}')
        total_count -= 28

    await win_calc(message)

    turn = False


async def win_calc(message: types.Message):
    global turn
    global total_count
    global win

    if total_count > 0:
        await bot.send_message(message.from_user.id, f'Количество конфет {total_count}.')
    else:
        if turn and total_count <= 0:
            await bot.send_message(message.from_user.id, 'Я выиграл!')
            win = True
        if not turn and total_count <= 0:
            await bot.send_message(message.from_user.id, 'Ты выиграл!')
            win = True

    if win:
        await bot.send_message(message.from_user.id, 'Давай заново!')
        await reset(message)


async def reset(message: types.Message):
    global turn
    global total_count
    global win
    total_count = 150
    turn = False
    win = False
