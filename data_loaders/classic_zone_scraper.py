# Webscraping library
from bs4 import BeautifulSoup
# Handles HTTP requests
import requests
# Regular expression
import re
# Time to mitigate max retries with URL
import time
# JSON
import json
# OS
import os
# Multi-threading
import threading

# Initialize response to None so it can be accessed outside of the loop
response = None
# Make a request to the page every 5 seconds to prevent the 'Connection refused' error.
while response == None:
    try:
        # GET request of wowhead's zone page
        response = requests.get('https://www.wowhead.com/zones')
    except requests.exceptions.ConnectionError:
        status_code = "Connection refused"
        time.sleep(5)
        continue
# Creates a BeautifulSoup object to parse the contents of the request
soup = BeautifulSoup(response.content, 'html.parser')

""" 
Use a regular expression to find all the IDs in the script tag inside of Listview
Example:
    <script type="..."> ... new Listview (
        {
            data: [{... ,"id":14663, ..."}], ...
        }) 
    </script>
"""
# As seen above, extract the content within the script tag and in the new Listview
script_tag = soup.find('script', string = re.compile('new Listview'))
# Convert the content to text
script_content = script_tag.text
# Use a regular expression to find all the IDs in the script content. 
zone_ids = re.findall(r'"id":(\d+)', script_content)
# Print the amount of zones found
total_ids = len(zone_ids)
print("Total number of Zones: ", total_ids)
# Will hold all valid classic zone IDs
classic_zones = []

def threading_zone(id, lock):
    # GET request to the tooltip URL for the zone and parse to text
    tooltip_url = f'https://nether.wowhead.com/tooltip/zone/{id}?dataEnv=1&locale=0'
    tooltip_response = requests.get(tooltip_url)
    tooltip_soup = BeautifulSoup(tooltip_response.content, 'html.parser')
    tooltip_text = tooltip_soup.text
    # Check if the tooltip text contains "Requires" which determines if it's from an expansion
    if 'Requires' not in tooltip_text:
    # If it does not contain "Requires" then it does not need an expansion which means it's a Classic WoW zone
        classic_zones.append(id)
    # Increment to show user progress
    with lock:
        processed_count[0] += 1
        print(str(processed_count[0]) + "/" + str(total_ids))

# Loop through all zones on the wowhead page
print("Loading data ...")
processed_count = [0]
lock = threading.Lock()
threads = []
# Create threads to increase the speed of web-scraping
for id in zone_ids:
    thread = threading.Thread(target=threading_zone, args=(id,lock,))
    thread.start()
    threads.append(thread)
# Wait for all threads to join
for thread in threads:
    thread.join()
# Total count of classic zones found
classic_zone_count = len(classic_zones)
print("Writing " + str(classic_zone_count) + " Classic WoW zone ID's to file...")
# Create a 'data' directory if it does not exist
if not os.path.exists('data'):
    os.makedirs('data')
# Write the classic_zones list to a JSON file called 'classic_zones.json' in the /data directory 
with open('data/classic_zones.json', 'w') as f:
    json.dump(classic_zones, f)
# Finished writing to file
print("Done!")