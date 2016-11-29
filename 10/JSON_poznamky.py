# repr = prevadeni na hodnoty pythonu

import json

json_retezec = """
    {
      "jméno": "Anna",
      "město": "Brno",
      "jazyky": ["čeština", "angličtina", "Python"],
      "věk": 26
    }
"""

data = json.loads(json_retezec)
print(data)
print(data['město'])

retezec = json.dumps(data, indent = 2, ensure_ascii = False)

print(retezec)


data = json.loads(retezec)
print(data)
