"""
program pozwalający:
    Dodawać nowe definicje
    Szukać istniejących definicji
    usuwać wybrane definicje
    """

definicje = {}

while True:
    print("1. Dodaj nową definicję")
    print("2. szukaj definicji")
    print("3. usuń definicję")
    print("4. wyjdź")
    choice = int(input("wybierz 1,2,3,4: "))

    if choice == 1:
        print("dodaj pozycję do słownika")
        word = input("podaj słowo: ")
        definition = input("podaj definicje: ")
        definicje.update({word:definition})
        print("--------")
        print(definicje)
    elif choice == 2:
        print("wybierz ze słownika")
        word = input("podaj słowo: ")
        print(definicje[word])
    elif choice == 3:
        print("usuwanie słowa ze słownika")
        word = input("podaj słowo: ")
        del(definicje[word])
    elif choice == 4:
        break
print(definicje)




