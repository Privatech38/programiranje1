stevilo = int(input("Vpiši število: "))

deljitelji = []
i = 1
while i <= stevilo:
    if stevilo % i == 0:
        deljitelji.append(i)
    i += 1

print(deljitelji)