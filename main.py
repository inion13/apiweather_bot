import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from routes.help import help_router
from routes.message import message_router
from routes.start import start_router

load_dotenv()

logging.basicConfig(level=logging.INFO)


async def main():
    bot_token = os.getenv('TOKEN')
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(message_router)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
