import requests
import json

URL = 'http://192.168.1.137:3245/'

datos = requests.get(url=URL)
print(datos.text)

POST_DATA = {"label": "Mi Segundo POST",
             "done": True}
POST_DATA = json.dumps(POST_DATA)
datos = requests.post(url=URL+'//todos',json=POST_DATA)
print(datos.text)

URL = 'http://192.168.1.137:3245/'

datos = requests.get(url=URL)
print(datos.text)