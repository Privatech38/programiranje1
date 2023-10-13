i = 0
count = 0
full_price = 0
while i < 10:
    cena = float(input("Cena: "))
    if cena == 0:
        break
    count += 1
    full_price += cena
    if full_price >= 100:
        break
    i += 1
print("Porabili boste", full_price, "evrov za", count, "stvari")