from django.shortcuts import render
import requests
from datetime import datetime

from weather.forms import WeatherForm

def weather(request):
    form = WeatherForm()
    weather = None
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a65a3f613545bf5b9fac5ec4b39fe7bd'.format(city)
            response = requests.get(url)
            data = response.json()
            print(data)
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'wind': data['wind']['speed'],
                'cloudiness': data['weather'][0]['description'],
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S'),
                'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S'),
            }

    return render(request, 'weather/weather.html', {'weather': weather, 'form': form})