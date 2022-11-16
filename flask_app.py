
import math
from flask import Flask, render_template, request, Blueprint
import requests
import players,free_agents,loginFile

app = Flask(__name__)

views = Blueprint('views', __name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    print("LOGIN")
    user=""
    password=""
    name=""
    newuser1=""
    newpassword1=""
    fullname=""
    if request.method == 'POST':
        user1=request.form.get('user')
        password=request.form.get('password')
        newuser1 = request.form.get('newuser')
        newpassword1 = request.form.get('newpassword')
        fullname = request.form.get("fullname")
        if newuser1 != None:
            loginFile.add_new(newuser1,newpassword1,fullname)
        else:
            name=loginFile.get_interface(user1,password)
        print("success")
        print(newuser1, newpassword1)
        if name=="":
            name="Please Create an Account"
    return render_template('login.html',fullname1=fullname,name1=name,newU1=newuser1,newP1=newpassword1)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    bat1={}
    bat2={}
    bowl1={}
    bowl2={}
    match_id=""
    if request.method == 'POST':
        match_id=request.form.get('match_id')
        bat1,bat2,bowl1,bowl2 = players.get_player_points(match_id)
        print(match_id)
    return render_template('dashboard.html',batsmen1=bat1,batsmen2=bat2,bowlers1=bowl1,bowlers2=bowl2,matchID=match_id)


@app.route('/players', methods=['GET', 'POST'])
def players_page():
    country =""
    players=[]
    if request.method == 'POST':
        country = request.form.get('country')
        players = free_agents.get_players_country(country)
    return render_template('players.html',country1=country,players1=players)


if __name__ == "__main__":
    app.run(debug=True)