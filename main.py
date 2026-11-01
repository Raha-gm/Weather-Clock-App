import requests
from customtkinter import *
from datetime import *

# City coordinates
cities = {
    "Tehran": {"latitude": 35.6892, "longitude": 51.3890},
    "Tabriz": {"latitude": 38.0962, "longitude": 46.2738},
    "Gilan": {"latitude": 37.2761, "longitude": 49.5886},
    "Isfahan": {"latitude": 32.6525, "longitude": 51.6746},
    "Shiraz": {"latitude": 29.6103, "longitude": 52.5311},
    "Mashhad": {"latitude": 36.2972, "longitude": 59.6067},
    "Ahvaz": {"latitude": 31.3183, "longitude": 48.6706},
    "Sari": {"latitude": 36.5633, "longitude": 53.0601},
    "Urmia": {"latitude": 37.5527, "longitude": 45.0760}
}


# Convert weather codes into readable descriptions
def get_weather_text(code):
    weather_codes = {
        0: "Clear",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Freezing fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Heavy rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Severe thunderstorm"
    }

    return weather_codes.get(code, "Unknown")


# Get weather information for the selected city
def update_weather():
    city_name = city_menu.get()
    location = cities[city_name]

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={location['latitude']}&longitude={location['longitude']}"
        f"&current=temperature_2m,weather_code&timezone=auto"
    )

    try:
        data = requests.get(url, timeout=10).json()["current"]

        temp = data["temperature_2m"]
        code = data["weather_code"]
        condition = get_weather_text(code)

        weather_label.configure(
            text=f"{temp}°C - {condition}",
            text_color="#008CFF"
        )

    except (requests.RequestException, KeyError, ValueError):
        weather_label.configure(
            text="Unable to connect to the internet",
            text_color="#FF0000"
        )


# Update the digital clock every second
def update_clock():
    now = datetime.now().strftime("%H:%M:%S")
    clock_label.configure(text=now)
    window.after(1000, update_clock)


# Create the main application window
window = CTk()
window.geometry("350x400")

CTkLabel(
    window,
    text="Clock",
    text_color="#FFDD00",
    font=("Morabba", 25)
).pack(pady=10)

clock_label = CTkLabel(
    window,
    text="00:00:00",
    font=("Morabba", 25),
    text_color="#FFDD00"
)
clock_label.pack(pady=5)

update_clock()

# Weather section
CTkLabel(
    window,
    text="Weather",
    text_color="#008CFF",
    font=("Morabba", 25)
).pack(pady=10)

city_menu = CTkOptionMenu(
    window,
    values=list(cities.keys()),
    font=("Morabba", 15)
)
city_menu.pack(pady=5)

weather_label = CTkLabel(
    window,
    text="Temperature",
    text_color="#008CFF",
    font=("Morabba", 25)
)
weather_label.pack(pady=10)

# Button to get the weather information
btn = CTkButton(
    window,
    text="Get Weather",
    font=("Morabba", 15),
    fg_color="#008CFF",
    command=update_weather
)
btn.pack(pady=10)

# Run the application
window.mainloop()