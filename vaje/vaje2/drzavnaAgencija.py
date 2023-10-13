full_price = 0
count = 0
while 1:
    cena = float(input("Cena artikla: "))
    if cena == 0:
        break
    full_price += cena
    count += 1
print("Vsota:", full_price)
print("Povprečje:", full_price / count)