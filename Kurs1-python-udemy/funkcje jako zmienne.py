# funkcja jako zmienna
import time


def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba + 1)])


def funkcion_performance(func, arg, how_many_times = 1):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter();
        sum = sum + (end - start)
    return sum

# z lekcji domyslnych argumentow
print(funkcion_performance(sumuj_do2, 500000, 20))

def increment(x, amount = 1):
    return x + amount

increment(4)