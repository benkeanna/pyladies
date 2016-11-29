import requests
import json

with open('token.txt', encoding='utf-8') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token} # musi byt takhle

odpoved = requests.get('http://api.github.com/user', headers = headers)

odpoved.raise_for_status()
print(odpoved.text)
print(odpoved.status_code)

data = json.loads(odpoved.text)
print(odpoved)

print(json.dumps(data, indent = 2))
print(data['email'])

odpoved = requests.put('https://api.github.com/user/starred/pyladiescz/pyladies.cz', headers=headers)

odpoved.raise_for_status()
