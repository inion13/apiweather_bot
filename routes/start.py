from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command(commands=['start']))
async def greetings(message: types.Message):
    await message.answer("Hello, im bot")