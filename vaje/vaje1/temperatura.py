temp_F = float(input("Temperatura [°F]? "))
temp_C = (temp_F - 32) * 5 / 9
temp_K = temp_C + 273.15
print(temp_F, "°F je enako", round(temp_C, 1), "°C oz.", round(temp_K, 1), "K")