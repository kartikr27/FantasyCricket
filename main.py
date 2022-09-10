from logging import exception
from winreg import QueryReflectionKey
import numpy as np
import requests
from scipy.linalg import solve

auth = "1g6uUwh0HPiddRjSu6vUZLt3dRKokTKpgD0m3RdOC8KcqtDXv5Qi0Z2GvjE5I6RD"

headers={'X-TBA-Auth-Key': auth}

team_api = "https://www.thebluealliance.com/api/v3/event/2022hop/teams/simple"
match_api = "https://www.thebluealliance.com/api/v3/team/frc624/event/2022hop/matches/simple"

teams = [team['team_number'] for team in requests.get(url=team_api, headers=headers).json()]

match = [team['key'] for team in requests.get(url=match_api, headers=headers).json()]

matches = [team['key'] for team in requests.get(url=match_api, headers=headers).json()]
score = "https://unofficial-cricbuzz.p.rapidapi.com/matches/get-scorecard"

overs = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/48431/overs"



querystring = {"matchId":"49871"}

headers = {
	"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
	"X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com"
}

data = requests.get(url=score, headers=headers, params=querystring).json()


print(data)

try:
	
	for player in data['scorecard'][0]['batsman']:
		
		bowler=False
		playerPoints=0 
		name = player['name']
		runs = int(player['runs'])
		try:
			fours = int(player['fours'])
			sixes = int(player['sixes'])
			playerPoints += fours + sixes*2
		except:
			pass
		
		if runs<30 and runs>0:
			playerPoints += runs
		if runs>=30 and runs<50:
			playerPoints += runs+4
		if runs>= 50 and runs<100:
			playerPoints += runs+8
		if runs>=100:
			playerPoints += runs+16

	
		print(name, playerPoints)
	
		
except:
	for bowler in data['scorecard'][1]['bowler']:
		
		bowlerpoints= 0
		name = bowler['name']
		try:
			wickets = int(bowler['wickets'])
			bowlerpoints += wickets*25
			print(name,bowlerpoints)
			if wickets==3:
				bowlerpoints+=4
			if wickets==4:
				bowlerpoints+=8
			if wickets>=5:
				bowlerpoints+=16
			
		except:
			print(name,bowlerpoints)

		
# score = "https://unofficial-cricbuzz.p.rapidapi.com/matches/get-scorecard"

# overs = "https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/48431/overs"



# querystring = {"matchId":"48431"}

# headers = {
# 	"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
# 	"X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com"
# }

# data = requests.get(url=score, headers=headers, params=querystring).json()
# print(data)