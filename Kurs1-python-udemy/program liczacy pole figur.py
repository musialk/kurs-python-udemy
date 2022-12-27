

def pole_prostokata(a, b):
    return a * b


def pole_kwadratu(a):
    return a * a


def pole_trojkata(a, h):
    return (a * h) / 2


def pole_trapezu(a, b, h):
    return ((a + b) * h) / 2


def pole_kola(r):
    return 3.14 * r ** 2

while(True):
    print("1 - prostokat")
    print("2 - kwadrat")
    print("3 - trojkat")
    print("4 - trapez")
    print("5 - kolo")

    wybor = input("Co chcesz obliczyc? Podaj cyfre z menu: ")

    if wybor == "1":
        a = int(input("Podaj a: "))
        b = int(input("Podaj b: "))
        print("Pole prostokata wynosi: ", pole_prostokata(a, b), "\n")
    elif wybor == "2":
        a = int(input("Podaj a: "))
        print("Pole kwadratu wynosi: ",pole_kwadratu(a), "\n")
    elif wybor == "3":
        a = int(input("Podaj a: "))
        h = int(input("Podaj h: "))
        print("Pole trojkata wynosi: ",pole_trojkata(a, h), "\n")
    elif wybor == "4":
        a = int(input("Podaj a: "))
        h = int(input("Podaj h: "))
        b = int(input("Podaj b: "))
        print("Pole trapezu wynosi: ",pole_trapezu(a, b, h), "\n")
    elif wybor == "5":
        r = int(input("Podaj r: "))
        print("Pole kola wynosi: ",pole_kola(r), "\n")
    elif wybor == "6":
        print("Zakonczono dzialanie programu.")
        break
    else:
        print("Nie ma takiej opcji w menu", "\n")