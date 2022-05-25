import math

def prostokat(a,b):
    return a * b

def kwadrat(a):
    return a ** 2

def trojkat(a,h):
    return (a * h)/2

def trapez(a,b,h):
    return (a+b)/2 *h

def kolo(r):
    return math.pi * r **2


while True:
    print("""
-------MENU------------
1 - prostokąt
2 - kwadrat
3 - trójkąt
4 - trapez
5 - koło
0 - koniec
-----------------------""")

    choice = input("Wprowadź wybór: ")

    if (choice == "1"):
        print(" - - prostokąt - -")
        a = float(input("podaj pierwszy bok a= "))
        b = float(input("podaj pierwszy bok b= "))
        p = (prostokat(a,b))
        
        print("pole prostokąta o bokach {} i {} wynosi {:.3f}" .format(a,b,p))       
        
    elif (choice == "2"):
        print(" - - kwadrat - -")
        a = float(input("podaj bok kwadratu a= "))
        p = (kwadrat(a))
        print("pole kwadratu o boku {} wynosi {}" .format(a,p))
        
    elif (choice == "3"):
        print(" - - trójkąt - -")
        a = float(input("podaj podstawę trójkąta a= "))
        h = float(input("podaj wysokość trójkąta h= "))
        p = (trojkat(a,h))
        print("pole trójkąta o podstawie {} i wydokości {} wynosi {}" .format(a,h,p))
    elif (choice=="4"):
        print(" - - trapez - -")
        a = float(input("podaj podstawę_1 trapezu a= "))
        b = float(input("podaj podstawę_2 trapezu b= "))
        h = float(input("podaj wysokość trapezu h= "))
        p = (trapez(a,b,h))
        print("pole trójkąta o podstawie_1 = {}, podstawie_2 = {} wydokości = {} wynosi {:.3f}" .format(a,b,h,p))
    elif (choice=="5"):
        print(" - - koło - -")
        r = float(input("podaj promień koła r= "))
        p = (kolo(r))
        print("pole kola o promieniu r = {} wynosi {:.3f}" .format(r,p))       
      
    elif (choice=="0"):
        print('koniec')
        break
    else:
        print('Niewłąściwy wybór')

print()


