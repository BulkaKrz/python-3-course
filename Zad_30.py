"""
# Krotki
krotka1 = 1,2,3,4,5
krotka2 = (6,7,8,9,10)
print(krotka1)
print(krotka1[1])
for k1 in krotka1:
    for k2 in krotka2:
        print(k1,"+",k2,"=",k1+k2)
"""

#dictionery - Słowniki

pokoje = {10:"Krzysiek",11:"Wojtek",12:"Michał"}
print(pokoje)
print(pokoje[10])
pokoje[12]="Tomek"
pokoje[15]="Jan"
print(pokoje)
print(pokoje.get(10))
print("-----------------")
print(pokoje)
pokoje.update({20:"Kasia",21:"Zuzia",22:"Marysia",44:"Panda",45:"Małpa",46:"Żuraw",47:"Po"})
print(pokoje)
del(pokoje[47])
print(pokoje)
skasowany1 = pokoje.pop(44)
skasowany2 = pokoje.popitem()
print(skasowany1)
print(skasowany2)
print(pokoje)
pokoje.clear()
print(pokoje)
