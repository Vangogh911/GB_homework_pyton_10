# сюда все функции отправляющие сообщения


from aiogram import types

from bot import bot


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки.\n'
                           f'Во время хода ты можешь взять от 1 до 28 конфет.\n'
                           f'Кто забирает последнюю конфету, тот выиграл.\n'
                           f'Погнали!\n'
                           f'Сделай свой ход!')
