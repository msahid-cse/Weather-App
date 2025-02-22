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





# from django.shortcuts import render
# import requests

# # OpenWeather API Key (Replace with your key)
# API_KEY = "b5ae4a84e5d2a9849a1aabf7978e7567"

# def get_weather_data(city):
#     """Fetch weather data from OpenWeather API"""
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return {
#             'city': data['name'],
#             'temperature': data['main']['temp'],
#             'description': data['weather'][0]['description'],
#             'humidity': data['main']['humidity'],
#             'wind_speed': data['wind']['speed'],
#             'icon': data['weather'][0]['icon']
#         }
#     return None

# def weather_view(request):
#     """Main weather view"""
#     weather_data = None
#     error_message = None

#     if request.method == "POST":
#         city = request.POST.get("city")
#         weather_data = get_weather_data(city)
#         if not weather_data:
#             error_message = "City not found. Please try again."

#     return render(request, "weather_app/weather.html", {"weather_data": weather_data, "error_message": error_message})

# # Separate views for each menu option
# def today_weather(request):
#     return render(request, "weather_app/today_weather.html")

# def next_week_weather(request):
#     return render(request, "weather_app/next_week_weather.html")

# def next_month_weather(request):
#     return render(request, "weather_app/next_month_weather.html")

# def previous_week_weather(request):
#     return render(request, "weather_app/previous_week_weather.html")

# def previous_month_weather(request):
#     return render(request, "weather_app/previous_month_weather.html")

# def yearly_prediction(request):
#     return render(request, "weather_app/yearly_prediction.html")


# import requests
# from django.shortcuts import render

# API_KEY = "b5ae4a84e5d2a9849a1aabf7978e7567"  # Replace with your actual API key
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# def get_weather_data(city):
#     params = {"q": city, "appid": API_KEY, "units": "metric"}
#     response = requests.get(BASE_URL, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         weather_data = {
#             "city": data["name"],
#             "temperature": data["main"]["temp"],
#             "description": data["weather"][0]["description"],
#             "humidity": data["main"]["humidity"],
#             "wind_speed": data["wind"]["speed"],
#             "icon": data["weather"][0]["icon"],
#         }
#         return weather_data
#     return None

# def weather_view(request):
#     weather_data = None
#     error_message = None
#     if request.method == "POST":
#         city = request.POST.get("city")
#         weather_data = get_weather_data(city)
#         if not weather_data:
#             error_message = "City not found! Please enter a valid city."
#     return render(request, "weather_app/today_weather.html", {"weather_data": weather_data, "error_message": error_message})

# def today_weather(request):
#     return render(request, "weather_app/today_weather.html", {"weather_data": weather_data, "error_message": error_message})

# def next_week_weather(request):
#     return render(request, "weather_app/next_week_weather.html")

# def next_month_weather(request):
#     return render(request, "weather_app/next_month_weather.html")

# def previous_week_weather(request):
#     return render(request, "weather_app/previous_week_weather.html")

# def previous_month_weather(request):
#     return render(request, "weather_app/previous_month_weather.html")

# def yearly_prediction(request):
#     return render(request, "weather_app/yearly_prediction.html")
