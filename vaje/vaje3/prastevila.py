stevilo = int(input("Vpiši število: "))


def vsota_deljiteljev(num):
    count = 0
    i = 1
    while i <= stevilo:
        if num % i == 0:
            count += 1
        i += 1
    return count

print(vsota_deljiteljev(stevilo) == 2)
