import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

timeBefore = timedelta(days = 30)
searchDate = datetime.today() - timeBefore

print(int(searchDate.timestamp()))


params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : int(searchDate.timestamp()),
    "tagged" : "python",
    "min" : 10
    }



r = requests.get("https://api.stackexchange.com/2.3/questions",params)


try:
    questions = r.json()

except json.decoder.JSONDencodeError:
    print("NIepoprawny adres")
else:
    for question in questions["items"]:
        print(question["title"]+ " score: "+ str(question["score"]))
      #  webbrowser.open_new_tab(question["link"])


