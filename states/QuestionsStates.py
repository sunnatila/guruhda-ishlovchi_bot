from aiogram.dispatcher.filters.state import State, StatesGroup


class QuestionsStatesGroup(StatesGroup):
    start = State()
    stop = State()

