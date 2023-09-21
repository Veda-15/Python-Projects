from tkinter import *
import requests

root = Tk()
root.title = "Weather App"
root.geometry("400x400")  #size of window by default
root.resizable(0,0) #to make window size fixwed resizable(bool-width,bool-height)



def weather_details():
    API_KEY = "8def909cdbdbf962b2c6247d95e0c881"

    location = input_box.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"

    weather_data = requests.get(url).json()     # requests.get() gives response obj ,.json() parses response obj into json obj

    text_field.delete("1.0","end")
    
    if weather_data['cod'] == 200:
        # Extract the relevant data from the API response
        current_temperature = weather_data["main"]["temp"]
        current_description = weather_data["weather"][0]["description"]
        current_humidity = weather_data["main"]["humidity"]
        current_pressure = weather_data["main"]["pressure"]
        current_wind_speed = weather_data["wind"]["speed"]
        
        weather = f"Weather of: {location}\nTemperature: {current_temperature}\nHumidity: {current_humidity}\nPressure: {current_pressure}\nWind Speed: {current_wind_speed}"
    else:
        weather = f"\n\tWeather for '{location}' not found!\n\tKindly Enter valid City Name !!"
 
    text_field.insert(INSERT,weather)



label1 = Label(root, text = "Enter City Name",font="Arial 12 bold")
label1.pack(pady=10)


input_box = Entry(width = 55,borderwidth= 5)
input_box.pack()

button = Button(padx=30,pady=5,bg="light blue",fg="black",text="Check weather",command =weather_details)
button.pack(pady =20)

weather_des = Label(root,text="Weather Description: ",font = "Arial 14 bold")
weather_des.pack()

text_field = Text(root,width=45,height=10,borderwidth=5)
text_field.pack(pady = 10)


root.mainloop()
