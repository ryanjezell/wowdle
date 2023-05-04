# Web framework
from flask import Flask, render_template
# Webscraping library
from bs4 import BeautifulSoup
# Json 
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    # Load zone IDs from JSON file
    with open('data/classic_zones.json') as f:
        classic_zones = json.load(f)
    # Sends the list of Classic WoW zone ID's to the index.html page
    return render_template('index.html', zones=classic_zones)