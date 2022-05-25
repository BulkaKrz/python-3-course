import figury
# enumeration - spis wyliczenie trzeba zaimportować bibliotekę enum
from enum import IntEnum
menu = ['Kwadrat', 'Prostokąt', 'Kolo' , 'Trójkąt', 'Trapez', 'Koniec']
a=1
Menu_Figury = IntEnum('Menu_Figury', menu)
while True:
    print("----MENU___")
    for i in menu:
        print(a,"-",i)
        a = a+1
    wybor = int(input(""" wybierz figurę którą chcesz obliczyć:
    """))

    if (wybor == Menu_Figury.Kwadrat):
        a = float(input("Podaj bok kwadratu a = "))
        print("pole kwadratu wynosi :{:.2f}" .format(figury.pole_kwadratu(a)))
    elif (wybor == Menu_Figury.Prostokąt):
        a = float(input("podaj pierwszy bok a= "))
        b = float(input("podaj pierwszy bok b= "))
        print("pole prostokąta o bokach {} i {} wynosi {:.2f}" .format(a,b,figury.pole_prostokata(a,b)))
    elif (wybor == Menu_Figury.Kolo):
        r = float(input("podaj promień koła r= "))
        print("pole kola o promieniu r = {} wynosi {:.2f}" .format(r,figury.pole_kola(r)))
    elif (wybor == Menu_Figury.Trójkąt):
        a = float(input("podaj podstawę trójkąta a= "))
        h = float(input("podaj wysokość trójkąta h= "))
        print("pole trójkąta o podstawie {} i wydokości {} wynosi {:.2f}" .format(a,h,figury.pole_trojkata(a,h)))
    elif (wybor == Menu_Figury.Trapez):
        a = float(input("podaj podstawę_1 trapezu a= "))
        b = float(input("podaj podstawę_2 trapezu b= "))
        h = float(input("podaj wysokość trapezu h= "))
        print("pole trójkąta o podstawie_1 = {}, podstawie_2 = {} wydokości = {} wynosi {:.2f}" .format(a,b,h,figury.pole_trapezu(a,b,h)))
    elif (wybor == Menu_Figury.Koniec):
        break
    
    else:
        print("błędny wybór")

