import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TG_TOKEN
from handlers import router

logging.basicConfig(level=logging.INFO)


async def main():
    """корутина запуска бота"""
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher(bot=bot)

    dp.include_router(router)

    logging.info("Бот в работе...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
