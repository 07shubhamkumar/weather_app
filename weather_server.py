import socket
import json
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load .env file
load_dotenv()

# Read API key from environment variable
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    raise RuntimeError("OPENWEATHER_API_KEY not set. Create a .env file and set your key.")

# OpenWeatherMap API endpoint
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather_data(city_name):
    try:
        params = {
            'q': city_name,
            'appid': API_KEY,
            'units': 'metric'
        }

        response = requests.get(WEATHER_API_URL, params=params)
        if response.status_code == 200:
            data = response.json()

            weather_details = {
                "City": data['name'],
                "Temperature": f"{data['main']['temp']} °C",
                "Condition": data['weather'][0]['description'].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Pressure": f"{data['main']['pressure']} hPa",
                "Wind Speed": f"{data['wind']['speed']} m/s",
                "Sunrise": convert_unix_to_time(data['sys']['sunrise']),
                "Sunset": convert_unix_to_time(data['sys']['sunset'])
            }

            return json.dumps(weather_details, indent=4)

        else:
            return json.dumps({"Error": "City not found or API error."}, indent=4)

    except Exception as e:
        return json.dumps({"Error": f"Server error: {e}"}, indent=4)


def convert_unix_to_time(unix_timestamp):
    try:
        return datetime.fromtimestamp(unix_timestamp).strftime('%H:%M:%S')
    except:
        return "N/A"


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen(5)
    print("Server is listening on port 65432...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        city_name = client_socket.recv(1024).decode()
        print(f"Received city name: {city_name}")

        weather_info = fetch_weather_data(city_name)
        client_socket.send(weather_info.encode())

        client_socket.close()


if __name__ == "__main__":
    start_server()
