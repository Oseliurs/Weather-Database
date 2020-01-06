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

GetCode()
