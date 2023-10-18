import random

# Ustvari ovire
ovire = []

i = 1
while i < 9:
    i += 1
    length = random.randint(0, 5)
    position = random.randint(0, 5)
    if position == 0:
        continue
    ovire.append((position, position + length, i))
print(ovire)

# Preveri za kolesarja
x = 4  # stolpec
najblizja = 10
for cords in ovire:
    if cords[0] <= x <= cords[1] and cords[2] < najblizja:
        najblizja = cords[2]
if najblizja == 10:
    print("Prva ovira pri", najblizja)
else:
    print("Ovira ni bila najdena")

# Dodatna naloga
sirina = 0
for cords in ovire:
    if cords[1] > sirina:
        sirina = cords

najdalsa_pot = (0,0)
for cords in ovire:
