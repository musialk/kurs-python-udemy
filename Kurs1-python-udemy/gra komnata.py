import random

eventDictionary = {
    "Skrzynia":0.6,
    "Nic":0.4
}

gameLegth = 5

print("Welcome in game")
print("U can go just 5 steps forward")
print("We'll see what u get'")

while gameLegth > 0:
    gamerAnswer = input("Do u want move forward?")
    if (gamerAnswer == "yes"):
        print("Okej, lets see what u got... ")

    else:
        print("U can move just straight")
        continue
    gameLegth = gameLegth - 1
