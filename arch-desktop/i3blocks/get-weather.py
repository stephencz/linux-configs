from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def get_weather_icon(weather):
    output = ""

    status = str(weather.status).lower()
    if(weather.clouds <= 25):
        output = ''

    if(weather.clouds <= 60 and weather.clouds > 25):
        output = ''

    if(weather.clouds > 60 or status == 'clouds'):
        output = ''

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
    owm = OWM('API')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Vineland, US')
    w = observation.weather

    output = ""

    output += get_weather_icon(w)
    output += ' ' + get_temp(w)
    output += ' ' + get_wind(w) + ' ' 

    print(output) # Full
    print(output) # Short

    with open('weather_output.txt', 'w') as file:
        file.write('Status: ' + str(w.status) + '\n')
        file.write('Temperature: ' + str(w.temperature('fahrenheit')) + '\n')
        file.write('Wind: ' + str(w.wind()) + '\n')
        file.write('Clouds: ' + str(w.clouds) + '\n')
        file.write('Rain: ' + str(w.rain) + '\n')
        file.write('Precipitation: ' + str(w.precipitation_probability) + '\n')

if __name__ == '__main__':
    run()
