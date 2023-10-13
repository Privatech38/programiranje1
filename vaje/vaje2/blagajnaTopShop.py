full_price = 0
while 1:
    cena = float(input("Cena artikla: "))
    if cena == 0:
        break
    full_price += cena
print("Vsota:", full_price)