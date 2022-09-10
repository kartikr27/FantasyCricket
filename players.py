# import numpy as np
# import requests

# score = "https://unofficial-cricbuzz.p.rapidapi.com/matches/get-scorecard"

# overs = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/48431/overs"



# querystring = {"matchId":"800451"}

# headers = {
# 	"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
# 	"X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com"
# }

# data = requests.get(url=score, headers=headers, params=querystring).json()
# batsmen={}
# bowlers={}

# try:
	
# 	for player in data['scorecard'][0]['batsman']:
		
# 		bowler=False
# 		playerPoints=0 
# 		name = player['name']
# 		runs = int(player['runs'])
# 		try:
# 			fours = int(player['fours'])
# 			sixes = int(player['sixes'])
# 			playerPoints += fours + sixes*2
# 		except:
# 			pass
		
# 		if runs<30 and runs>0:
# 			playerPoints += runs
# 		if runs>=30 and runs<50:
# 			playerPoints += runs+4
# 		if runs>= 50 and runs<100:
# 			playerPoints += runs+8
# 		if runs>=100:
# 			playerPoints += runs+16
# 		batsmen[name]= playerPoints

# except Exception:
# 	for bowler in data['scorecard'][1]['bowler']:
		
# 		bowlerpoints= 0
# 		name = bowler['name']
# 		try:
# 			wickets = int(bowler['wickets'])
# 			bowlerpoints += wickets*25
# 			print(name,bowlerpoints)
# 			if wickets==3:
# 				bowlerpoints+=4
# 			if wickets==4:
# 				bowlerpoints+=8
# 			if wickets>=5:
# 				bowlerpoints+=16
			
# 		except:
# 			pass
# 		bowlers[name]=bowlerpoints


# print(batsmen)
# print(bowlers)

import requests

url = "https://cricket-live-data.p.rapidapi.com/match/51259"

headers = {
	"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
	"X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)