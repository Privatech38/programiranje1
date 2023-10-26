def is_prastevilo(num):
    count = 0
    i = 1
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count == 2

prastevila = []
i = 0
while i < 101:
    if is_prastevilo(i):
        prastevila.append(i)
    i += 1

print(prastevila)