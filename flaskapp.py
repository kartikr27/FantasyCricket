
from logging import exception
import numpy as np
import requests
from scipy.linalg import solve

from flask import Flask, render_template, Blueprint

app = Flask(__name__)

views = Blueprint('views', __name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('dashboard.html')


@app.route('/players', methods=['GET', 'POST'])
def players_page():
    return render_template('players.html')


if __name__ == "__main__":
    app.run(True)