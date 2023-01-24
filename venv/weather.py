from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def get_weather(city, country='RUS'):
    owm = OWM('aa0a32f4341403aa09700231c23386ce')
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(f'{city}, {country}')
    except:
        return None

    w = observation.weather
    result = f'⌬ {w.detailed_status}',\
        f'⌬ Скорость ветра: {w.wind()["speed"]} м/с', \
        f'⌬ Температура: {w.temperature("celsius")["temp"]} °C', \
        f'⌬ Ощущается как: {w.temperature("celsius")["feels_like"]} °C'
    result = '; '.join(result)

    return result

