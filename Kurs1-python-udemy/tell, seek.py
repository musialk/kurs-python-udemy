
with open("oceany.txt") as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell())
    file.seek(0)
    print(file.tell())
    file.seek(5)
    print(file.readline())
    print(file.tell())