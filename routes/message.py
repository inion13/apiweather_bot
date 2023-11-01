import os

from aiogram import Router, types
from weather_api import *

message_router = Router()


@message_router.message()
async def handle_message(message: types.Message):
    api_key = os.getenv('API_YANDEX_KEY')
    locator = YandexGeoLocator(api_key)
    service = WeatherForecastService(locator)
    user_input = message.text
    weather = service.get_weather(user_input)
    await message.answer(weather)
