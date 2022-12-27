import random
from collections import Counter

movieList = ["Tytuł 1", "Tytul 2", "Tytul 3"]

event = ["smierc", "narodziny", "slub", "wygrana", "przegrana"]

nagrodaZeSkrzynki = ["zielona", "pomaranczowa", "purpurowa","legendarna"]

print(random.choice(movieList))
print(random.choices(nagrodaZeSkrzynki, k=100))
print(Counter(random.choices(nagrodaZeSkrzynki, [1,2,1,2], k=100)))