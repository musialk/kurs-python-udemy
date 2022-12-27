liczby = [1,2,3,4,5]

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)

print(liczbyParzyste)

podegiDwojki2 = [element**2
                 for element in liczby]
print(podegiDwojki2)

liczbyParzyste2 = [element
                   for element in liczby
                   if element % 2 == 0]
print(liczbyParzyste2)
