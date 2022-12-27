import random

list = []

def choose_numbers(amount, total):
    x=0
    while x < amount:
        numer = random.randint(amount, total)
        if numer not in list:
            list.append(numer)
        else:
            continue
        x = x+1

choose_numbers(6, 49)
print(set(list))