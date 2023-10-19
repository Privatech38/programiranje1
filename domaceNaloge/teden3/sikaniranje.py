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

def najkrajsaPot(x):
    najblizja = 10
    for cords in ovire:
        if cords[0] <= x <= cords[1] and cords[2] < najblizja:
            najblizja = cords[2]
    return najblizja


# Preveri za kolesarja
x = 4  # stolpec
najblizja_ovira = najkrajsaPot(x)
if najblizja_ovira != 10:
    print("Prva ovira pri", najblizja_ovira)
else:
    print("Ovira ni bila najdena")

# Dodatna naloga
# Izracunaj sirino
sirina = 0
for cords in ovire:
    if cords[1] > sirina:
        sirina = cords[1]

najdalsa_pot = (0, 0)
najdalse_poti = []
# ustvari začetne dolžine z vsak stolpec
x = 1
while x <= sirina:
    trenutna = (x, najkrajsaPot(x))
    najdalse_poti.append(trenutna)
    if trenutna[1] > najdalsa_pot[1]:
        najdalsa_pot = trenutna
    x += 1

print(najdalsa_pot[0], ",", ("Zmaga" if najdalsa_pot[1] == 10 else najdalsa_pot[1]))