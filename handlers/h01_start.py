from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart

from keyboards.inline import get_learning_menu
from keyboards.reply import get_start_keyboard
from states.creator import Creator
from aiogram.fsm.context import FSMContext
from settings_ai.settings import ask

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
    """Daily routine — запрос к ИИ"""
    await callback.message.answer("🚀 Подбираю слова по теме *Daily routine*...")

    prompt = (
        "Составь список из 15 полезных английских слов и выражений на тему 'Daily routine'. "
        "Дай их перевод на русский и пример короткого предложения на английском."
    )

    response = await ask(prompt)
    await callback.message.answer(response)
    await callback.answer()


@router.callback_query(F.data == "learn_irregular")
async def learn_irregular(callback: CallbackQuery):
    """Irregular verbs — запрос к ИИ"""
    await callback.message.answer("🔥 Подбираю список неправильных глаголов...")

    prompt = (
        "Составь список из 15 наиболее часто используемых неправильных глаголов в английском языке. "
        "Укажи три формы (Infinitive – Past Simple – Past Participle) и перевод на русский."
    )

    response = await ask(prompt)
    await callback.message.answer(response)
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
