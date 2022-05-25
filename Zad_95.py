import requests
import json
import webbrowser
from pprint import pprint

params = {
    "api_key" : "b202bef085d9c34cc517fc7d71221fbcfa308d4f",
    "country" : "pl",
    "year" : 2022,
    "month" : 12
    
}



r = requests.get("https://calendarific.com/api/v2/holidays/",params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny adres")
else:
    pprint(content)
        
    


