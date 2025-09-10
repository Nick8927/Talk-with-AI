from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    """обработка команды /start"""
    await message.answer("Я готов дать ответ на любой вопрос\nНапишите его 👇")