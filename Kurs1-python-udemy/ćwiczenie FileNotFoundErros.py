
def read_file(path):
    try:
        with open(path, "r") as file:
            return print(file.read())
    except FileNotFoundError:
        print("File does not exist")

nameOfFile = input("File: ")
fileContent = read_file(nameOfFile)