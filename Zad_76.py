
def openFileAndRead(filename):
    try:
        with open(filename, 'r', encoding = "UTF-8") as file:
            return (file.read())
    except FileNotFoundError:
        print("Plik nie istnieje")
        


filename = input("podaj nazwę pliku do wczytania: ")

print(openFileAndRead(filename))
