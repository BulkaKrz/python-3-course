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

"""
# sposób 1
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()
for user in users:
    if (user["id"] in usersWithTopCompletedTask):
        print(user["id"],"-----",user['name'], "---- email:", user['email'].lower())

#sposób 2
for userId in usersWithTopCompletedTask:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId)) #- to jest jak pobieramy pojedynczy parametr
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    users = r.json()
    #print(users["name"])

"""

#sposób 3 
def change_list_into_conj_of_parameters(my_list, key="id"):
    conj_parameters = key +"="
    print(my_list)
    lastIterationNumber=len(my_list)
    i=0
    for item in my_list:
        i+=1
        if ( i==lastIterationNumber):
            conj_parameters+=str(item)
        else:
            conj_parameters+=str(item)+"&" + key + "="
    print(conj_parameters)
        
    return conj_parameters

conj_parameters = change_list_into_conj_of_parameters(usersWithTopCompletedTask)
# conj_parameters = change_list_into_conj_of_parameters([2,4,7])

r = requests.get("https://jsonplaceholder.typicode.com/users", params=conj_parameters)

users = r.json()
for user in users:
    print(user["name"])
