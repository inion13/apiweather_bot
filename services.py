def get_print(r, location):
    return f'''
По адресу: {location}
погода на сегодня ({r['daily']['time'][0][-2:]}.{r['daily']['time'][0][-5:-3]}.{r['daily']['time'][0][:4]}):
    Температура: {r['current']['temperature_2m']}{r['current_units']['temperature_2m']} (ощущается как: \
{r['current']['apparent_temperature']}°C)
    Осадки: {r['current']['precipitation']} мм
        Дождь: {r['current']['rain']} мм
        Град: {r['current']['showers']} мм
        Снег: {r['current']['snowfall']} см
    Облачность: {r['current']['cloudcover']}{r['current_units']['cloudcover']}
    Атмосферное давление: {int(r['current']['surface_pressure']) / 1.333:.1f} мм рт. ст.
    Скорость ветра: {r['current']['windspeed_10m']} м/с
Восход солнца в {r['daily']['sunrise'][0][-5:]}, заход солнца в {r['daily']['sunset'][0][-5:]} по московскому времени

Прогноз погоды на неделю:
    {r['daily']['time'][1][-2:]}.{r['daily']['time'][1][-5:-3]}.{r['daily']['time'][1][:4]}: \
{r['daily']['temperature_2m_min'][1]}°C ночью, {r['daily']['temperature_2m_max'][1]}°C днём
    {r['daily']['time'][2][-2:]}.{r['daily']['time'][2][-5:-3]}.{r['daily']['time'][2][:4]}: \
{r['daily']['temperature_2m_min'][2]}°C ночью, {r['daily']['temperature_2m_max'][2]}°C днём
    {r['daily']['time'][3][-2:]}.{r['daily']['time'][3][-5:-3]}.{r['daily']['time'][3][:4]}: \
{r['daily']['temperature_2m_min'][3]}°C ночью, {r['daily']['temperature_2m_max'][3]}°C днём
    {r['daily']['time'][4][-2:]}.{r['daily']['time'][4][-5:-3]}.{r['daily']['time'][4][:4]}: \
{r['daily']['temperature_2m_min'][4]}°C ночью, {r['daily']['temperature_2m_max'][4]}°C днём
    {r['daily']['time'][5][-2:]}.{r['daily']['time'][5][-5:-3]}.{r['daily']['time'][5][:4]}: \
{r['daily']['temperature_2m_min'][5]}°C ночью, {r['daily']['temperature_2m_max'][5]}°C днём
    {r['daily']['time'][6][-2:]}.{r['daily']['time'][6][-5:-3]}.{r['daily']['time'][6][:4]}: \
{r['daily']['temperature_2m_min'][6]}°C ночью, {r['daily']['temperature_2m_max'][6]}°C днём
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