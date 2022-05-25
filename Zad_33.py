listaGości = [
                ["Arkadiusz",28,"mężczyzna"],
                ["Weronika",28,"kobieta"],
                ["Zuzanna",28,"kobieta"],
                ["Piotr",28,"mężczyzna"],
                ["Tomasz",28,"mężczyzna"],
                ["Katarzyna",28,"kobieta"]
            ]
print(listaGości[1])
print(listaGości[1][2])
print(listaGości[1][0])

listaGości2 = [
                ("Arkadiusz",28,"mężczyzna"),
                ("Weronika",28,"kobieta"),
                ("Zuzanna",28,"kobieta"),
                ("Piotr",28,"mężczyzna"),
                ("Tomasz",28,"mężczyzna"),
                ("Katarzyna",28,"kobieta")
            ]
print(listaGości2[1])
print(listaGości2)
listaGości2.append(("Karol",20,"mężczyzna"))
print(listaGości2)



listaGości3 = {
                ("Arkadiusz",28,"mężczyzna"),
                ("Weronika",28,"kobieta"),
                ("Zuzanna",28,"kobieta"),
                ("Piotr",28,"mężczyzna"),
                ("Tomasz",28,"mężczyzna"),
                ("Katarzyna",28,"kobieta"),
            }
print(listaGości[1])
print(listaGości[1][2])
print(listaGości[1][0])

listaGości4 = {
                ("Arkadiusz",28,"mężczyzna"),
                ("Weronika",28,"kobieta"),
                ("Zuzanna",28,"kobieta"),
                ("Piotr",28,"mężczyzna"),
                ("Tomasz",28,"mężczyzna"),
                ("Katarzyna",28,"kobieta"),
                ("Karol",20,"mężczyzna")
            }

print("============3|4=============")
print(listaGości3 | listaGości4)
print("============3^4=============")
print(listaGości3 ^ listaGości4)
print("===========3&4==============")
print(listaGości3 & listaGości4)
print("===========4-3==============")
print(listaGości4 - listaGości3)
print("===========3-4==============")
print(listaGości3 - listaGości4)






