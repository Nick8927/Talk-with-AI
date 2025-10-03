from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_learning_menu():
    """клавиатура для меню обучения"""
    keyboard = [
        [InlineKeyboardButton(text="📅 Daily routine", callback_data="learn_daily")],
        [InlineKeyboardButton(text="🔤 Irregular verbs", callback_data="learn_irregular")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
