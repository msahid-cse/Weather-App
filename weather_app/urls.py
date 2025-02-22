from django.urls import path
from .views import weather_view

urlpatterns = [
    path('', weather_view, name='weather'),  # Show weather page at homepage
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.weather_view, name='weather'),
#     path('today/', views.today_weather, name='today_weather'),
#     path('next-week/', views.next_week_weather, name='next_week_weather'),
#     path('next-month/', views.next_month_weather, name='next_month_weather'),
#     path('previous-week/', views.previous_week_weather, name='previous_week_weather'),
#     path('previous-month/', views.previous_month_weather, name='previous_month_weather'),
#     path('yearly-prediction/', views.yearly_prediction, name='yearly_prediction'),
# ]

