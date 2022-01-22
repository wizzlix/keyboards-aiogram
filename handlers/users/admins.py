from aiogram.dispatcher.filters import Command

from filters import IsPrivate

from loader import dp
from aiogram import types
from data.config import ADMINS


@dp.message_handler(IsPrivate(), Command("admin", prefixes="."), user_id=ADMINS)
async def send_admin_secret_message(message: types.Message):
    await message.answer(text="You admin!")
