# kopia płytka
import copy


def evil_function(toBeDestroyedList):
    toBeDestroyedList.clear()


myList = [1, 2, 3]

print(evil_function(myList.copy()))
print(evil_function(copy.deepcopy(myList)))