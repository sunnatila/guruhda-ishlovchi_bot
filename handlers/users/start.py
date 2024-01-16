from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import AdminFilter, PrivateFilter
from loader import dp


@dp.message_handler(CommandStart(), AdminFilter())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} siz adminsiz!")


@dp.message_handler(CommandStart(), PrivateFilter())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
