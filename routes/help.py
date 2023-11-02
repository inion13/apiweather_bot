from aiogram import Router, types
from aiogram.filters import Command

help_router = Router()


@help_router.message(Command(commands=['help']))
async def get_help(message: types.Message):
    await message.answer("Чтобы воспользоваться ботом, тебе нужно просто написать нужный населенный пункт")
