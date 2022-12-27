names = {"Ola", "Jan", "Arkadiusz", "Jarek", "Stanisław"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': 20, 't2': -15, 't3': 10, 't4': 6}

namesLenght = {
    name: len(name)
    for name in names
    if name.startswith("J")
}

print(namesLenght)

multiply = {
    numer: numer*numer
    for numer in numbers
}

print(multiply)

fahrenheit = {
    key: temp*1.8+38
    for key, temp in celcius.items()
    if temp > 5
    if temp < 20
}

print(fahrenheit)