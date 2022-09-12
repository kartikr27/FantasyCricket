from pickletools import float8
from re import match
from tokenize import Double
import requests
#series id: 1075 
#add captain 2x , vice cap 1.5x and inc annnounced lineups +4






def get_player_points(match_id):
	batsmen1={}
	batsmen2={}
	bowlers1={}
	bowlers2={}
	url = "https://cricket-live-data.p.rapidapi.com/match/"+match_id

	headers = {
		"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
		"X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
	}

	data = requests.request("GET", url, headers=headers).json()

	try:
		for player in data['results']['live_details']['scorecard'][0]['batting']:
		
			bowler=False
			playerPoints=0 
			strike_rate=0.00
			name = player['player_name']
			runs = int(player['runs'])
			fours = int(player['fours'])
			sixes = int(player['sixes'])
			balls_played= int(player['balls'])

			if player['strike_rate'] != '-':
				strike_rate= float(player['strike_rate'])
		
			playerPoints += fours + sixes*2
			
			
			if runs<30 and runs>0:
				playerPoints += runs
			if runs>=30 and runs<50:
				playerPoints += runs+4
			if runs>= 50 and runs<100:
				playerPoints += runs+8
			if runs>=100:
				playerPoints += runs+16
			
			if balls_played>=10:
				if strike_rate > 170:
					playerPoints += 6
				if 150.01<=strike_rate<=170:
					playerPoints += 4
				if 130<=strike_rate<=150:
					playerPoints += 2
				if 60<=strike_rate<=70:
					playerPoints -= 2
				if 50<=strike_rate<=50.99:
					playerPoints -= 4
				if strike_rate<50:
					playerPoints -= 6


			batsmen1[name]= playerPoints
			
	except:
		print("heheheh SIUUUU 1")

	try:
		
		for player in data['results']['live_details']['scorecard'][1]['batting']:
		
			bowler=False
			playerPoints=0 
			strike_rate=0.00
			name = player['player_name']
			runs = int(player['runs'])
			fours = int(player['fours'])
			sixes = int(player['sixes'])
			balls_played= int(player['balls'])

			if player['strike_rate'] != '-':
				strike_rate= float(player['strike_rate'])
		
			playerPoints += fours + sixes*2
			
			
			if runs<30 and runs>0:
				playerPoints += runs
			if runs>=30 and runs<50:
				playerPoints += runs+4
			if runs>= 50 and runs<100:
				playerPoints += runs+8
			if runs>=100:
				playerPoints += runs+16
			
			if balls_played>=10:
				if strike_rate > 170:
					playerPoints += 6
				if 150.01<=strike_rate<=170:
					playerPoints += 4
				if 130<=strike_rate<=150:
					playerPoints += 2
				if 60<=strike_rate<=70:
					playerPoints -= 2
				if 50<=strike_rate<=50.99:
					playerPoints -= 4
				if strike_rate<50:
					playerPoints -= 6


			batsmen2[name]= playerPoints
			
	except:
		print("heheheh SIUUUU 2")

	try:
		for bowler in data['results']['live_details']['scorecard'][0]['bowling']:
			bowlerpoints= 0
			name = bowler['player_name']

			overs = float(bowler['overs'])
			wickets = int(bowler['wickets'])
			maiden = int(bowler['maidens'])
			economy= float(bowler['economy'])
			bowlerpoints += wickets*25
			if wickets==3:
				bowlerpoints+=4
			if wickets==4:
				bowlerpoints+=8
			if wickets>=5:
				bowlerpoints+=16
			
			bowlerpoints+= maiden*12

			if overs >=2:
				if economy<5:
					bowlerpoints+=6
				elif economy<=5.99:
					bowlerpoints +=4
				elif economy<=7:
					bowlerpoints +=6
				elif 10<=economy<=11:
					bowlerpoints -=2
				elif 11.01<=economy<=12:
					bowlerpoints -=4
				elif economy>12:
					bowlerpoints -=6

			bowlers1[name]=bowlerpoints
	

	except:
		print("heheheh SIUUUU 3")

	try:
		for bowler in data['results']['live_details']['scorecard'][1]['bowling']:
			bowlerpoints= 0
			name = bowler['player_name']

			overs = float(bowler['overs'])
			wickets = int(bowler['wickets'])
			maiden = int(bowler['maidens'])
			economy= float(bowler['economy'])
			bowlerpoints += wickets*25
			if wickets==3:
				bowlerpoints+=4
			if wickets==4:
				bowlerpoints+=8
			if wickets>=5:
				bowlerpoints+=16
			
			bowlerpoints+= maiden*12

			if overs >=2:
				if economy<5:
					bowlerpoints+=6
				elif economy<=5.99:
					bowlerpoints +=4
				elif economy<=7:
					bowlerpoints +=6
				elif 10<=economy<=11:
					bowlerpoints -=2
				elif 11.01<=economy<=12:
					bowlerpoints -=4
				elif economy>12:
					bowlerpoints -=6

			bowlers2[name]=bowlerpoints
	except:
		print("heheheh SIUUUU 4")
	return batsmen1,batsmen2,bowlers1, bowlers2
#gets players in squad
# for thing in data['results']['live_details']['teamsheets']['home']:
# 	print(thing) 
# print(batsmen1)
# print(batsmen2)
# print(bowlers1)
# print(bowlers2)