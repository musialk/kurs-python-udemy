osoba1 = ("Arkadiusz", 29, "mezczyzna")
osoba2 = ("Monika", 30, "kobieta")
osoba3 = ("Jan", 9, "mezczyzna")

ListaGosci = [
    ["Arkadiusz", 29, "mezczyzna"],
    ["Monika", 30, "kobieta"],
    ["Jan", 9, "mezczyzna"]
]

print(ListaGosci[0])
print(ListaGosci[1][-1])

ListaGosci[0][1] = 28
print(ListaGosci[0])

# mozna miec krotke w liscie albo krotke w krotce rowniez

for imie, wiek, plec in ListaGosci:
    print("imie", imie)
    print("wiek", wiek)
    print("plec", plec)
    print("\n")

# mozna rowniez slownik w slowniku albo slownik w liscie

people3 = ["Arkadiusz",
           "Wiola",
           "Kuba"]

oceny = {
    "Arkadiusz": (2,3,4,6,5),
    "Wiola": (3,6,5,4,1)
}

oceny1 = [
    {'name': "Arkadiusz", 'ratings': (2,5,3,4,6), 'behaviour': 4},
    {'name': "Wiola", 'ratings': (4,6,2,3,4), 'behaviour': 3}
]

oceny2 = {
    "Arkadiusz": {'ratings': (2,5,3,4,6), 'behaviour': 4},
    "Wiola": {'ratings': (4,6,2,3,4), 'behaviour': 3}
}

# print(oceny["Arkadiusz"])
# print(oceny["Wiola"])

for key in oceny:
    print(key, "oceny", oceny[key])

# for value in people3:
#     for key in value:
#         print(key, "oceny", value[key])
