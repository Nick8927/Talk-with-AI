from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from states.creator import Creator
from aiogram.fsm.context import FSMContext
from settings_ai.settings import ask

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """обработка команды /start"""
    await message.answer("Я готов дать ответ на любой вопрос\nНапишите его 👇")


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
