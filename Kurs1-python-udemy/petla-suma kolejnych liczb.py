licznik = 1
wynik = 0
ilosc = int(input("Podaj ilosc liczb: "))

while licznik <= ilosc:
    liczba = int(input("Podaj liczbe: "))
    wynik += liczba
    licznik += 1
print("Wynik sumowania: ", wynik)