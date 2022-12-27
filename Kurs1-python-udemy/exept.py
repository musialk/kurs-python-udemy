
namesandsurenames = []

with open("imionanazwiska.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesandsurenames.append(tuple(line.replace("\n", "").split(" ")))

with open("imiona.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurenames:
        file.write(item[0] + "\n")

with open("surenames.txt", "w", encoding="UTF-8") as file:
    for item in namesandsurenames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")