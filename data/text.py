from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


from loader import dp


class NotCommand(BoundFilter):
    async def check(self, message: types.Message):
        command = str(message.text)
        return command[0] != "/"


@dp.message_handler(NotCommand())
async def NotCommandFunc(message: types.Message):
    await message.answer(text="Не команда")


@dp.message_handler()
async def NotCommandFunc(message: types.Message):
    await message.answer(text="Команда")
