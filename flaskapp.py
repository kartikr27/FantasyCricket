

from flask import Flask, render_template, request, Blueprint
import requests
import players

app = Flask(__name__)

views = Blueprint('views', __name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    bat1={}
    # bat1, bat2, bowl1,bowl2=[],[],[],[]
    if request.method == 'POST':
        match_id=request.form.get('match_id')
        bat1, bat2, bowl1,bowl2 = players.get_player_points(match_id)
    return render_template('dashboard.html',batsmen1=bat1,batsmen2=bat2,bowlers1=bowl1,bowlers2=bowl2,matchID=match_id)


@app.route('/players', methods=['GET', 'POST'])
def players_page():
    return render_template('players.html')


if __name__ == "__main__":
    app.run(debug=True)