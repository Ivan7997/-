import requests

def weather(city):

    appid = '7080b85d03b618cd74a84a0fa43249d3'

    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

    print(data["coord"])
    print(data["main"]["temp"])
    print(data["main"]["pressure"])
    print(data["main"]["humidity"])
    print(data["visibility"])
    print(data["clouds"])
    print(data["snow"])
    print(data["timezone"])

weather("Kazan")