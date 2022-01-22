from typing import Any

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import NotCommand, IsCommand
from states.states import Form
from loader import dp


@dp.message_handler(Command("form"), state=None)
async def name(message: types.Message, state: FSMContext):
    await message.answer(text="\t\t<b>[: Form :]</b>\n"
                              "Добро пожаловать в заполнение формы!\n\n"
                              "<i>Введите свое имя:</i>")

    await Form.first()


# @dp.message_handler(IsCommand())
# async def error(message: types.Message, state: FSMContext):
#     await message.answer(text="\t\t<b>[: Form :]</b>\n\n"
#                               "<b>[ ! ERR ! ] Введите корректное значение</b>")
#     await Form.previous()


@dp.message_handler(NotCommand(), state=Form.name, )
async def email(message: types.Message, state: FSMContext):
    await message.answer(text="\t\t<b>[: Form :]</b>\n\n"
                              "<i>Введите свой email:</i>")

    async with state.proxy() as data:
        data["name"] = message.text

    await Form.next()


@dp.message_handler(NotCommand(), state=Form.email)
async def email(message: types.Message, state: FSMContext):
    await message.answer(text="\t\t<b>[: Form :]</b>\n\n"
                              "<i>Введите свой номер телефона:</i>")
    async with state.proxy() as data:
        data["email"] = message.text

    await Form.next()


@dp.message_handler(NotCommand(), state=Form.phone)
async def email(message: types.Message, state: FSMContext):
    await message.answer(text="\t\t<b>[: Form :]</b>\n\n"
                              "<i>Спасибо за ответы!</i>")
    async with state.proxy() as data:
        data["phone"] = message.text

    await Form.next()

    await message.answer(text="\t\t<b>[: Form :]</b>\n"
                              f"<i>{message.from_user.first_name.capitalize()}, спасибо за заполнение формы:</i>\n\n\n"
                              "Ваши данные:\n\n"
                              f"<b>Имя:</b> {data['name']}\n"
                              f"<b>Email:</b> {data['email']}\n"
                              f"<b>Телефон:</b> {data['phone']}\n"
                         )

    await state.reset_state()
