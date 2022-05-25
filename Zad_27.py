# LISTY
"""
names = ["Arkasiusz", "Wioletta", "Karol", "Kuba", "Adrian"]
liczby = [1,4,56,-23,20,7]
mixlist = [1,"aa",45,"kra"]

print(names)
print("-----------------------")

for name in names:
    print(name)

print(mixlist[1])

print(names)
names[-1] = "Wojtek"
print(names)

print("Wojtek" in names)

if 2 not in liczby:
    print("nie ma liczby 2")
else:
    print("liczna 2 jest w liście")

print(3*liczby)     #potraja listę
print([4]+liczby)   # dodaje listę [4] do listy
print([4,5,7,8]+liczby)     #daje list4,5,7,8 do listy
print(4+int(liczby[2]))     #dodaje do 4 liczbę int pozycja 3 na liście czyli 4+ 56

print(liczby)
liczby = [6,7,8,9,10,11] + liczby   #na stałe zmienia listę
print(liczby)
print("----------------------")
print(len(liczby))

"""
lista1 = [54,1,-2,20,1]
lista2 = ["Arkadiusz", "Wioletta"]
print(lista1)
print(lista1 +[4])

lista1.append(5)
print(lista1)

lista1.extend([2,12,24,2])
print(lista1)

#lista1.append([2,12,24,2])
#print(lista1)
print("-------------------")
print(lista2)
lista2.insert(1,"Kuba")
print(lista2)
print("-------------------")
print(lista1.index(54))
print(lista2.index("Wioletta"))
print("-------------------")

lista1.sort()
print(lista1)
lista1.sort(reverse=True)
print(lista1)

print(max(lista1))
print(min(lista1))
print(lista1.count(2))
"""
print("-----------------")
print(lista1)
for i in range(len(lista1)):
    print(len(lista1))
    print(lista1[-1])
    lista1.pop()
    print(lista1)
"""
print(lista1)
lista1.remove(2)
print(lista1)

print(lista2)
lista2.clear()
print(lista2)










































