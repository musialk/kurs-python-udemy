evenNumbers = [element
               for element in range(400)
               if (element % 2 == 0)
               ]

# generator stworzony, oszczedza miejsce
evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0)
                        )

print(evenNumbers)
print(evenNumbersGenerator)

for item in evenNumbersGenerator:
    print(item)

genPotega = (element ** 2
             for element in range(100)
             )

for item in genPotega:
    print(item)