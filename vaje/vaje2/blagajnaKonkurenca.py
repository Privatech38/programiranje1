
amount = int(input("Število izdelkov: "))
i = 0
full_price = 0
while i < amount:
    full_price += float(input("Cena artikla: "))
    i += 1
print("Vsota:", full_price)