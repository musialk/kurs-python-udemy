import random
from collections import Counter

x = 0

while x < 100:
    x = x + 1
    print(random.random())


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if isHitChance < weaponChanceToHitPercentage:
        return "hit"
    else:
        return "not hit"


print(will_weapon_hit(50))

x = 0

listHit = []

while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

print(listHit)
print(listHit.count("hit"))

dictionaryHit = Counter(listHit)

print(dictionaryHit)
