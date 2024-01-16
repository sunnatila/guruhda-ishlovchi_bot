from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import GroupFilter, AdminFilter, PrivateFilter
from loader import dp


@dp.message_handler(GroupFilter(), CommandStart(), AdminFilter())
async def start_bot_admin(msg: types.Message):
    await msg.answer(f"Salom {msg.from_user.full_name} \n"
                     f"Oyin oynamoqchi bolsangiz /start_questions komandasini bering!!")


@dp.message_handler(GroupFilter(), CommandStart())
async def start_bot_admin(msg: types.Message):
    await msg.answer(f"Salom {msg.from_user.full_name}")


