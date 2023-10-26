stevilo = int(input("Vpiši število: "))

count = 0
i = 1
while i < stevilo:
    if stevilo % i == 0:
        count += i
    i += 1

print(count)