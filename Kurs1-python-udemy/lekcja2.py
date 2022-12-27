# Zmienia literki w wyrazie na pierwsza duza i kolejne male
imie = "arkadiusz"

print(imie)
print(imie.capitalize())

imie = imie.upper()

print(imie)

# # Pobieranie danych od użytkownika oraz rzutowanie
# a = int(input())
# b = int(input())
#
# print("Wynik dodawania to: " + str(a + b))

# Pobieranie imienia od użytkownika, przywitanie go i zapytanie o wiek
imie = str(input("Hej, jak masz na imie?\n"))
imie = imie.capitalize()

print("Czesc", imie, "!")

wiek = int(input("Podaj swoj wiek: "))

print("Zapisany wiek to:", wiek, "lat, dziekuje!")