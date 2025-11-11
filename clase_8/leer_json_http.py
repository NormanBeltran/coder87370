import json
import requests


api = 'https://apis.datos.gob.ar/georef/api/provincias?nombre=Sgo. del Estero'
response = requests.get(api)

response.raise_for_status()

data = response.json()
print(data)