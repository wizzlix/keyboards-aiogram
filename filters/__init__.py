from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .is_private import IsPrivate
from .not_command import NotCommand
from .is_command import IsCommand

if __name__ == "filters":
    # dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(NotCommand)
    dp.filters_factory.bind(IsCommand)
