import requests

from abc import ABC, abstractmethod
from services import get_print


class GeoLocatorInterface(ABC):

    @abstractmethod
    def get_coordinates(self, address: str) -> tuple:
        pass


class YandexGeoLocator(GeoLocatorInterface):

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}'

    def get_coordinates(self, address: str) -> tuple:
        call_url = f'{self.base_url}&geocode={address}&format=json'
        response = requests.get(call_url)
        json_response = response.json()
        lat_lon = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point'][
                'pos'].split(' ')
        adr = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
                'metaDataProperty']['GeocoderMetaData']['text']
        return (lat_lon[1], lat_lon[0]), adr


class WeatherForecastService:

    def __init__(self, geo_locator: GeoLocatorInterface):
        self.geo_locator = geo_locator

    def get_weather(self, address):
        coordinates = self.geo_locator.get_coordinates(address)[0]
        location = self.geo_locator.get_coordinates(address)[1]
        response = requests.get(
            f'https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&'
            'current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,rain,'
            'showers,snowfall,cloudcover,surface_pressure,windspeed_10m,winddirection_10m&'
            'daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&windspeed_unit=ms&'
            'timezone=Europe%2FMoscow'
            )
        r = response.json()
        return get_print(r, location)
