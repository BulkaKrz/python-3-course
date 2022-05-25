
import random
cardList = [ "9", "9", "9", "9",
             "10", "10", "10", "10",
             "Jack", "Jack", "Jack", "Jack",
             "King", "King", "King", "King",
             "Queen", "Queen", "Queen", "Queen"
             "Ace", "Ace", "Ace", "Ace",
             "Joker", "Joker"
           ]

random.shuffle(cardList)
print(cardList)
player1 = []
player2 = []
for card in range(1,int(len(cardList)/2)+1):
    player1.append(cardList.pop())
    player2.append(cardList.pop())

print(player1)
print(player2)
print(cardList)

"""
import random
def choose_random_numbers(amount, total_amount):
    numberList = []
    while len(numberList) < amount:
        randomNumber = random.randint(1,total_amount)
        if randomNumber not in numberList:
            numberList.append(randomNumber)
    print(numberList)
        
choose_random_numbers(6,49)


def choose_random_numbers2(amount, total_amount):
    print(random.sample(range(1,total_amount+1),amount))

choose_random_numbers2(6,49)
"""
