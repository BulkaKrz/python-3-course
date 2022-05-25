import requests
import json
import webbrowser
from pprint import pprint

params = {
    "breed_id": "aege",
    "limit": 3
}



r = requests.get("https://api.thecatapi.com/v1/images/search",params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny adres")
else:
    for cat in content:
        print(cat)
        webbrowser.open_new_tab(cat["url"])
    
    


