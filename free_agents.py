
import requests

url = "https://cricket-live-data.p.rapidapi.com/fixtures-by-date/2022-10-17"

headers = {
	"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
	"X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
}

data = requests.request("GET", url, headers=headers).json()

def get_match_data(match_id):
	url = "https://cricket-live-data.p.rapidapi.com/match/"+match_id

	headers = {
		"X-RapidAPI-Key": "772de23cf7mshad02bab176a4375p11e056jsn158ef8de72e1",
		"X-RapidAPI-Host": "cricket-live-data.p.rapidapi.com"
	}
p_South_Africa = ['Temba Bavuma', ' Quinton de Kock', ' Heinrich Klaasen', ' Reeza Hendricks', ' Keshav Maharaj', ' Aiden Markram', ' David Miller', ' Lungi Ngidi', ' Anrich Nortje', ' Wayne Parnell', ' Kagiso Rabada', ' Rillee Rossouw', ' Tabraiz Shamsi', ' Tristan Stubbs', 'Bjorn Fortuin', ' Marco Jansen', ' Andile Phehlukwayo']
p_Pakistan=['Babar Azam', 'Shadab Khan', 'Asif Ali', 'Haider Ali', 'Haris Rauf', 'Iftikhar Ahmed', 'Khushdil Shah', 'Mohammad Hasnain', 'Mohammad Nawaz', 'Mohammad Rizwan', 'Mohammad Wasim', 'Naseem Shah', 'Shaheen Shah Afridi', 'Shan Masood', 'Usman Qadir,Fakhar Zaman', 'Mohammad Haris', 'Shahnawaz Dahani']
p_India = ['Rohit Sharma', ' KL Rahul', ' Virat Kohli', ' Suryakumar Yadav', ' Deepak Hooda', ' Rishabh Pant', ' Dinesh Karthik', ' Hardik Pandya', ' R Ashwin', ' Yuzvendra Chahal', ' Axar Patel', ' Bhuvneshwar Kumar', ' Harshal Patel', ' Arshdeep Singh. Standby Players: Mohammad Shami', ' Shreyas Iyer', ' Ravi Bishnoi', ' Deepak Chahar']
p_Bangladesh = ['Shakib Al Hasan', ' Sabbir Rahman', ' Mehidy Hasan Miraz', ' Afif Hossain', ' Mossadek Hossain', ' Litton Das', ' Yasir Ali', ' Nurul Hasan', ' Mustafizur Rahman', ' Saifuddin', ' Taskin Ahmed', ' Ebadot Hossain', ' Hasan Mahmud', ' Najmul Hossain', ' Nasum Ahmed', ' Shoriful Islam', ' Shak Mahedi Hasan', ' Rishad Hossain', ' Soumya Sarkar']
p_New_Zealand = ['Kane Williamson', 'Tim Southee', 'Ish Sodhi', 'Mitchell Santner', 'Glenn Phillips', 'Jimmy Neesham', 'Daryl Mitchell', 'Adam Milne', 'Martin Guptill', 'Lachlan Ferguson', 'Devon Conway', 'Mark Chapman', 'Michael Bracewell', 'Trent Boult', 'Finn Allen'] 
p_England= ['Jos Buttler', 'Moeen Ali', 'Harry Brook', 'Sam Curran', 'Chris Jordan', 'Liam Livingstone', 'Dawid Malan', 'Adil Rashid', 'Phil Salt', 'Ben Stokes', 'Reece Topley', 'David Willey', 'Chris Woakes', 'Mark Wood', 'Alex Hales', 'Liam Dawson', 'Richard Gleeson', 'Tymal Mills']
p_Australia= ['Aaron Finch', 'Ashton Agar', 'Pat Cummins', 'Tim David', 'Josh Hazlewood', 'Josh Inglis', 'Mitchell Marsh', 'Glenn Maxwell', 'Kane Richardson', 'Steven Smith', 'Mitchell Starc', 'Marcus Stoinis', 'Matthew Wade', 'David Warner', 'Adam Zampa']
p_Afghanistan=['Mohammad Nabi', 'Najibullah Zadran', 'Rahmanullah Gurbaz', 'Azmatullah Omarzai', 'Darwish Rasooli', 'Farid Ahmad Malik', 'Fazal Haq Farooqi', 'Hazratullah Zazai', 'Ibrahim Zadran', 'Mujeeb ur Rahman', 'Naveen ul Haq', 'Qais Ahmad', 'Rashid Khan', 'Salim Safi', 'Usman Ghani. Standby Players: Afsar Zazai', 'Sharafuddin Ashraf', 'Rahmat Shah', 'Gulbadin Naib']

teams = ["South Africa",'Pakistan','India','Bangladesh','New Zealand','England','Australia','Afghanistan']
team_player_list = [p_South_Africa,p_Pakistan,p_India,p_Bangladesh,p_New_Zealand,p_England,p_Australia,p_Afghanistan]
def get_players_country(country):
    index = teams.index(country)
    return team_player_list[index] 

# def get_specific_player(player_name):
#     for team in team_player_list:
#         for player in team:
#             if player_name==player:
#                 return player