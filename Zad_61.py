import random
"""
print(random.random())
print(random.uniform(2.5,10))
print(random.randrange(10))
print(random.randrange(0,15,2))
print(random.randint(0,4))
"""

def will_wepon_hit(weponChanceToHitPercentage):
    isHitChance = random.uniform(0,100)
    if (isHitChance < weponChanceToHitPercentage):
        return "hit"
    else:
        return "miss"

listHit=[]
x=0
while x < 100:
    listHit.append(will_wepon_hit(70))
    x+=1

from collections import Counter
dictioneryHit = Counter(listHit)
print(dictioneryHit)
