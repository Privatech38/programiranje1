stevilo = int(input("Vpiši število: "))


def vsota_deljiteljev(num):
    amount = 0
    i = 1
    while i < stevilo:
        if num % i == 0:
            amount += i
        i += 1
    return amount


first_count = vsota_deljiteljev(stevilo)

if vsota_deljiteljev(first_count) == stevilo:
    print(first_count)
else:
    print(stevilo, "nima prijateljev")
