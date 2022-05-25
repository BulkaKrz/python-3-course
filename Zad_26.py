import random

szukanaLiczba = random.randrange(10,20)
while (True):
    zgadywanaLiczba = int(input("odgadnij liczbę: "))
    if zgadywanaLiczba == szukanaLiczba:
        print("-------------------")
        print("---Zgadłeś SUPER---")
        print("-------------------")
        break
    elif zgadywanaLiczba > szukanaLiczba:
        print("Za DUŻA. Spróbuj jeszcze raz")
    else:
        print("Za MAŁA. Spróbuj jeszcze raz")
