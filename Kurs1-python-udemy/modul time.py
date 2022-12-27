import time

def sumuj_do(liczba):
    suma = 0

    for liczba in range(1, liczba+1):
        suma = suma + liczba

    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba+1)])

def sumuj_do3(liczba):
    return sum((liczba for liczba in range(1, liczba+1)))

def sumuj_do4(liczba):
    return sum({liczba for liczba in range(1, liczba+1)})

def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba


start = time.perf_counter()
print(sumuj_do(255598525))
end = time.perf_counter()
print(end - start)

start2 = time.perf_counter()
print(sumuj_do2(255598525))
end2 = time.perf_counter()
print(end2 - start2)

start3 = time.perf_counter()
print(sumuj_do3(255598525))
end3 = time.perf_counter()
print(end3 - start3)

start4 = time.perf_counter()
print(sumuj_do4(255598525))
end4 = time.perf_counter()
print(end4 - start4)

start5 = time.perf_counter()
print(sumuj_do5(255598525))
end5 = time.perf_counter()
print(end5 - start5)