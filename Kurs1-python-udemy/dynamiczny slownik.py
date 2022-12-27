definicje = {}
print(definicje)

while (True):
    print("1 - dodaj definicje")
    print("2 - znajdz definicje")
    print("3 - usun definicje")
    print("4 - zakoncz")

    wybor = input("Wybierz co chcesz zrobic: ")

    if (wybor == "1"):
        klucz = input("Podaj klucz, czyli slowo do zdefiniowania: ")
        definicja = input("Podaj definicje: ")
        definicje[klucz] = definicja
        print("definicja dodana")
    elif (wybor == "2"):
        klucz = input("Podaj definicje, ktora chcesz znalezc: ")
        if (klucz in definicje):
            print("Znaleziona definicja: ", definicje[klucz])
        else:
            print("Nie ma podanego slowa")
    elif (wybor == "3"):
        klucz = input("Podaj definicje do usuniecia: ")
        if (klucz in definicje):
            del definicje[klucz]
            print("Slowo zostalo usuniete: ", klucz)
        else:
            print("Nie ma podanego slowa")
    elif (wybor == "4"):
        print("Zakonczono dzialanie programu")
        break
