import requests
import json
import webbrowser
import credentials

from pprint import pprint


def get_json_content_from_response(response):
    
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny adres", response.text)
    else:
        return content




def get_favourite_cats(userId):
    params = {
        "sub_id" : userId

        }

    r = requests.get('https://api.thecatapi.com/v1/favourites/', params, headers=credentials.headers)
    return get_json_content_from_response(r)


def get_random_cat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                     headers=credentials.headers)
    
    return get_json_content_from_response(r)

def add_favourite_cat(catId, userId):
    catDate = {
    "image_id": catId,
    "sub_id" : userId
   }
    r = requests.post('https://api.thecatapi.com/v1/favourites/', json = catDate,
                      headers=credentials.headers)
    return get_json_content_from_response(r)


def remove_favourite_cat(userId, favoriteCatId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/'+favoriteCatId, 
                      headers=credentials.headers)
    return get_json_content_from_response(r)



    
print("Hej zaloguj się - podaj login i hasło")
#pobranie loginu i hasła
# sprawdzamy czy login i hasło są właściwe
# logowanie zaszło poprawnie
# pobieramy z bazy danych userID i name - nazwai id użytkownika

userId = "agh2m"
name = "Arkadiusz"
i=1
print("Witaj", name)
favouriteCats = get_favourite_cats(userId)
#print("Twoje ulubione kotki to ",favouriteCats)
for cat in favouriteCats:
    print(i," - ",cat['id']," - ",cat['image']['url'])
    i+=1
   



randomCat = get_random_cat()
print("wylosowano kotka : ", randomCat[0]["url"])
addToFavourites = input("Czy chcesz go dodać do ulubionych T/N ")
if (addToFavourites.upper() == "T"):
    print(add_favourite_cat(randomCat[0]["id"], userId))
else:
    print("Nie dodałeś kotka, będzie miałczał")


favouriteCatsById = {
    favouriteCat["id"] : favouriteCat["image"]["url"]
    for favouriteCat in favouriteCats

}


print(favouriteCatsById)
favoriteCatId = input("czy chcesz usunąć kotka z ulubionych podaj jego id: ")

print(remove_favourite_cat(userId, favoriteCatId))
