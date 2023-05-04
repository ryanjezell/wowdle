# WOWDLE (WIP)
WOWDLE is a browser-based game where players try to guess the zone in Classic WoW when given hints such as pictures, the continent, faction, and distance from the answer.


### Dependencies
- Python 3.x
- Flask
- BeautifulSoup4 
- Requests

See __requirements.txt__ for exact versions

### Installation
1. Clone the repo if you haven't already
```
git clone https://github.com/ryanjezell/wowdle.git
```

2. Install the required dependencies using pip by running the following command in your command prompt or terminal
```
pip install -r requirements.txt
```

### Running WOWDLE
1. Run these snippets of code one-by-one from top to bottom

__Windows__
```
set FLASK_APP=app.py
python -m flask run
```

__Linux/Mac__
```
export FLASK_APP=app.py
python -m flask run
```

### Reload Classic Zone IDs
1. Run the script

```
python classic_zone_scraper.py
```

2. Check the __data/classic_zones.json__ file for the list of Classic WoW zone IDs