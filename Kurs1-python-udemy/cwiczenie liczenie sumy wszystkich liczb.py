#dokończyć ćwiczenie - zrobic funkcje ktora przy wywołaniu podanego printa wypisze 28, czyli sume wszystkich w princie

def count(*n):
    suma = 0
    for i in n:
        suma = suma + i
    return suma

print(count(2,4,1,2,4,5,10))

