from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=3,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text="Телефон", callback_data=buy_callback.new(
                                                            item_name="Phone",
                                                            count=2))

                                  ],
                                  [
                                      InlineKeyboardButton(text="Компьютер", callback_data=buy_callback.new(
                                                            item_name="Computer",
                                                            count=5))

                                  ],

                                  [
                                      InlineKeyboardButton(text="Видеокарта", callback_data=buy_callback.new(
                                                            item_name="VideoCard",
                                                            count=3))

                                  ],

                                  [
                                      InlineKeyboardButton(text="Отмена", callback_data="chancel")

                                  ]
                              ])
