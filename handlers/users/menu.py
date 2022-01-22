from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберете товар из списка!", reply_markup=menu)


@dp.message_handler(Text(equals=["Пюрешка", "Макарошки"]))
async def get_food(message: types.Message):
    await message.answer(text=f"Вы выбрали {message.text}", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Котлетки")
async def get_food(message: types.Message):
    await message.answer(text=f"Вы выбрали Котлетки")