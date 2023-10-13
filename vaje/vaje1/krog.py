from math import pi

polmer = float(input("Polmer kroga (v cm): "))
obseg = 2 * pi * polmer
povrsina = pi * polmer ** 2
print("Obseg kroga:", round(obseg, 1), "cm\nPovršina kroga:", round(povrsina, 1), "cm^2")