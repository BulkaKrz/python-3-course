import requests
import json
 
r = requests.get("https://jsonplaceholder.typicode.com/todos")
#r = requests.get("https://videokurs.pl")
#tasks = json.loads(r.text)

def get_keys_with_top_values(my_dict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
        ]

def count_task_frequency(tasks):
    complitedTaskFrequencyByUser = dict()
    for entry in tasks:
        if entry["completed"] == True:
            try:
                complitedTaskFrequencyByUser[entry["userId"]] +=1
            except KeyError:
                complitedTaskFrequencyByUser[entry["userId"]] = 1
    return complitedTaskFrequencyByUser

def users_with_top_complited_task(complitedTaskFrequencyByUser):
    maxAmountOfComplitedTask = max(complitedTaskFrequencyByUser.values())
    userIDWithMaxComplitedTasks = []
    for userID, numberOfComplitedTasks in complitedTaskFrequencyByUser.items():
        if (numberOfComplitedTasks == maxAmountOfComplitedTask):
            userIDWithMaxComplitedTasks.append(userID)
    return userIDWithMaxComplitedTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    complitedTaskFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTask = users_with_top_complited_task(complitedTaskFrequencyByUser)
    for idUser in  usersWithTopCompletedTask:
        print("Wręczamy ciasteczka mistrzunia dyscypliny dla urzytkownika o id: {}" .format(idUser))
  
        a = requests.get("https://jsonplaceholder.typicode.com/users")
        users=a.json()
        for user in users:
            if (user["id"] == idUser):
                print(user["id"],"-----",user['name'], "---- email:", user['email'].lower())



