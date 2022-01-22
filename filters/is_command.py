from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsCommand(BoundFilter):
    async def check(self, message: types.Message):
        command = str(message.text)
        print("YES" + str(command[0] == "/"))
        return command[0] == "/"
