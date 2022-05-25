"""
program pozwalający:
    Dodawać nowe definicje
    Szukać istniejących definicji
    usuwać wybrane definicje
    """

definicje = {}
while (True):
    print("1: Dodaj definicję")
    print("2. Znajdź definicję")
    print("3. Usuń definicję")
    print("4. Zakończ")

    wybor = input("Co chcesz zrobić? ")

    if (wybor == "1"):
        klucz = input("podaj słowo do zdefiniowania: ")
        definicja = input("podaj definicję ")
        definicje[klucz] = definicja
        print("definicja dodana pomyślnie")
    elif (wybor == "2"):
        klucz = input("czego szukasz")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("nie znaleziono definicji o nazwie:",klucz)
        
    elif (wybor == "3"):
        klucz = input("Jaką definicję hccesz usunąć? ")
        if klucz in definicje:
            del definicje[klucz]
        else:
            print("nie znaleziono definicji o nazwie:",klucz)
        
    elif (wybor == "4"):
        print("koniec")
        break
    else :
        print("podałeś coś z poza zakresu")
