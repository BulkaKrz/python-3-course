listaGości = {
                ("Arkadiusz",28,"mężczyzna"),
                ("Weronika",28,"kobieta"),
                ("Zuzanna",28,"kobieta"),
                ("Piotr",28,"mężczyzna"),
                ("Tomasz",28,"mężczyzna"),
                ("Katarzyna",28,"kobieta"),
                ("Karol",20,"mężczyzna")
            }

"""
for imie, wiek, plec in listaGości:
    print("Imię:\t", imie)
    print("Wiek:\t", wiek)
    print("Płeć:\t", plec)
    print("----------------")
"""
people = {
               1: {"name":"Arkadiusz","age":21,"sex":"mężczyzna"},
               2:  {"name":"Weronika","age":28,"sex":"kobieta"},
               3: {"name":"Zuzanna","age":29,"sex":"kobieta"},
               4: {"name":"Piotr","age":24,"sex":"mężczyzna"},
               5: {"name":"Tomasz","age":27,"sex":"mężczyzna"},
               6: {"name":"Katarzyna","age":38,"sex":"kobieta"},
               7: {"name":"Karol","age":33,"sex":"mężczyzna"}
            }


people2 = [
               {"id":1, "name":"Arkadiusz","age":21,"sex":"mężczyzna"},
               {"id":2, "name":"Weronika","age":28,"sex":"kobieta"},
               {"id":3, "name":"Zuzanna","age":29,"sex":"kobieta"},
               {"id":4, "name":"Piotr","age":24,"sex":"mężczyzna"},
               {"id":5, "name":"Tomasz","age":27,"sex":"mężczyzna"},
               {"id":6, "name":"Katarzyna","age":38,"sex":"kobieta"},
               {"id":7, "name":"Karol","age":33,"sex":"mężczyzna"}
            ]


ratings1 = {
        "Arkadiusz" : (3,4,6,4,3,3,3,2),
        "Wiola": (4,2,5,6,4,1)
        }
"""
for record in people2:
    print(record["name"],":", record["sex"])
    print("------------------")


for record in people2:
    for key in record:
        print("{:5s}: {}" .format(key, record[key]))
    print("------------------")


for key2 in people:
    print("ID", key2, ":", people[key2])
    for record in people[key2]:
        print(record, ":", people[key2][record])

print("---------------")

print(people2[1])
print(people2[1]["name"], ": wiek ", people2[1]["age"])

print("ID 4: ",people[4])
print("ID 4: imię :",people[4]["name"])


#for key in ratings1:
#    print(key, "oceny", ratings1[key])
 
"""
for ID, dictionery in people.items():
    print("ID :",ID)

