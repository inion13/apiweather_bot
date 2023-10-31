import requests


def get_weather(latitude, longitude):
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&'
                            'current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,rain,'
                            'showers,snowfall,cloudcover,surface_pressure,windspeed_10m,winddirection_10m&'
                            'daily=sunrise,sunset&timezone=Europe%2FMoscow'
                            )
    r = response.json()

    for i in r:
        print(f'{i} : {r[i]}')

    print(f'''
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
''')

if __name__ == '__main__':
    lat = input('Input latitude: ')
    long = input('Input longitude: ')
    get_weather(lat, long)

