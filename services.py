def get_print(r, location):
    return f'''
Погода по адресу: {location} ({r['daily']['time'][0]}):
    Температура: {r['current']['temperature_2m']}{r['current_units']['temperature_2m']} (Apparent Temperature: \
{r['current']['apparent_temperature']}{r['current_units']['apparent_temperature']}
    Осадки: {r['current']['precipitation']} мм
        Дождь: {r['current']['rain']} мм
        Град: {r['current']['showers']} мм
        Снег: {r['current']['snowfall']} см
    Облачность: {r['current']['cloudcover']} {r['current_units']['cloudcover']}
    Атмосферное давление: {int(r['current']['surface_pressure']) / 1.333:.1f} мм рт. ст.
    Скорость ветра: {r['current']['windspeed_10m']} м/с
Восход солнца в {r['daily']['sunrise'][0][-5:]}, заход солнца в {r['daily']['sunset'][0][-5:]} по московскому времени
'''


def get_print_en(r, location):
    return f'''
Weather at the desired coordinates ({r['daily']['time'][0]}):
    Temperature: {r['current']['temperature_2m']}{r['current_units']['temperature_2m']} (Apparent Temperature: \
{r['current']['apparent_temperature']}{r['current_units']['apparent_temperature']}
    Precipitation: {r['current']['precipitation']} {r['current_units']['precipitation']}
        Rain: {r['current']['rain']} {r['current_units']['rain']}
        Showers: {r['current']['showers']} {r['current_units']['showers']}
        Snowfall: {r['current']['snowfall']} {r['current_units']['snowfall']}
    Cloudcover Total: {r['current']['cloudcover']} {r['current_units']['cloudcover']}
    Surface Pressure: {int(r['current']['surface_pressure']) / 1.333:.1f} mmHg
    Wind Speed: {r['current']['windspeed_10m']} {r['current_units']['windspeed_10m']}
Sunrise at {r['daily']['sunrise'][0][-5:]}, sunset at {r['daily']['sunset'][0][-5:]} by Moscow time
'''
def get_zero_coords():
    return 'Что-то пошло не так, попробуй еще раз'