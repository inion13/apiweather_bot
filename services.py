def get_print(r):
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
