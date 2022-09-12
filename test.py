
import requests

url = "https://cricket-live-data.p.rapidapi.com/fixtures-by-series/1053"
# url = "https://cricket-live-data.p.rapidapi.com/fixtures-by-date/2022-09-11"
# url = "https://cricket-live-data.p.rapidapi.com/results-by-date/2020-09-20"

headers = {
	"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
	"X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
}

data = requests.request("GET", url, headers=headers).json()

for matchID in data['results']:
    print(matchID['id'])

#t20 WC cup- 1075
#Asia cup- 1053