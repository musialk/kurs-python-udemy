def sumuj_do(liczba):
    suma = 0
    for liczba in range(1, 6):
        suma = suma + liczba
    return suma

def sumuj_do2(liczba):
    return sum([liczba
                for liczba in range(1, liczba+1)])

print(sumuj_do2(50))