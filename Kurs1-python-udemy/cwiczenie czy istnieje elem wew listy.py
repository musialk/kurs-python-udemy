import time

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

def funkcion_performance(func, *arg, how_many_times = 1):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter();
        sum = sum + (end - start)
    return sum

def is_elem_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False

print(funkcion_performance(is_elem_in,450,setContainer, how_many_times=3000))
print(funkcion_performance(is_elem_in,450,listContainer, how_many_times=3000))

#Argumenty pozycyjne (nienazwane) muszą być przed argumentami nazwanymi (kluczowymi)