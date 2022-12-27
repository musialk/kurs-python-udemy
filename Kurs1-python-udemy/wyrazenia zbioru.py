names = {"ola", "jan", "arkadiusz", "jarek", "stanisław", "barbara", "bartłomiej"}

names = {
    name.capitalize()
    for name in names
}

print(names)

names = {
    name.capitalize()
    for name in names
    if name[0] != "B"
}

print(names)