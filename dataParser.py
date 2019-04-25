import json
import datetime
import threading
import time
import requests

def LoadDataFileFromMap():
	neLat = "43.63706904996992"
	neLng = "-84.65892791748048"
	swLat = "45.56496912804994"
	swLng = "-84.87865447998048"
	raw_data_url = "https://beta.pogoalerts.net/raw_data.php"
	time_now = str(int(round(time.time())))

	headers = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Referer': 'https://beta.pogoalerts.net/',
	'Origin': 'https://beta.pogoalerts.net',
	'X-Requested-With': 'XMLHttpRequest',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	}

	data = {
	'timestamp': time_now,
	'login': 'true',
	'expireTimestamp': '0',
	'pokemon': 'false',
	'lastpokemon': 'false',
	'pokestops': 'false',
	'lures': 'false',
	'quests': 'true',
	'dustamount': '0',
	'reloaddustamount': 'false',
	'nests': 'false',
	'lastnests': 'false',
	'communities': 'false',
	'lastcommunities': 'false',
	'portals': 'false',
	'pois': 'false',
	'lastpois': 'false',
	'newportals': '0',
	'lastportals': 'false',
	'lastpokestops': 'false',
	'gyms': 'true',
	'lastgyms': 'true',
	'exEligible': 'false',
	'scanned': 'false',
	'lastslocs': 'false',
	'spawnpoints': 'false',
	'lastspawns': 'false',
	'minIV': '0',
	'prevMinIV': '0',
	'minLevel': '0',
	'prevMinLevel': '0',
	'bigKarp': 'false',
	'tinyRat': 'false',
	'swLat': swLat,
	'swLng': swLng,
	'neLat': neLat,
	'neLng': neLng,
	'oSwLat': swLat,
	'oSwLng': swLng,
	'oNeLat': neLat,
	'oNeLng': neLng,
	'reids': '',
	'eids': '',
	'exMinIV': '',
	'qpreids': '',
	'qpeids': '',
	'qireids': '',
	'qieids': '',
	'token': '6MKZARFtM3srrjjYLNeTcMHj0B1eKJactX3uCJUvAWI='
	}

	response = requests.post('https://beta.pogoalerts.net/raw_data.php', headers=headers, data=data)

	print(response.reason)

#pull data and process every 120 seconds
while(True):
	print('Updating...')

	LoadDataFileFromMap();

	data_file = open("raw_data.php","r") 

	raw_json = json.loads(data_file.read())

	gyms_json = raw_json['gyms']

	for gym in gyms_json:
		if(gym['raid_level'] is not None):
			print('-' * 20)
			print(gym['name'])
			if(gym['raid_pokemon_name'] is not None):
				print(gym['raid_pokemon_name'])
				end_time = datetime.datetime.fromtimestamp(gym['raid_end']/1000.0)
				print("Ends at: {:d}:{:02d}".format(end_time.hour, end_time.minute))
			else:
				print('Egg Tier: ' + gym['raid_level'])
				start_time = datetime.datetime.fromtimestamp(gym['raid_start']/1000.0)
				print("Starts at: {:d}:{:02d}".format(start_time.hour, start_time.minute))
				end_time = datetime.datetime.fromtimestamp(gym['raid_end']/1000.0)
				print("Ends at: {:d}:{:02d}".format(end_time.hour, end_time.minute))

	time.sleep(120)



'''
"gyms": [
    {
      "gym_id": "0abae9f51bf24fdbb27ac5f799f20fa4.12",
      "latitude": 43.592978,
      "longitude": -84.769662,
      "name": "Museum of Cultural and Natural History",
      "url": "https://images.weserv.nl/?url=lh4.ggpht.com/RaUHMTWYBu6ATkxy5v8JXvuLPZHavRATSqUS88ECg4efP9g0CRv4vUEL5ZrGu9c3JfaAUOIs5cFjP4GiC78",
      "last_modified": 1556073183000,
      "raid_end": 1556039094000,
      "raid_start": 0,
      "last_scanned": 1556109761000,
      "raid_pokemon_id": null,
      "guard_pokemon_id": "289",
      "slots_available": 5,
      "team_id": 1,
      "raid_level": null,
      "raid_pokemon_move_1": null,
      "raid_pokemon_move_2": null,
      "form": null,
      "raid_pokemon_cp": null,
      "park": "0",
      "pokemon": [],
      "guard_pokemon_name": "Slaking",
      "raid_pokemon_name": null,
      "sponsor": null
    }
'''