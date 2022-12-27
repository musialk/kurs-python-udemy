imiona = ["Arkadiusz", "Ola", "Karol", "Kacper"]
liczby = [1, 54, -20]
mieszana = ["Ola", 5, "a"]

'''
for imie in imiona:
    print(imie)
'''

# Wybor elementu ostatniego
print(imiona[-1])

# Czy dany element jest w liscie?
print("Arkadiusz" in imiona)

if ("Wojtek" in imiona):
    print("Czesc Wojtek!")
else:
    print("Nie ma takiego imienia.")

# Dodawanie pozycji w liscie
liczby = [2, 3] + liczby
print(liczby)

# Dlugosc
print(len(mieszana))

# Dodawanie do konca listy
liczby.append(4)
print(liczby)

# Rozszerzanie listy
liczby.extend([12, 14, 16])
print(liczby)

# Wstawianie
liczby.insert(2, -50)
print(liczby)

# Indeks danego elementu
print(liczby.index(1))

# Sortowanie
liczby.sort(reverse=False)
print(liczby)

# Usuwanie ostatniego elementu
liczby.pop()
print(liczby)

# Usuwanie pierwszy napotkany dany element
liczby.remove(1)
print(liczby)