import requests
from datetime import datetime

api_key = '01eed2dda00f969afcfad57deea61294'
location = input("enter city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data=api_link.json()

temp_city =((api_data['main']['temp'])-273.15)
weather_desc =api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time= datetime.now().strftime(" %d %b %Y | %I:%M:%S %P")

#Explicitly print to file method
with open("info.txt","a") as f:
    
    print ("-------------------------------------------------------------",file=f)
    print("Weather stats for - {} || {}".format(location.upper(), date_time),file=f)
    print ("-------------------------------------------------------------",file=f)
    print("Current temperature is : {:.2f} deg C".format(temp_city),file=f)
    print("Current Weather desc   :",weather_desc,file=f)
    print("Current Humidity       :",hmdt,'%',file=f)
    print("Current wind speed     :",wind_speed,'kmph',file=f)
    print("",file=f)

