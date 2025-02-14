import requests

# API-Key wahrscheinlich nicht mehr gültig!
api_key = 'ef445623229f6aae515011f47b94e800'

url = f'http://api.openweathermap.org/data/2.5/weather?q=Berlin&appid={api_key}&units=metric'

response = requests.get(url)

data = response.json()

if data['cod'] == 200:
    print(f"Aktuelle Temperatur in Berlin: {data['main']['temp']}°C")
else:
    print(f"Fehler bei der API-Anfrage: {data['message']}")
