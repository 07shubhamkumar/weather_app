## Weather App (Client–Server Python Project)

A Python weather app that uses client-server architecture. The client is a Tkinter GUI, and the server fetches weather data from OpenWeatherMap.

Built this to learn socket programming while making something useful.

## What it does

- Shows temperature, humidity, pressure, wind speed
- Sunrise/sunset times
- Has a loading animation while fetching data
- Error handling for invalid cities

## Setup

**Get an API key** from [OpenWeatherMap](https://openweathermap.org/api)

Create a `.env` file in the project root:

OPENWEATHER_API_KEY=your_actual_key_here

Don't commit this file. It's already in `.gitignore`.

Install dependencies:
pip install -r requirements.txt

## Running it

**Terminal 1** (start server):

python weather_server_side.py

**Terminal 2** (start client):

python weather_client_side.py

Type a city name and hit enter.

Environment Variables: 
Variable -> OPENWEATHER_API_KEY
Purpose -> Your OpenWeatherMap API key

## Troubleshoot 
Tkinter Test (if GUI doesn’t open)
Use this quick test:

python - <<'PY'
import tkinter as tk
root = tk.Tk()
tk.Label(root, text="Tkinter works!").pack()
root.after(1500, root.destroy)
root.mainloop()
PY

If this opens a small window, Tkinter is installed correctly.

Credits
Weather data from OpenWeatherMap