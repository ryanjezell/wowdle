# WOWDLE (WIP)
WOWDLE is a browser-based game where players try to guess the zone in Classic WoW when given hints such as a picture, the continent, faction, and distance.


## Dependencies
- Python 3.x
- BeautifulSoup4 
- Requests

See __requirements.txt__ for exact versions


## Reload Classic Zone IDs
1. Run the script
    ```
    python classic_zone_scraper.py
    ```
2. Wait for the script to complete
3. Check the __data/classic_zones.json__ file for the list of Classic WoW zone IDs