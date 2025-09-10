from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_start_keyboard():
    """Клавиатура при старте"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="I'm ready to talk 👁‍🗨")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
