import figury
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'Prostokat Kwadrat')
wybor = int(input('''Wybierz figure: 
1. Prostokat
2. Kwadrat
'''))

if (wybor == Menu_Figury.Prostokat):
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    print("Pole prostokata wynosi: ", figury.pole_prostokata(a, b))
elif (wybor == Menu_Figury.Kwadrat):
    a = float(input("Podaj a: "))
    print("Pole kwadratu wynosi: ", figury.pole_kwadratu(a))
