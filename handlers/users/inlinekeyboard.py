from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice
from loader import dp, bot


@dp.message_handler(Command("items"))
async def give_items(message: types.Message):
    await message.answer("Выберете продукт!", reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="Computer"))
async def computer(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    await call.message.answer(f"Вы выбрали {callback_data.get('item_name')} \n\n Колличество на складе: "
                              f"{callback_data.get('count')}")


@dp.callback_query_handler(buy_callback.filter(item_name="VideoCard"))
async def video_card(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    await call.message.answer(f"Вы выбрали {callback_data.get('item_name')} \n\n Колличество на складе: "
                              f"{callback_data.get('count')}")


@dp.callback_query_handler(buy_callback.filter(item_name="Phone"))
async def phone(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    await call.message.answer(f"Вы выбрали {callback_data.get('item_name')} \n\n Колличество на складе: "
                              f"{callback_data.get('count')}")


@dp.callback_query_handler(text='chancel')
async def chancel(call: CallbackQuery):
    await call.answer(cache_time=60, text="Вы отменили покупку...", show_alert=True)

    await call.message.edit_reply_markup(reply_markup=None)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


