from aiogram.dispatcher.filters.state import StatesGroup,State


class Form(StatesGroup):
    name = State()
    email = State()
    phone = State()

    @classmethod
    def reset_state(cls):
        pass
