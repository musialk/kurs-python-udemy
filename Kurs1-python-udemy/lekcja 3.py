#kalkulator

a = int(input("Podaj liczbe:"))
b = int(input("Podaj liczbe:"))


wybor = input("1 - mnozenie, 2 - dzielenie, 3 - dodawanie, 4 - odejmowanie, 5 - potegowanie, 6 - modulo")

if (wybor == '1'):
    print(a * b)
elif (wybor == '2'):
    if (b != 0):
        print(a / b)
    else:
        print("nie dziel przez 0")
elif (wybor == '3'):
    print(a + b)
elif (wybor == '4'):
    print(a - b)
elif (wybor == '5'):
    print(a ** b)
elif (wybor == '6'):
    if (b != 0):
        print(a % b)
    else:
        print("nie dziel przez 0")
else:
    print("zly wybor")
