from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart

from keyboards.reply import get_start_keyboard
from states.creator import Creator
from aiogram.fsm.context import FSMContext
from settings_ai.settings import ask

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """обработка команды /start"""
    await message.answer(
        "Привет 👋\nЯ готов дать ответ на любой вопрос.\nНажми кнопку ниже",
        reply_markup=get_start_keyboard()
    )

@router.message(F.text == "I'm ready to talk 👁‍🗨")
async def start_chat(message: Message):
    """обработка кнопки при входе"""
    await message.answer(
        "Я жду твоего вопроса,\nнапиши его скорее 👇",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Creator.wait)
async def stop_flood(message: Message):
    """защита от флуда"""
    await message.answer("Ваш запрос обрабатывается,\nпожалуйста подождите 😊")


@router.message()
async def generate(message: Message, state: FSMContext):
    """обработка запроса и ответ пользователю"""
    await state.set_state(Creator.wait)
    response = await ask(message.text)
    await message.answer(response)
    await state.clear()
