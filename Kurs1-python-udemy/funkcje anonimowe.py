def podwoj(x):
    return x * 2


print(podwoj(4))

test = lambda x: x * 2

print(test(4))

my_list = [2, 3, 6, 8, 13, 56, 43]

print(list(filter(lambda x: x % 2 == 0, my_list)))

my_list_filtr = [x for x in my_list if (x % 2) == 0]
print(my_list_filtr)