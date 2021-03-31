from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def get_weather_icon(weather):
    output = ""

    status = str(weather.status).lower()
    if(weather.clouds <= 60 and weather.clouds > 25):
        output = ''

    if(weather.clouds > 60):
        output = ''

    else:
        output = ''

    if('rain' in status or 'rainy' in status or 'raining' in status):
        output = ''

    if('snow' in status or 'snowy' in status or 'snowing' in status):
        output = ''

    return output

def get_temp(weather):
    return str(weather.temperature('fahrenheit')['temp']).split('.', 1)[0] + '°'

def get_wind(weather):
    wind = weather.wind()['speed'] * 2.237
    return '  ' + str(wind).split('.', 1)[0] 

def run():
    # Get weather data for Vineland, NJ
    owm = OWM('d1275943b595a4bf513b71ae9573036b')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Vineland, US')
    w = observation.weather

    output = ""

    output += get_weather_icon(w)
    output += ' ' + get_temp(w)
    output += ' ' + get_wind(w) + ' ' 

    print(output) # Full
    print(output) # Short

if __name__ == '__main__':
    run()
