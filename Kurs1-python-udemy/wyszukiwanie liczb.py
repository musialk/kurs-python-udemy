#generator
numbers = (
    number
    for number in range(100,470)
    if number % 7 == 0 and number % 5 != 0
)

print(numbers)

# wyrazenie listowne
numberlist = [
    num
    for num in range(100,470)
    if num % 7 == 0 and num % 5 != 0
]

print(numberlist)

# wyrazenie slownikowe
numbers1 = {
    num: num % 7 == 0 and num % 5 != 0
    for num in range(100,470)
}
print(numbers1)

# wyrazenie zbioru
numberzbior = {
    num
    for num in range(100,470)
    if num % 7 == 0 and num % 5 != 0
}