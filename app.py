# Web framework
from flask import Flask, render_template
# Webscraping library
from bs4 import BeautifulSoup
# Handles HTTP requests
import requests

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    # Make a request to the zones page
    response = requests.get('https://www.wowhead.com/zones')
    # Creates a BeautifulSoup object to parse the contents of the request
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all anchor elements <a> with the class 'listview-cleartext' which contains the zone ID's
    zone_links = soup.select('a.listview-cleartext')
    # Will hold the zones from Classic WoW
    zones = []
    # Filter out zones that require an expansion
    for link in zone_links:
        # Grab the ID of the zone from the link
        # Example link: href="https://www.wowhead.com/zone=14663/aberrus-the-shadowed-crucible"
        # 'link' corresponds to the <a> tag 
        # ['href'] returns the URL within it
        # .split('/') will split it by '/' which results in: ["https:", "", "www.wowhead.com", "zone=14663", "aberrus-the-shadowed-crucible"]
        # We'll end up with "zone=14663"
        zone_id_part = link['href'].split('/')[3]
        # Only grab ID so we split by '='
        zone_id = zone_id_part.split('=')[1]
        # Make GET request
        zones.append(zone_id)
        print ("Appending: " + zone_id)
    for id in zones:
        print(id)
    # Render template and initialize zones_web to zones   
    return render_template('index.html', zones_web=zones)