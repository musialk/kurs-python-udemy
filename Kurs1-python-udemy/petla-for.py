# while licznik <= ilosc:
#     liczba = int(input("Podaj liczbe: "))
#     wynik += liczba
#     licznik += 1
# print("Wynik sumowania: ", wynik)
'''
wynik = 0
ilosc = int(input("Podaj ilosc liczb: "))

for i in range(ilosc):
    liczba = int(input("Podaj liczbe: "))
    wynik += liczba

print("Wynik sumowania: ", wynik)
'''
# Wypisz liczby podzielne przez 5 i niepodzielne przez 7

number = int(input("Podaj liczbe: "))
for i in range(number):
    if (i % 5 == 0 and i % 7 != 0):
        print(i)