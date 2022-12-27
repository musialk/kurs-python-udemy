wynik = 0
i = 1
'''
for i in range(3):
    x = int(input("Podaj dodatnia liczbe: "))
    if (x>0):
        wynik += x
    else:
        print("Miala byc liczba dodatnia!")
        break
    print("Aktualny wynik: ", wynik)
'''

'''
while i < 3:
    x = int(input("Podaj dodatnia liczbe: "))
    if (x>0):
        wynik += x
    else:
        print("Miala byc liczba dodatnia!")
        continue
    print("Aktualny wynik: ", wynik)
    i += 1
'''

# while i <= 3:
#     dodatnia = int(input("Podaj liczbe dodatnia, ktora jest parzysta: "))
#     if (dodatnia > 0 and dodatnia % 2 == 0):
#         wynik += dodatnia
#     else:
#         print("Zostaly podane bledne liczby")
#         continue
#     print("Aktualny wynik wynosi: ", wynik)
#     i += 1

# Program pyta uzytkownika zeby podal liczbe i sprawdzal czy uzytkownik zgadnal

secret = 7

while i <=3:
    print("Masz 3 szanse!")
    proba = int(input("Zgadnij liczbe: "))
    if (proba == secret):
        print("Brawo!")
        break
    elif (proba < secret):
        print("Liczba jest za mala. Sprobuj ponownie")
        i += 1
    else:
        print("Liczba jest za duza. Sprobuj ponownie")
        i += 1