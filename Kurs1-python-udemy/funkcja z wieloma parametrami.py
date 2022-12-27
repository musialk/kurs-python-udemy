def pole_prostokata(a, b):
    return a * b

poleProstokataA = pole_prostokata(2, 8)
print(5 * poleProstokataA)

def dzielenie(a, b):
    if (b == 0):
        return
    return a / b

x = dzielenie(10, 5)
if (x):
    print("jest ok", x)
else:
    print("cos nie tak")