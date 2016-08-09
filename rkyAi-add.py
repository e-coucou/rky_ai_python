import requests
import json
import csv
from geopy.geocoders import Nominatim

geocoder = Nominatim()
fo = file('Var.csv','r')
headers = {'content-type': 'application/json'}
url = 'https://rkyai.herokuapp.com/api/v1/map'

for ligne in fo:
	commune = ligne.split(",")[0]
	address, (latitude, longitude)  = geocoder.geocode(commune, True, 30)
	payload = {"profil":{"user":"Python_Test"}, "latitude":repr(latitude), "longitude":repr(longitude)}
#	print(payload)
	r = requests.post(url=url,headers=headers, data = json.dumps(payload))
	print(r.json())#	print(latitude,longitude)

#adresse = "45 rue de vouille, Paris, France"
#address, (latitude, longitude)  = geocoder.geocode(adresse, True, 30)
#print(latitude,longitude)
#payload = {"profil":{"user":"Python_Test"}, "latitude":repr(latitude), "longitude":repr(longitude)}
#print(payload)

#r = requests.post(url=url,headers=headers, data = json.dumps(payload))
#print(r.json())