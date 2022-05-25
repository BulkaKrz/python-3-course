"""
ĆWICZENIE:

Wczytaj imiona i nazwiska z pliku o nazwie:
imionanazwiska.txt

1) rozdziel je tak, by powstała lista krotek, gdzie wewnętrzne krotki to
pary imiona/nazwiska
2) zapisz imiona do pliku imiona.txt
3) zapisz nazwiska do pliu nazwiska.txt

Zastanów się jak rozwiązać problem,
gdy nie ma podanego nazwiska w pliku imionanazwiska.txt, gdy będziesz
zapsywał nazwiska do pliku nazwiska.txt


[
 ("Arkadiusz", "Włodarczyk"),
 ("Jakis", "Ziom")
]

"""

nameAndSurnameList = []


with open('imionanazwiska.txt','r', encoding='UTF-8') as file:
   for line in file:
       nameAndSurnameList.append(tuple(line.replace('\n','').split(' ')))


with open('imiona.txt','w', encoding='UTF-8') as file:
    for item in nameAndSurnameList:
        file.write(item[0] + "\n")

with open('nazwiska.txt','w', encoding='UTF-8') as file:
    for item in nameAndSurnameList:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")
            

"""
        if len(item) == 2:
            file.write(item[1] + "\n")
        else:
            file.write("\n")

"""


        
