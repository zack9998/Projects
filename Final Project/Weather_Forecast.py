import tkinter as tk
import requests

#function to dislay wheather informations 
import requests

def display_wether_info():
    city = entry.get().strip()
    api_key = "63605cf3e80711e4c10cbe31a50f9796"
    url = "http://api.openweathermap.org/data/2.5/weather"
    headers = {"apikey": api_key}
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
        }  
    response = requests.get(url, params=params)
    if city :
        if response.status_code == 200 :
            data = response.json()
            Temperature.config(text=f'Temperature : {data["main"]["temp"]} C')
            Humidity.config(text = f'Humidity : {data["main"]["humidity"]} %')
            Wind_Speed.config(text=f'Wind_Speed : {data["wind"]["speed"]}km/h')
            Pressure.config(text = f'Pressure :{data["main"]["pressure"]} hPa')
            if "rain" in data:
                precipitation = data["rain"].get("1h", 0)  # Default to 0 if "1h" key is missing
            elif "snow" in data:
                precipitation = data["snow"].get("1h", 0)  # Default to 0 if "1h" key is missing
            else:
                precipitation = 0
            Precipitation.config(text =f"Precipitation : {precipitation} %")
        else :
            print("Failed to retrieve data:", response.status_code)
    else : 
        Temperature.config(text='Temperature')
        Humidity.config(text='Humidity')
        Wind_Speed.config(text='Wind Speed')
        Pressure.config(text='Pressure')
        Precipitation.config(text='Precipitation')

#GUI Creatio,
root = tk.Tk()
root.geometry("400x400")
root.title("Weather Forecast")


#Input creation
label = tk.Label(root, text="Location : ")
label.grid(column=0,row=0)
entry = tk.Entry(root)
entry.grid(column=1,row=0)

#Output Declaration
Temperature = tk.Label(root, text="Temperature:")
Temperature.grid(column=0, row=1, pady=5)
Humidity = tk.Label(root, text="Humidity:")
Humidity.grid(column=0, row=2, pady=5)
Wind_Speed = tk.Label(root, text="Wind Speed:")
Wind_Speed.grid(column=0, row=3, pady=5)
Pressure = tk.Label(root, text="Pressure:")
Pressure.grid(column=0, row=4, pady=5)
Precipitation = tk.Label(root, text="Precipitation:")
Precipitation.grid(column=0, row=5, pady=5)


#Button creation
button = tk.Button(root,text="Search ",command=display_wether_info)
button.grid(column=2,row=0, padx=15 , pady=15)


root.mainloop()