from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters import GroupFilter, AdminFilter
from loader import dp


@dp.message_handler(GroupFilter(), CommandHelp(), AdminFilter())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start_questions - O'yinni ishga tushirish",
            "/stop_questions - O'yini tugatish")

    await message.answer("\n".join(text))