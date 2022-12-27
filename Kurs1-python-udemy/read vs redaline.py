
with open("oceany.txt", "w") as file:
    file.write("Atlantycki"
               "\nSpokojny"
               "\nIndyjski"
               "\nArktyczny"
               "\nPołudniowy")
    file.close()

with open("oceany.txt", "r") as file:
    '''oceany = file.read().splitlines()
    oceany = file.readlines()
    oceany = file.readline()
    oceany = file.read()
    
print(oceany)'''
    for line in file:
        print(line)
        