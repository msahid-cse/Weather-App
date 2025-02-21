from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.POST.get("city")
        api_key = "b5ae4a84e5d2a9849a1aabf7978e7567"  # Replace with your OpenWeatherMap API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }
        else:
            error_message = "City not found. Please try again."

    return render(request, "weather_app/weather.html", {"weather_data": weather_data, "error_message": error_message})
