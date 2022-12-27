listSample = [1, 4, 512, 24]

listSample2 = listSample

listSample2.append(465)

print(listSample2)
print(id(listSample))
print(id(listSample2))

k = 4

h = 4

print(id(k))
print(id(h))

c = 5

def add(c, amount = 1):
    c = c + amount

add(c)
print(c)