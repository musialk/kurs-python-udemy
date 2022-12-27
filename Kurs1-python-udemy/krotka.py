krotka = (1, -3, 42, 5)
# krotka jest niezmienna, zajmuje mniej pamięci niż lista

slownik = {49: "spedzam czas w pokoju 49", 69: "moja zona jest w pokoju 69"}
slownik[49] = "Jan Kowalski"
slownik[50] = "Jacek Mucha"

print(slownik)

slownik.update({500: "ktos", 400: "owca"})

print(slownik)

slownik.pop(69)

print(slownik)

#zbior
A = {1, 4, -20, 2}
print(A)
