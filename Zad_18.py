"""
a = int(input("podaj liczbę: "))

if a >= 0:
    print(a)
elif a< 0:
    print(a*(-1))


a = int(input("czu liczba z zakresu od 1 do 10: "))
if a>=1:
    if (a <= 10):
        print("jest ok")
    else:
        print("nie jest ok")
else:
    print("nie jest ok")


a = 100
while a >= 0:
    print(a)
    a-=1


wynik = 0
i = 0
while i < 4:
    x = int(input("podaj liczbę: "))
    wynik +=x
    i+=1
print("wynik dodawania liczb to:",wynik)


wynik = 0
i = 0

while i <3:
    x=int(input("Podaj dodatnią liczbę: "))
    if (x > 0):
        wynik +=x

    else:
        print("miała być liczba dodatnia ")
        continue

    i+=1
print("aktualny wynik to:",wynik)
    

"""

wynik = 0
i = 1
while i < 4:
    print("liczna nr",i)
    x = int(input("Podaj liczbę parzystą: "))
    if x % 2 == 0:
        wynik +=x
    else:
        print("miała być liczba parzysta")
        continue
    i+=1
print("\n ----------- wynik dodawania =",wynik)
    












