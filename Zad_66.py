"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""

import random
from enum import Enum

def findApproximateValue(value, percentRange):
    lowestValue = value - (percentRange/100) * value
    higestValue = value + (percentRange/100) * value
    return random.randint(lowestValue,higestValue)





Event = Enum("Event",["Chest", "Empty"])

eventDictionary = {
                    Event.Chest : 0.6,
                    Event.Empty : 0.4
                    }
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

Colors = Enum("Colors",{"green":"zielony",
                        "orange":"pomarańczowy",
                        "purple":"fiolet",
                        "gold":"złoty"
                        }
              )
              

chestColoursDictionary = {
                    Colors.green : 0.75,
                    Colors.orange : 0.2,
                    Colors.purple : 0.04,
                    Colors.gold : 0.01
                    }

chestColoursList = tuple(chestColoursDictionary.keys())
chestColoursProbability = tuple(chestColoursDictionary.values())

rewardForChest = {
                chestColoursList[reward]: (reward + 1) * (reward + 1) * 1000
                for reward in range(len(chestColoursList))
    }


gameLenght = 5
goldAcquired = 0

print("Welcom to ma game go stright")
print("you hahe only 5 steps to make")
while gameLenght > 0:
    gameAnswer = input("Do you want to move forward?")
    if gameAnswer == "yes":
        print("Great, let's see what you got ...")
        dravnEvent = random.choices(eventList,eventProbability)[0]
        if dravnEvent == Event.Chest:
            print("You find a chest :-)")
            drawnChest = random.choices(chestColoursList,chestColoursProbability)[0]
            print("The chest color chest is", drawnChest.value)
            gameReward = findApproximateValue(rewardForChest[drawnChest], 10)
            goldAcquired = goldAcquired + gameReward
            print("You find in the chest",gameReward,"gold")
            
        elif dravnEvent == Event.Empty:
            print("You've drawn nothing, you are so unlucky :-(")

       
    else:
        print("You can go just stright man, nothing else, this game is dump")
        continue
        
    
    gameLenght = gameLenght -1


print("congratulation, you have acquired: ", goldAcquired ,"gold")





























    
