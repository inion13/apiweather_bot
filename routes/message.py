import os

from aiogram import Router, types
from weather_api import *

message_router = Router()


@message_router.message()
async def handle_message(message: types.Message):
    api_key = os.getenv('API_YANDEX_KEY')
    locator = YandexGeoLocator(api_key)
    service = WeatherForecastService(locator)
    weather = service.get_weather(message)
    await message.answer(weather)
