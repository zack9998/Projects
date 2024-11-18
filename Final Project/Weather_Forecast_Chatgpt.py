import tkinter as tk
import requests

# Function to display weather information
def display_weather_info():
    city = entry.get().strip()
    if not city:
        status_label.config(text="Please enter a city name.", fg="red")
        clear_labels()
        return

    api_key = "63605cf3e80711e4c10cbe31a50f9796"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # to get temperature in Celsius
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Display weather data
        Temperature.config(text=f'Temperature: {data["main"]["temp"]} °C')
        Humidity.config(text=f'Humidity: {data["main"]["humidity"]} %')
        Wind_Speed.config(text=f'Wind Speed: {data["wind"]["speed"]} km/h')
        Pressure.config(text=f'Pressure: {data["main"]["pressure"]} hPa')

        # Handle precipitation
        if "rain" in data:
            precipitation = data["rain"].get("1h", 0)
        elif "snow" in data:
            precipitation = data["snow"].get("1h", 0)
        else:
            precipitation = 0
        Precipitation.config(text=f'Precipitation: {precipitation} mm')
        
        # Clear status label on success
        status_label.config(text="Weather data retrieved successfully.", fg="green")

    except requests.exceptions.RequestException as e:
        # Handle any errors with the API request
        status_label.config(text="Error retrieving data. Check city name.", fg="red")
        clear_labels()

# Helper function to clear output labels
def clear_labels():
    Temperature.config(text="Temperature:")
    Humidity.config(text="Humidity:")
    Wind_Speed.config(text="Wind Speed:")
    Pressure.config(text="Pressure:")
    Precipitation.config(text="Precipitation:")

# GUI Setup
root = tk.Tk()
root.geometry("400x400")
root.title("Weather Forecast")

# Input creation
label = tk.Label(root, text="Location:")
label.grid(column=0, row=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(column=1, row=0, padx=10, pady=10)

# Status message label for errors or success messages
status_label = tk.Label(root, text="", fg="green")
status_label.grid(column=0, row=1, columnspan=3)

# Output Declaration
Temperature = tk.Label(root, text="Temperature:")
Temperature.grid(column=0, row=2, pady=5)
Humidity = tk.Label(root, text="Humidity:")
Humidity.grid(column=0, row=3, pady=5)
Wind_Speed = tk.Label(root, text="Wind Speed:")
Wind_Speed.grid(column=0, row=4, pady=5)
Pressure = tk.Label(root, text="Pressure:")
Pressure.grid(column=0, row=5, pady=5)
Precipitation = tk.Label(root, text="Precipitation:")
Precipitation.grid(column=0, row=6, pady=5)

# Button creation
button = tk.Button(root, text="Search", command=display_weather_info)
button.grid(column=2, row=0, padx=15, pady=15)

root.mainloop()
