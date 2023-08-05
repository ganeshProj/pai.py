import requests

from datetime import datetime

# usar_api= os.environ['6b2c453784f528b0c9cff410e71bd9fd']
usar_api = '6b2c453784f528b0c9cff410e71bd9fd'
location =input("Enter the city name: ")

#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def kel_to_cel(kelvin):
    celsius = kelvin - 273.15
    return celsius

compile_api_link = "https://api.openweathermap.org/data/2.5/weather?"+"&q="+location+"&appid="+usar_api

api_link = requests.get(compile_api_link)
api_data = api_link.json()

try:
    # 'cod'=='404'
    temp_kelvin = api_data['main']['temp']
    t_celsius = kel_to_cel(temp_kelvin)
    print("The temperature of the city", location, "is : ", format(t_celsius, ".2f"), "°C")
except:

    print("Invalid city : Check your city name")
# print(api_data)