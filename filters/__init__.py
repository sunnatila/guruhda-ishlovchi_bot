from aiogram import Dispatcher

from loader import dp
from .is_admin import AdminFilter
from .is_group import GroupFilter
from .is_private import PrivateFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(GroupFilter)
    dp.filters_factory.bind(PrivateFilter)
    pass
