from math import sqrt

number = int(input("Vpiši število: "))
if sqrt(number).is_integer():
    print("Število je kvadrat")
else:
    print("Število ni kvadrat")
