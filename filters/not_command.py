from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class NotCommand(BoundFilter):
    async def check(self, message: types.Message):
        command = str(message.text)
        print("NOT" + str(command[0] != "/"))
        return command[0] != "/"
