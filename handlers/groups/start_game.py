from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from filters import AdminFilter, GroupFilter
from states import QuestionsStatesGroup
from handlers.groups.write_data import clear_data, write_user, get_user, get_users
from handlers.groups.sorted_result import result_sort


@dp.message_handler(GroupFilter(), AdminFilter(), Command('start_questions'))
async def start_game(msg: types.Message, state: FSMContext):
    chat_id = msg.chat.id
    file_path = f"data/groups/group{chat_id}.json".replace('-', '_')
    clear_data(file_path)
    await msg.answer(f"Oyin boshlandi. Hamaga omad\n"
                     f"Oyinni yakunlash uchun /stop_questions komadasini bering.")
    await state.set_state(QuestionsStatesGroup.start)


@dp.message_handler(GroupFilter(), AdminFilter(), Command('start_questions'), state=QuestionsStatesGroup.start)
async def start_game_error(msg: types.Message):
    await msg.answer("Oyin boshlanib bolgan, oyinni tohtatish uchun /stop_questions komandasini bering.")


@dp.message_handler(GroupFilter(), AdminFilter(), Command('stop_questions'), state=QuestionsStatesGroup.start)
async def stop_game(msg: types.Message, state: FSMContext):
    await msg.answer("Savol berish oyinni tugadi \n"
                     "Natijani bilish uchun /result komandasini bering.")
    await QuestionsStatesGroup.next()


@dp.message_handler(GroupFilter(), AdminFilter(), state=QuestionsStatesGroup.start)
async def error_start_questions(msg: types.Message, state: FSMContext):
    id_group = msg.chat.id
    file_path = f"data/groups/group{id_group}.json".replace('-', '_')
    try:
        user = msg.reply_to_message.from_user
        ball = msg.text
        if ball.isdigit():
            ball = int(ball)
        else:
            await msg.reply(f"Admin siz {user.get_mention(as_html=True)} ga notog'ri ball berdingiz!")
            return
        user_data = get_user(user.id, file_path)
        if user_data:
            data = user_data[0]
            data['score'] += ball
        else:
            data = {
                'id': user.id,
                'username': user.username,
                'fullname': user.full_name,
                'score': ball,
                'mention': user.get_mention(as_html=True)
            }

        write_user(data, file_path)
        await msg.answer(f"{user.get_mention(as_html=True)} ga {ball} ball berildi!")
    except AttributeError:
        return


@dp.message_handler(GroupFilter(), Command("result"), AdminFilter(), state=QuestionsStatesGroup.stop)
async def result_questions(msg: types.Message, state: FSMContext):
    id_group = msg.chat.id
    file_path = f"data/groups/group{id_group}.json".replace('-', '_')
    result = get_users(file_path)
    info = "Reyting: \n"
    response = result_sort(result)
    if response:
        info += '\n'.join(map(lambda user, i: f"{i}. {user['mention']} - {user['score']} ball", response,
                              range(1, len(response) + 1)))
    await msg.answer(text=info)
    await state.finish()


@dp.message_handler(GroupFilter(), AdminFilter(), state=QuestionsStatesGroup.stop)
async def error_stop(msg: types.Message, state: FSMContext):
    await msg.answer("O'yin yakunlangan. Natijalarni elon qiling: /result")
