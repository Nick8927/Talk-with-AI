from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart

from keyboards.inline import get_learning_menu
from keyboards.reply import get_start_keyboard
from states.creator import Creator
from aiogram.fsm.context import FSMContext
from settings_ai.settings import ask
from data.lessons import daily_routine_words, irregular_verbs


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """обработка команды /start"""
    photo = FSInputFile("media/banner.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Привет 👋\nЯ готов дать ответ на любой вопрос.\nНажми кнопку ниже:",
        reply_markup=get_start_keyboard()
    )


@router.message(F.text == "I'm ready to talk 👁‍🗨")
async def open_learning_menu(message: Message):
    """открытие подменю"""
    await message.answer(
        "Выбери, что хочешь изучать 👇",
        reply_markup=get_learning_menu()
    )


@router.callback_query(F.data == "learn_daily")
async def learn_daily(callback: CallbackQuery):
    await callback.message.answer(daily_routine_words, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data == "learn_irregular")
async def learn_irregular(callback: CallbackQuery):
    await callback.message.answer(irregular_verbs, parse_mode="Markdown")
    await callback.answer()

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
