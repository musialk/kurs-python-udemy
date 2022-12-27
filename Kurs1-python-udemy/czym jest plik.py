

try:
    file = open('test.txt', "w") #uchwyt handle
    file.write("sample")

    print(0/0)
    file.write("sample")
finally:
    file.close()

