import os

from aiogram import Router, types
from weather_api import *

message_router = Router()


@message_router.message()
async def handle_message(message: types.Message):
    api_key = os.getenv('API_YANDEX_KEY')
    locator = YandexGeoLocator(api_key)
    service = WeatherForecastService(locator)
    try:
        weather = service.get_weather(message.text)
        await message.answer(weather)
    except Exception:
        await message.answer('Что-то пошло не так, я не знаю этого адреса :(\nПопробуй еще раз')
