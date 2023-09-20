from django.shortcuts import render
import requests, datetime
from decouple import config

# Use the config function to get the API key from the environment variable
API_key = config("API_KEY")


# Create your views here.
def home(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get("cityInput")
        if city:
            weather_data = API_Request(API_key, city)
            # "Error: No Matching Location Found."
            if not weather_data:
                weather_data = {"Error": "No matching location found."}
            # print(weather_data)
            # print(weather_data.get("city"))
            # weather_text = weather_data.items
            # weather_text = weather_text.ite
        else:
            weather_data = {weather_data: "No city was found"}
            weather_data = "No city was found"
    # print(weather_data)
    return render(
        request,
        "home.html",
        {"weather_data": weather_data},
    )


import requests
import datetime


def is_valid_city(city):
    if not city or len(city) <= 1:
        return False
    if not all(char.isalpha() or char.isspace() for char in city):
        return False
    if len(city.strip()) == 1:
        return False
    if len(city) > 50:
        return False
    if city.strip() != city:
        return False
    if "  " in city:
        return False
    return True


def API_Request(key, city):
    if not is_valid_city(city):
        return False  # "Error: No Matching Location Found."

    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return f"Error: {data['error']['message']}"

    city_name = data["location"]["name"]
    country_name = data["location"]["country"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    Humidity = data["current"]["humidity"]
    Wind = data["current"]["wind_kph"]
    time = data["current"]["last_updated"]
    feelLike = data["current"]["feelslike_f"]
    formatted_time = datetime.datetime.fromtimestamp(feelLike).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    formatted_time = datetime.datetime.now()
    obj = {
        "city": city_name,
        "country": country_name,
        "temperature": temperature,
        "condition": condition,
        "Humidity": Humidity,
        "Wind": Wind,
        "time": formatted_time,
        "feelLike": feelLike,
    }
    return obj  # print(object, data["current"])
