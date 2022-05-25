import random

movieList = ["Tytuł 1", "Tytuł 2", "Tytuł 3", "Tytuł 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia", "losowa rzecz"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]

from collections import Counter 
print(random.choice(movieList))
print(Counter(random.choices(nagrodaZeSkrzynki,[80,15,4,1], k = 100)))
print(Counter(random.choices(nagrodaZeSkrzynki,[0.8,0.15,0.4,0.1], k = 100)))
