import requests
import json

api = "PUT_YOUR_API_KEY_HERE_!!!"

def GetCode():

    user = input("Type the City Code of your City ...\n")
    req = requests.get("http://dataservice.accuweather.com/locations/v1/search?q=" + user + "&apikey=" + api)
    jfile = json.loads(req.text)

    for i in range( len(jfile) ):
        print( str(i) + ": " + jfile[i]["LocalizedName"] )

    choice = input("Choose the number corresponding to your City ...\n")
    print(jfile[int(choice)]["Key"])
    return jfile[int(choice)]["Key"]

def GetWeather(Code):

    req = requests.get("http://dataservice.accuweather.com/currentconditions/v1/" + Code + "?apikey=" + api + "&details=true")
    jfile = json.loads(req.text)

    print("In the City with the code " + Code + " the weather is " + jfile[0]["WeatherText"] + ".")
    print("The Temperature is " + str( jfile[0]["Temperature"]["Metric"]["Value"] ) + "°C with a feeling temperature of " + str( jfile[0]["RealFeelTemperature"]["Metric"]["Value"] ) + "°C")
    print("The wind is blowing at " + str( jfile[0]["Wind"]["Speed"]["Metric"]["Value"] ) + " km/h in the " + str( jfile[0]["Wind"]["Direction"]["English"] ) + " direction (" + str( jfile[0]["Wind"]["Direction"]["Degrees"] ) + ")")

    print(jfile)

GetCode()
