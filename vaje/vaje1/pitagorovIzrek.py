from math import sqrt

kateta1 = float(input("Dolzina prve katete (v cm): "))
kateta2 = float(input("Dolzina druge katete (v cm): "))
hipotenuza = sqrt(kateta1 ** 2 + kateta2 ** 2)
print("Dolžina hipotenuze:", round(hipotenuza, 1), "cm")